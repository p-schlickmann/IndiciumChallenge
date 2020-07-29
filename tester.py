from conn import DatabaseConnection
import itertools


with DatabaseConnection('./parser/data.db') as cursor:
    content = cursor.execute(
        "SELECT dealsPrice, contactsName FROM deals INNER JOIN contacts ON deals.contactsId = contacts.contactsId")
    contacts = content.fetchall()

from collections import defaultdict

sums = defaultdict(int)
for amount, date in contacts:
    amount_number = int(amount)
    sums[date] += amount_number

print(sums.items())
