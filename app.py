import operator
from collections import defaultdict
from datetime import datetime
from flask import Flask, render_template

from conn import DatabaseConnection

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


def get_amount():
    per_contact()
    per_date()


def per_contact():
    with DatabaseConnection('./parser/data.db') as cursor:
        content = cursor.execute(
            "SELECT dealsPrice, contactsName FROM deals INNER JOIN contacts ON deals.contactsId = contacts.contactsId")
        contacts = content.fetchall()

    data = group_data(contacts)
    print(data)


def per_date():
    with DatabaseConnection('./parser/data.db') as cursor:
        content = cursor.execute("SELECT dealsDateCreated,dealsPrice FROM deals")
        deals = content.fetchall()

    date_formated = remove_day(deals)
    data = group_data(date_formated)

    per_sector(data)


def per_sector(deals_per_month):
    with DatabaseConnection('./parser/data.db') as cursor:
        content = cursor.execute(
            "SELECT dealsDateCreated, dealsPrice, sectorKey FROM deals INNER JOIN companies ON deals.companiesId = companies.companiesId")
        deals = content.fetchall()
    with DatabaseConnection('./parser/data.db') as cursor:
        content = cursor.execute("SELECT sectorKey, sector FROM sectors")
        sectors = content.fetchall()

    date_formated = remove_day(deals)
    sums = defaultdict(int)
    for amount, date, sectorKey in date_formated:
        amount_number = int(amount)
        key = f'{date}#{sectorKey}'
        sums[key] += amount_number

    another_list = []
    for sectorKey, sector in sectors:
        for key, value in sums.items():
            date, formated_key = key.split('#')
            if formated_key == sectorKey:
                another_list.append((sector, sectorKey, value, date))

    final = []
    for name, key, value, month in another_list:
        total = int(deals_per_month[month])
        sector_pct = (100 * value / total) / 100
        formated_pct = "{:.2f}".format(sector_pct)
        final.append((int(key), name, formated_pct, month))

    final.sort(key=operator.itemgetter(0))  # index da sectorKey
    final.sort(key=lambda index: datetime.strptime(index[3], '%m/%Y'))

    for element in final:
        pass


def group_data(data):
    sums = defaultdict(int)

    for amount, in_common_element, *other_info in data:
        amount_number = int(amount)
        sums[in_common_element] += amount_number

    return sums


def remove_day(content):
    content_formated = []
    for date, amount, *other_info in content:
        _ = datetime.strptime(date, "%m/%d/%Y")
        new_date = _.strftime("%m/%Y")
        formated = [amount, new_date, *other_info]
        content_formated.append(tuple(formated))
    return content_formated


if __name__ == '__main__':
    app.run()

