# This is example of Python program.
# this module do logic for calculator

import sqlite3
import datetime


def get_statistic_data():
    all_data = []
    with sqlite3.connect('db/database.db') as db:
        db.row_factory = sqlite3.Row
        cursor = db.cursor()
        query = """SELECT * FROM payments JOIN expenses
                    ON expenses.id=payments.expense_id """
        cursor.execute(query)
        all_data = cursor
    return all_data


def get_most_common_item():
    data = get_statistic_data()
    quantity = {}
    for payments in data:
        # print(payments, type(payments))
        # print(quantity)
        # print(payments["expense_id"])
        if payments["expense_id"] in quantity:
            quantity[payments["expense_id"]]["qty"] += 1
        else:
            quantity[payments["expense_id"]] = {'qty': 1, 'name': payments['name']}
    return max(quantity.values(), key=lambda x: x['qty'])['name']


def get_most_exp_item():
    data = get_statistic_data()
    return max(list(data), key=lambda x: x["amount"])['name']


def get_timestamp(y, m, d):
    return int(datetime.datetime.timestamp(datetime.datetime(y, m, d)))


def get_date(tmstmp):
    return datetime.datetime.fromtimestamp(tmstmp).date()


def get_most_exp_day():
    data = get_statistic_data()
    week_days = ("Понедельник", "Вторник", "Среда", "Четверг",
                 "Пятница", "Суботта", "Воскресенье")
    days = {}

    for payments in data:
        if get_date(payments["payments_date"]).weekday() in days:
            days[get_date(payments["payments_date"]).weekday()] += payments["amount"]
        else:
            days[get_date(payments["payments_date"]).weekday()] = payments["amount"]
    return week_days[max(days, key=days.get)]


def get_most_exp_month():
    data = get_statistic_data()

    month_list = ("0", "Январь", "Февраль", "Март", "Апрель", "Май", "Июнь",
                  "Июль", "Август", "Сентябрь", "Окрябрь", "Ноябрь", "Декабрь")

    days = {}
    for payments in data:
        if get_date(payments['payments_date']).month in days:
            days[get_date(payments['payments_date']).month] += payments["amount"]
        else:
            days[get_date(payments["payments_date"]).month] = payments["amount"]
    return month_list[max(days, key=days.get)]
