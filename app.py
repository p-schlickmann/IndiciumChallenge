import re
from collections import defaultdict

from conn import DatabaseConnection


def get_amount():
    with DatabaseConnection('./parser/data.db') as cursor:
        content = cursor.execute("SELECT * FROM deals")
        deals = content.fetchall()
    per_contact()
    per_date()


def per_contact():
    with DatabaseConnection('./parser/data.db') as cursor:
        content = cursor.execute(
            "SELECT dealsPrice, contactsName FROM deals INNER JOIN contacts ON deals.contactsId = contacts.contactsId")
        contacts = content.fetchall()

    data = group_data(contacts)


def per_date():
    with DatabaseConnection('./parser/data.db') as cursor:
        content = cursor.execute("SELECT dealsDateCreated,dealsPrice FROM deals")
        deals = content.fetchall()

    date_formated = []
    for date, amount in deals:
        expression = r'([0-9]+)\/[0-9]+(\/[0-9]+)'
        matches = re.search(expression, date)
        new_month = matches.group(1)
        new_year = matches.group(2)
        new_date = new_month + new_year
        date_formated.append((amount, new_date,))

    data = group_data(date_formated)


def group_data(data):
    sums = defaultdict(int)

    for amount, in_common_element in data:
        amount_number = int(amount)
        sums[in_common_element] += amount_number

    return sums


get_amount()
