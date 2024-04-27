import eel
import requests
import datetime
from lessons import lesson as les
from typing import Optional

eel.init('web')


@eel.expose
def get_data_force(place="м. Київ") -> Optional[bool]:
    api_url = 'https://vadimklimenko.com/map/statuses.json'
    response = requests.get(api_url)
    if response.status_code == requests.codes.ok:
        if response.json()["states"][place]["enabled"] is True:
            return True
        else:
            return False
    else:
        return None


@eel.expose
def get_date_time(place="м. Київ") -> str:
    api_url = 'https://vadimklimenko.com/map/statuses.json'
    response = requests.get(api_url)
    if response.status_code == requests.codes.ok:
        if response.json()["states"][place]["enabled_at"] is None:
            time = response.json()["states"][place]["disabled_at"][11:19]
            date = response.json()["states"][place]["disabled_at"][0:10]
            if time[0:2] == ["21", "22", "23", "24"]:
                date = datetime.datetime.strptime(date, "%Y-%m-%d")
                date += datetime.timedelta(days=1)
                date = date.strftime("%Y-%m-%d")
            time = datetime.datetime.strptime(time, "%H:%M:%S")
            time += datetime.timedelta(hours=3)
            time = time.strftime("%H:%M:%S")
            return f"Остання тривога закінчилася {date} в {time}"
        else:
            time = response.json()["states"][place]["enabled_at"][11:19]
            date = response.json()["states"][place]["enabled_at"][0:10]
            if time[0:2] in ["21", "22", "23", "24"]:
                date = datetime.datetime.strptime(date, "%Y-%m-%d")
                date += datetime.timedelta(days=1)
                date = date.strftime("%Y-%m-%d")
            time = datetime.datetime.strptime(time, "%H:%M:%S")
            time += datetime.timedelta(hours=3)
            time = time.strftime("%H:%M:%S")
            return f"Тривога триває з {date} в {time}"
    else:
        return "Помилка з API"


@eel.expose
def lesson() -> str:
    return les()


eel.start('index.html', host="0.0.0.0", port=80, mode=None, shutdown_delay=float('inf'))
