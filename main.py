import eel
import requests
import datetime

eel.init('web')


@eel.expose
def get_data_force(place):
    api_url = 'https://vadimklimenko.com/map/statuses.json'
    response = requests.get(api_url)
    if response.status_code == requests.codes.ok:
        if response.json()["states"][place]["enabled"] is True:
            return True
        else:
            return False
    else:
        return "Помилка з api"


@eel.expose
def get_date_time(place):
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
            return f"Остання тривога була {date} в {time}"
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
def lesson(place):
    current_time = datetime.datetime.now()
    current_week = current_time.weekday()
    api_url = 'https://vadimklimenko.com/map/statuses.json'
    response = requests.get(api_url)
    if response.status_code == requests.codes.ok:
        if response.json()["states"][place]["enabled"] is False or response.json()["states"][place]["enabled"] is True:
            if datetime.time(8, 30) > current_time.time():
                return "Уроки поки що не почалися"
            elif datetime.time(15, 5) < current_time.time():
                return "Уроки закінчилися, йди додому"
            elif current_week in [5, 6]:
                return "Відпочивай зараз вихідний день!"
            elif datetime.time(9, 15) <= current_time.time() <= datetime.time(9, 25):
                return f"Зараз перша маленька перерва (Вона вже йде - {datetime.datetime.combine(datetime.date.today(), datetime.datetime.now().time()).replace(microsecond=0) - datetime.datetime.combine(datetime.date.today(), datetime.time(9, 15)).replace(microsecond=0)})"
            elif datetime.time(10, 10) <= current_time.time() <= datetime.time(10, 30):
                return f"Зараз перша велика перерва (Вона вже йде - {datetime.datetime.combine(datetime.date.today(), datetime.datetime.now().time()).replace(microsecond=0) - datetime.datetime.combine(datetime.date.today(), datetime.time(10, 10)).replace(microsecond=0)})"
            elif datetime.time(11, 15) <= current_time.time() <= datetime.time(11, 35):
                return f"Зараз друга велика перерва (Вона вже йде - {datetime.datetime.combine(datetime.date.today(), datetime.datetime.now().time()).replace(microsecond=0) - datetime.datetime.combine(datetime.date.today(), datetime.time(11, 15)).replace(microsecond=0)})"
            elif datetime.time(12, 20) <= current_time.time() <= datetime.time(12, 30):
                return f"Зараз друга маленька перерва (Вона вже йде - {datetime.datetime.combine(datetime.date.today(), datetime.datetime.now().time()).replace(microsecond=0) - datetime.datetime.combine(datetime.date.today(), datetime.time(12, 20)).replace(microsecond=0)})"
            elif datetime.time(13, 15) <= current_time.time() <= datetime.time(13, 25):
                return f"Зараз третя маленька перерва (Вона вже йде - {datetime.datetime.combine(datetime.date.today(), datetime.datetime.now().time()).replace(microsecond=0) - datetime.datetime.combine(datetime.date.today(), datetime.time(13, 15)).replace(microsecond=0)})"
            elif datetime.time(14, 10) <= current_time.time() <= datetime.time(14, 20):
                return f"Зараз четверта маленька перерва (Вона вже йде - {datetime.datetime.combine(datetime.date.today(), datetime.datetime.now().time()).replace(microsecond=0) - datetime.datetime.combine(datetime.date.today(), datetime.time(14, 10)).replace(microsecond=0)})"

            elif current_week == 0 and datetime.time(8, 30) <= current_time.time() <= datetime.time(9, 15):
                return f"Зараз перший урок: Українська мова або Англійська мова (Вона вже йде - {datetime.datetime.combine(datetime.date.today(), datetime.datetime.now().time()).replace(microsecond=0) - datetime.datetime.combine(datetime.date.today(), datetime.time(8, 30)).replace(microsecond=0)})"
            elif current_week == 0 and datetime.time(9, 25) <= current_time.time() <= datetime.time(10, 10):
                return f"Зараз другий урок: Українська мова або Англійська мова (Вона вже йде - {datetime.datetime.combine(datetime.date.today(), datetime.datetime.now().time()).replace(microsecond=0) - datetime.datetime.combine(datetime.date.today(), datetime.time(9, 25)).replace(microsecond=0)})"
            elif current_week == 0 and datetime.time(10, 30) <= current_time.time() <= datetime.time(11, 15):
                return f"Зараз третій урок: Англійська мова або Українська мова (Вона вже йде - {datetime.datetime.combine(datetime.date.today(), datetime.datetime.now().time()).replace(microsecond=0) - datetime.datetime.combine(datetime.date.today(), datetime.time(10, 30)).replace(microsecond=0)})"
            elif current_week == 0 and datetime.time(11, 35) <= current_time.time() <= datetime.time(12, 20):
                return f"Зараз четвертий урок: Англійська мова або Українська мова (Вона вже йде - {datetime.datetime.combine(datetime.date.today(), datetime.datetime.now().time()).replace(microsecond=0) - datetime.datetime.combine(datetime.date.today(), datetime.time(11, 35)).replace(microsecond=0)})"
            elif current_week == 0 and datetime.time(12, 30) <= current_time.time() <= datetime.time(13, 15):
                return f"Зараз п'ятий урок: Хімія (Вона вже йде - {datetime.datetime.combine(datetime.date.today(), datetime.datetime.now().time()).replace(microsecond=0) - datetime.datetime.combine(datetime.date.today(), datetime.time(12, 30)).replace(microsecond=0)})"
            elif current_week == 0 and datetime.time(13, 25) <= current_time.time() <= datetime.time(14, 10):
                return f"Зараз шостий урок: Хімія (Вона вже йде - {datetime.datetime.combine(datetime.date.today(), datetime.datetime.now().time()).replace(microsecond=0) - datetime.datetime.combine(datetime.date.today(), datetime.time(13, 25)).replace(microsecond=0)})"
            elif current_week == 0 and datetime.time(14, 20) <= current_time.time() <= datetime.time(15, 5):
                return f"Зараз сьомий урок: Фізичка культура (Вона вже йде - {datetime.datetime.combine(datetime.date.today(), datetime.datetime.now().time()).replace(microsecond=0) - datetime.datetime.combine(datetime.date.today(), datetime.time(14, 20)).replace(microsecond=0)})"

            elif current_week == 1 and datetime.time(8, 30) <= current_time.time() <= datetime.time(9, 15):
                return f"Зараз перший урок: Українська література (Вона вже йде - {datetime.datetime.combine(datetime.date.today(), datetime.datetime.now().time()).replace(microsecond=0) - datetime.datetime.combine(datetime.date.today(), datetime.time(8, 30)).replace(microsecond=0)})"
            elif current_week == 1 and datetime.time(9, 25) <= current_time.time() <= datetime.time(10, 10):
                return f"Зараз другий урок: Українська література (Вона вже йде - {datetime.datetime.combine(datetime.date.today(), datetime.datetime.now().time()).replace(microsecond=0) - datetime.datetime.combine(datetime.date.today(), datetime.time(9, 25)).replace(microsecond=0)})"
            elif current_week == 1 and datetime.time(10, 30) <= current_time.time() <= datetime.time(11, 15):
                return f"Зараз третій урок: Фізика (Вона вже йде - {datetime.datetime.combine(datetime.date.today(), datetime.datetime.now().time()).replace(microsecond=0) - datetime.datetime.combine(datetime.date.today(), datetime.time(10, 30)).replace(microsecond=0)})"
            elif current_week == 1 and datetime.time(11, 35) <= current_time.time() <= datetime.time(12, 20):
                return f"Зараз четвертий урок: Біологія (Вона вже йде - {datetime.datetime.combine(datetime.date.today(), datetime.datetime.now().time()).replace(microsecond=0) - datetime.datetime.combine(datetime.date.today(), datetime.time(11, 35)).replace(microsecond=0)})"
            elif current_week == 1 and datetime.time(12, 30) <= current_time.time() <= datetime.time(13, 15):
                return f"Зараз п'ятий урок: Біологія (Вона вже йде - {datetime.datetime.combine(datetime.date.today(), datetime.datetime.now().time()).replace(microsecond=0) - datetime.datetime.combine(datetime.date.today(), datetime.time(12, 30)).replace(microsecond=0)})"
            elif current_week == 1 and datetime.time(13, 25) <= current_time.time() <= datetime.time(14, 10):
                return f"Зараз шостий урок: Фізична культура (Вона вже йде - {datetime.datetime.combine(datetime.date.today(), datetime.datetime.now().time()).replace(microsecond=0) - datetime.datetime.combine(datetime.date.today(), datetime.time(13, 25)).replace(microsecond=0)})"
            elif current_week == 1 and datetime.time(14, 20) <= current_time.time() <= datetime.time(15, 5):
                return f"Зараз сьомий урок: Географія (Вона вже йде - {datetime.datetime.combine(datetime.date.today(), datetime.datetime.now().time()).replace(microsecond=0) - datetime.datetime.combine(datetime.date.today(), datetime.time(14, 20)).replace(microsecond=0)})"

            elif current_week == 2 and datetime.time(8, 30) <= current_time.time() <= datetime.time(9, 15):
                return f"Зараз перший урок: Алгебра (Вона вже йде - {datetime.datetime.combine(datetime.date.today(), datetime.datetime.now().time()).replace(microsecond=0) - datetime.datetime.combine(datetime.date.today(), datetime.time(8, 30)).replace(microsecond=0)})"
            elif current_week == 2 and datetime.time(9, 25) <= current_time.time() <= datetime.time(10, 10):
                return f"Зараз другий урок: Алгебра (Вона вже йде - {datetime.datetime.combine(datetime.date.today(), datetime.datetime.now().time()).replace(microsecond=0) - datetime.datetime.combine(datetime.date.today(), datetime.time(9, 25)).replace(microsecond=0)})"
            elif current_week == 2 and datetime.time(10, 30) <= current_time.time() <= datetime.time(11, 15):
                return f"Зараз третій урок: Фізика (Вона вже йде - {datetime.datetime.combine(datetime.date.today(), datetime.datetime.now().time()).replace(microsecond=0) - datetime.datetime.combine(datetime.date.today(), datetime.time(10, 30)).replace(microsecond=0)})"
            elif current_week == 2 and datetime.time(11, 35) <= current_time.time() <= datetime.time(12, 20):
                return f"Зараз четвертий урок: Німецька мова або Інформатика (Вона вже йде - {datetime.datetime.combine(datetime.date.today(), datetime.datetime.now().time()).replace(microsecond=0) - datetime.datetime.combine(datetime.date.today(), datetime.time(11, 35)).replace(microsecond=0)})"
            elif current_week == 2 and datetime.time(12, 30) <= current_time.time() <= datetime.time(13, 15):
                return f"Зараз п'ятий урок: Німецька мова або Інформатика (Вона вже йде - {datetime.datetime.combine(datetime.date.today(), datetime.datetime.now().time()).replace(microsecond=0) - datetime.datetime.combine(datetime.date.today(), datetime.time(12, 30)).replace(microsecond=0)})"
            elif current_week == 2 and datetime.time(13, 25) <= current_time.time() <= datetime.time(14, 10):
                return f"Зараз шостий урок: Інформатика або Німецька мова (Вона вже йде - {datetime.datetime.combine(datetime.date.today(), datetime.datetime.now().time()).replace(microsecond=0) - datetime.datetime.combine(datetime.date.today(), datetime.time(13, 25)).replace(microsecond=0)})"
            elif current_week == 2 and datetime.time(14, 20) <= current_time.time() <= datetime.time(15, 5):
                return f"Зараз сьомий урок: Інформатика або Німецька мова (Вона вже йде - {datetime.datetime.combine(datetime.date.today(), datetime.datetime.now().time()).replace(microsecond=0) - datetime.datetime.combine(datetime.date.today(), datetime.time(14, 20)).replace(microsecond=0)})"

            elif current_week == 3 and datetime.time(8, 30) <= current_time.time() <= datetime.time(9, 15):
                return f"Зараз перший урок: Геометрія (Вона вже йде - {datetime.datetime.combine(datetime.date.today(), datetime.datetime.now().time()).replace(microsecond=0) - datetime.datetime.combine(datetime.date.today(), datetime.time(8, 30)).replace(microsecond=0)})"
            elif current_week == 3 and datetime.time(9, 25) <= current_time.time() <= datetime.time(10, 10):
                return f"Зараз другий урок: Геометрія (Вона вже йде - {datetime.datetime.combine(datetime.date.today(), datetime.datetime.now().time()).replace(microsecond=0) - datetime.datetime.combine(datetime.date.today(), datetime.time(9, 25)).replace(microsecond=0)})"
            elif current_week == 3 and datetime.time(10, 30) <= current_time.time() <= datetime.time(11, 15):
                return f"Зараз третій урок: Англійська мова або Українська мова (Вона вже йде - {datetime.datetime.combine(datetime.date.today(), datetime.datetime.now().time()).replace(microsecond=0) - datetime.datetime.combine(datetime.date.today(), datetime.time(10, 30)).replace(microsecond=0)})"
            elif current_week == 3 and datetime.time(11, 35) <= current_time.time() <= datetime.time(12, 20):
                return f"Зараз четвертий урок: Англійська мова або Українська мова (Вона вже йде - {datetime.datetime.combine(datetime.date.today(), datetime.datetime.now().time()).replace(microsecond=0) - datetime.datetime.combine(datetime.date.today(), datetime.time(11, 35)).replace(microsecond=0)})"
            elif current_week == 3 and datetime.time(12, 30) <= current_time.time() <= datetime.time(13, 15):
                return f"Зараз п'ятий урок: Українська мова або Англійська мова (Вона вже йде - {datetime.datetime.combine(datetime.date.today(), datetime.datetime.now().time()).replace(microsecond=0) - datetime.datetime.combine(datetime.date.today(), datetime.time(12, 30)).replace(microsecond=0)})"
            elif current_week == 3 and datetime.time(13, 25) <= current_time.time() <= datetime.time(14, 10):
                return f"Зараз шостий урок: Українська мова або Англійська мова (Вона вже йде - {datetime.datetime.combine(datetime.date.today(), datetime.datetime.now().time()).replace(microsecond=0) - datetime.datetime.combine(datetime.date.today(), datetime.time(13, 25)).replace(microsecond=0)})"
            elif current_week == 3 and datetime.time(14, 20) <= current_time.time() <= datetime.time(15, 5):
                return f"Зараз сьомий урок: Історія України (Вона вже йде - {datetime.datetime.combine(datetime.date.today(), datetime.datetime.now().time()).replace(microsecond=0) - datetime.datetime.combine(datetime.date.today(), datetime.time(14, 20)).replace(microsecond=0)})"

            elif current_week == 4 and datetime.time(8, 30) <= current_time.time() <= datetime.time(9, 15):
                return f"Зараз перший урок: Алгебра (Вона вже йде - {datetime.datetime.combine(datetime.date.today(), datetime.datetime.now().time()).replace(microsecond=0) - datetime.datetime.combine(datetime.date.today(), datetime.time(8, 30)).replace(microsecond=0)})"
            elif current_week == 4 and datetime.time(9, 25) <= current_time.time() <= datetime.time(10, 10):
                return f"Зараз другий урок: Фізика (Вона вже йде - {datetime.datetime.combine(datetime.date.today(), datetime.datetime.now().time()).replace(microsecond=0) - datetime.datetime.combine(datetime.date.today(), datetime.time(9, 25)).replace(microsecond=0)})"
            elif current_week == 4 and datetime.time(10, 30) <= current_time.time() <= datetime.time(11, 15):
                return f"Зараз третій урок: Зарубіжна література (Вона вже йде - {datetime.datetime.combine(datetime.date.today(), datetime.datetime.now().time()).replace(microsecond=0) - datetime.datetime.combine(datetime.date.today(), datetime.time(10, 30)).replace(microsecond=0)})"
            elif current_week == 4 and datetime.time(11, 35) <= current_time.time() <= datetime.time(12, 20):
                return f"Зараз четвертий урок: Зарубіжна література (Вона вже йде - {datetime.datetime.combine(datetime.date.today(), datetime.datetime.now().time()).replace(microsecond=0) - datetime.datetime.combine(datetime.date.today(), datetime.time(11, 35)).replace(microsecond=0)})"
            elif current_week == 4 and datetime.time(12, 30) <= current_time.time() <= datetime.time(13, 15):
                return f"Зараз п'ятий урок: Мистецтво (Вона вже йде - {datetime.datetime.combine(datetime.date.today(), datetime.datetime.now().time()).replace(microsecond=0) - datetime.datetime.combine(datetime.date.today(), datetime.time(12, 30)).replace(microsecond=0)})"
            elif current_week == 4 and datetime.time(13, 25) <= current_time.time() <= datetime.time(14, 10):
                return f"Зараз шостий урок: Всесвітня історія (Вона вже йде - {datetime.datetime.combine(datetime.date.today(), datetime.datetime.now().time()).replace(microsecond=0) - datetime.datetime.combine(datetime.date.today(), datetime.time(13, 25)).replace(microsecond=0)})"
            elif current_week == 4 and datetime.time(14, 20) <= current_time.time() <= datetime.time(15, 5):
                return f"Зараз сьомий урок: Правознавство (Вона вже йде - {datetime.datetime.combine(datetime.date.today(), datetime.datetime.now().time()).replace(microsecond=0) - datetime.datetime.combine(datetime.date.today(), datetime.time(14, 20)).replace(microsecond=0)})"
            else:
                return "Помилка 404"
        else:
            return "Неправильно вказана область/місто"
    else:
        return None


eel.start('index.html', host="0.0.0.0", port=80, mode=None, shutdown_delay=float('inf'))
