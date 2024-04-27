import datetime


def get_time_lesson(hour: int, minute: int) -> datetime.timedelta:
    return datetime.datetime.combine(datetime.date.today(), datetime.datetime.now().time()).replace(microsecond=0) - datetime.datetime.combine(datetime.date.today(), datetime.time(hour=hour, minute=minute)).replace(microsecond=0)


def lesson() -> str:
    current_time = datetime.datetime.now()
    current_week = current_time.weekday()
    current_month = current_time.month
    current_day = current_time.day
    if datetime.time(8, 30) > current_time.time():
        return "Уроки поки що не почалися"
    elif datetime.time(15, 5) < current_time.time():
        return "Уроки закінчилися, йди додому"
    elif current_week in [5, 6]:
        return "Відпочивай зараз вихідний день!"
    elif current_month in [6, 7, 8] or current_month == 5 and current_day == 31:
        return f"Зараз літні канікули!!!"
    elif datetime.time(9, 15) <= current_time.time() <= datetime.time(9, 25):
        return f"Зараз перша маленька перерва (Вона вже йде - {get_time_lesson(hour=9, minute=15)})"
    elif datetime.time(10, 10) <= current_time.time() <= datetime.time(10, 30):
        return f"Зараз перша велика перерва (Вона вже йде - {get_time_lesson(hour=10, minute=10)})"
    elif datetime.time(11, 15) <= current_time.time() <= datetime.time(11, 35):
        return f"Зараз друга велика перерва (Вона вже йде - {get_time_lesson(hour=11, minute=15)})"
    elif datetime.time(12, 20) <= current_time.time() <= datetime.time(12, 30):
        return f"Зараз друга маленька перерва (Вона вже йде - {get_time_lesson(hour=12, minute=20)})"
    elif datetime.time(13, 15) <= current_time.time() <= datetime.time(13, 25):
        return f"Зараз третя маленька перерва (Вона вже йде - {get_time_lesson(hour=13, minute=15)})"
    elif datetime.time(14, 10) <= current_time.time() <= datetime.time(14, 20):
        return f"Зараз четверта маленька перерва (Вона вже йде - {get_time_lesson(hour=14, minute=10)})"

    elif current_week == 0 and datetime.time(8, 30) <= current_time.time() <= datetime.time(9, 15):
        return f"Зараз перший урок: Українська мова/Англійська мова (Вона вже йде - {get_time_lesson(hour=8, minute=30)})"
    elif current_week == 0 and datetime.time(9, 25) <= current_time.time() <= datetime.time(10, 10):
        return f"Зараз другий урок: Українська мова/Англійська мова (Вона вже йде - {get_time_lesson(hour=9, minute=25)})"
    elif current_week == 0 and datetime.time(10, 30) <= current_time.time() <= datetime.time(11, 15):
        return f"Зараз третій урок: Англійська мова/Українська мова (Вона вже йде - {get_time_lesson(hour=10, minute=30)})"
    elif current_week == 0 and datetime.time(11, 35) <= current_time.time() <= datetime.time(12, 20):
        return f"Зараз четвертий урок: Англійська мова/Українська мова (Вона вже йде - {get_time_lesson(hour=11, minute=35)})"
    elif current_week == 0 and datetime.time(12, 30) <= current_time.time() <= datetime.time(13, 15):
        return f"Зараз п'ятий урок: Хімія (Вона вже йде - {get_time_lesson(hour=12, minute=30)})"
    elif current_week == 0 and datetime.time(13, 25) <= current_time.time() <= datetime.time(14, 10):
        return f"Зараз шостий урок: Хімія (Вона вже йде - {get_time_lesson(hour=13, minute=25)})"
    elif current_week == 0 and datetime.time(14, 20) <= current_time.time() <= datetime.time(15, 5):
        return f"Зараз сьомий урок: Фізичка культура (Вона вже йде - {get_time_lesson(hour=14, minute=20)})"

    elif current_week == 1 and datetime.time(8, 30) <= current_time.time() <= datetime.time(9, 15):
        return f"Зараз перший урок: Українська література (Вона вже йде - {get_time_lesson(hour=8, minute=30)})"
    elif current_week == 1 and datetime.time(9, 25) <= current_time.time() <= datetime.time(10, 10):
        return f"Зараз другий урок: Українська література (Вона вже йде - {get_time_lesson(hour=9, minute=25)})"
    elif current_week == 1 and datetime.time(10, 30) <= current_time.time() <= datetime.time(11, 15):
        return f"Зараз третій урок: Фізика (Вона вже йде - {get_time_lesson(hour=10, minute=30)})"
    elif current_week == 1 and datetime.time(11, 35) <= current_time.time() <= datetime.time(12, 20):
        return f"Зараз четвертий урок: Біологія (Вона вже йде - {get_time_lesson(hour=11, minute=35)})"
    elif current_week == 1 and datetime.time(12, 30) <= current_time.time() <= datetime.time(13, 15):
        return f"Зараз п'ятий урок: Біологія (Вона вже йде - {get_time_lesson(hour=12, minute=30)})"
    elif current_week == 1 and datetime.time(13, 25) <= current_time.time() <= datetime.time(14, 10):
        return f"Зараз шостий урок: Фізична культура (Вона вже йде - {get_time_lesson(hour=13, minute=25)})"
    elif current_week == 1 and datetime.time(14, 20) <= current_time.time() <= datetime.time(15, 5):
        return f"Зараз сьомий урок: Географія (Вона вже йде - {get_time_lesson(hour=14, minute=20)})"

    elif current_week == 2 and datetime.time(8, 30) <= current_time.time() <= datetime.time(9, 15):
        return f"Зараз перший урок: Алгебра (Вона вже йде - {get_time_lesson(hour=8, minute=30)})"
    elif current_week == 2 and datetime.time(9, 25) <= current_time.time() <= datetime.time(10, 10):
        return f"Зараз другий урок: Алгебра (Вона вже йде - {get_time_lesson(hour=9, minute=25)})"
    elif current_week == 2 and datetime.time(10, 30) <= current_time.time() <= datetime.time(11, 15):
        return f"Зараз третій урок: Фізика (Вона вже йде - {get_time_lesson(hour=10, minute=30)})"
    elif current_week == 2 and datetime.time(11, 35) <= current_time.time() <= datetime.time(12, 20):
        return f"Зараз четвертий урок: Німецька мова/Інформатика (Вона вже йде - {get_time_lesson(hour=11, minute=35)})"
    elif current_week == 2 and datetime.time(12, 30) <= current_time.time() <= datetime.time(13, 15):
        return f"Зараз п'ятий урок: Німецька мова/Інформатика (Вона вже йде - {get_time_lesson(hour=12, minute=30)})"
    elif current_week == 2 and datetime.time(13, 25) <= current_time.time() <= datetime.time(14, 10):
        return f"Зараз шостий урок: Інформатика/Німецька мова (Вона вже йде - {get_time_lesson(hour=13, minute=25)})"
    elif current_week == 2 and datetime.time(14, 20) <= current_time.time() <= datetime.time(15, 5):
        return f"Зараз сьомий урок: Інформатика/Німецька мова (Вона вже йде - {get_time_lesson(hour=14, minute=20)})"

    elif current_week == 3 and datetime.time(8, 30) <= current_time.time() <= datetime.time(9, 15):
        return f"Зараз перший урок: Геометрія (Вона вже йде - {get_time_lesson(hour=8, minute=30)})"
    elif current_week == 3 and datetime.time(9, 25) <= current_time.time() <= datetime.time(10, 10):
        return f"Зараз другий урок: Геометрія (Вона вже йде - {get_time_lesson(hour=9, minute=25)})"
    elif current_week == 3 and datetime.time(10, 30) <= current_time.time() <= datetime.time(11, 15):
        return f"Зараз третій урок: Англійська мова/Українська мова (Вона вже йде - {get_time_lesson(hour=10, minute=30)})"
    elif current_week == 3 and datetime.time(11, 35) <= current_time.time() <= datetime.time(12, 20):
        return f"Зараз четвертий урок: Англійська мова/Українська мова (Вона вже йде - {get_time_lesson(hour=11, minute=35)})"
    elif current_week == 3 and datetime.time(12, 30) <= current_time.time() <= datetime.time(13, 15):
        return f"Зараз п'ятий урок: Українська мова/Англійська мова (Вона вже йде - {get_time_lesson(hour=12, minute=30)})"
    elif current_week == 3 and datetime.time(13, 25) <= current_time.time() <= datetime.time(14, 10):
        return f"Зараз шостий урок: Українська мова/Англійська мова (Вона вже йде - {get_time_lesson(hour=13, minute=25)})"
    elif current_week == 3 and datetime.time(14, 20) <= current_time.time() <= datetime.time(15, 5):
        return f"Зараз сьомий урок: Історія України (Вона вже йде - {get_time_lesson(hour=14, minute=20)})"

    elif current_week == 4 and datetime.time(8, 30) <= current_time.time() <= datetime.time(9, 15):
        return f"Зараз перший урок: Алгебра (Вона вже йде - {get_time_lesson(hour=8, minute=30)})"
    elif current_week == 4 and datetime.time(9, 25) <= current_time.time() <= datetime.time(10, 10):
        return f"Зараз другий урок: Фізика (Вона вже йде - {get_time_lesson(hour=9, minute=25)})"
    elif current_week == 4 and datetime.time(10, 30) <= current_time.time() <= datetime.time(11, 15):
        return f"Зараз третій урок: Зарубіжна література (Вона вже йде - {get_time_lesson(hour=10, minute=30)})"
    elif current_week == 4 and datetime.time(11, 35) <= current_time.time() <= datetime.time(12, 20):
        return f"Зараз четвертий урок: Зарубіжна література (Вона вже йде - {get_time_lesson(hour=11, minute=35)})"
    elif current_week == 4 and datetime.time(12, 30) <= current_time.time() <= datetime.time(13, 15):
        return f"Зараз п'ятий урок: Мистецтво (Вона вже йде - {get_time_lesson(hour=12, minute=30)})"
    elif current_week == 4 and datetime.time(13, 25) <= current_time.time() <= datetime.time(14, 10):
        return f"Зараз шостий урок: Всесвітня історія (Вона вже йде - {get_time_lesson(hour=13, minute=25)})"
    elif current_week == 4 and datetime.time(14, 20) <= current_time.time() <= datetime.time(15, 5):
        return f"Зараз сьомий урок: Правознавство (Вона вже йде - {get_time_lesson(hour=14, minute=20)})"
    else:
        return "404"
