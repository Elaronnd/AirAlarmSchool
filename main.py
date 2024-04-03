import eel
import requests
from datetime import datetime, timedelta

eel.init('web')


@eel.expose
def get_data_force():
    api_url = 'https://vadimklimenko.com/map/statuses.json'
    response = requests.get(api_url)
    if response.status_code == requests.codes.ok:
        place = "м. Київ"
        if response.json()["states"][place]["enabled"] == True:
            return "[info] На даний момент в Києві повітряна тривога"
        else:
            return "[info] На даний момент в Києві немає повітряної тривоги"
    else:
        return "[error] Error:", response.status_code, response.text


@eel.expose
def get_date_time():
  api_url = 'https://vadimklimenko.com/map/statuses.json'
  response = requests.get(api_url)
  if response.status_code == requests.codes.ok:
    place = "м. Київ"
    if response.json()["states"][place]["enabled_at"] == None:
      time = response.json()["states"][place]["disabled_at"][11:19]
      date = response.json()["states"]["м. Київ"]["disabled_at"][0:10]
      if time[0:2] == ["21", "22", "23", "24"]:
        date = datetime.strptime(date, "%Y-%m-%d")
        date += timedelta(days=1)
        date = date.strftime("%Y-%m-%d")
      time = datetime.strptime(time, "%H:%M:%S")
      time += timedelta(hours=3)
      time = time.strftime("%H:%M:%S")
      return f"Остання тривога була {date} в {time}"
    else:
      time = response.json()["states"][place]["enabled_at"][11:19]
      date = response.json()["states"]["м. Київ"]["enabled_at"][0:10]
      if time[0:2] == ["21", "22", "23", "24"]:
        date = datetime.strptime(date, "%Y-%m-%d")
        date += timedelta(days=1)
        date = date.strftime("%Y-%m-%d")
      time = datetime.strptime(time, "%H:%M:%S")
      time += timedelta(hours=3)
      time = time.strftime("%H:%M:%S")
      return f"Тривога триває з {date} в {time}"

eel.start('index.html', port=80, mode=None, shutdown_delay=float('inf'))
