from datetime import datetime, timedelta
from collections import defaultdict

"""Програма виводить список колег, яких потрібно привітати з днем народження на тижні """


def main(users: dict):
    users = transform_date(users)
    birthday_list = defaultdict(list)
    for name, birthday in users.items():
        delta = birthday - datetime.now()
        if int(delta.days) in range(0, 6):
            if birthday.strftime("%A") == "Saturday":
                birthday += timedelta(days=2)
            elif birthday.strftime("%A") == "Sunday":
                birthday += timedelta(days=1)
            birthday_list[birthday.strftime("%A")].append(name)
    output_birthday_list(birthday_list)


"""Функція виконує приведення дати народження до дня народження у поточному році """


def transform_date(users: dict) -> dict:
    current_year = (datetime.now()).year
    for name, birthday in users.items():
        users.update({name: birthday.replace(year=current_year)})
    return users


"""Функція виводить на екран список колег, яких треба привітати на тижні"""


def output_birthday_list(birthday_list: dict):
    for day, name in birthday_list.items():
        name = ", ".join(name)
        print(f"{day}: {name}")


"""Функція виконує читання файлу з вихідними даними та приводить отримані дані 
до словника виляду "Ім'я: Дата Народження (формат YYYY-MM-D)" """


def read_birthday_list(source: str) -> dict:
    with open(source, "r") as file:
        users = {}
        for line in file.readlines():
            name, birthday = (line.split())[0], (line.split())[1]
            users.update({name: datetime.strptime(birthday, "%Y-%m-%d")})
        return users


if __name__ == "__main__":
    users = read_birthday_list("list_birthday.txt")
    main(users)
