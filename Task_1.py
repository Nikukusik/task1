import datetime as dt
from datetime import datetime as dtdt
import random
import re
#1--------------------------------------------------
def get_days_from_today(date):
    try:
        date = dtdt.strptime(date, "%Y-%d-%m")
        date_today = dtdt.today()
        return (date_today - date).days
    except Exception:
        print("Invalid date")                     

#print(get_days_from_today("2021-11-10"))
#2--------------------------------------------------
def get_numbers_ticket(min, max, quantity):
    number_ticket = []
    if min < 1 or max > 999 or not min <= quantity <= max:
        return number_ticket
    else:
        for i in range(quantity):
            a = random.randint(min,max)
            if a not in number_ticket:
                number_ticket.append(a)
            else:
                i -= 1
                continue
        while(len(number_ticket) < quantity):
            a = random.randint(min,max)
            if a not in number_ticket:
                number_ticket.append(a)
        return number_ticket

#print(get_numbers_ticket(1, 49, 6))
#3--------------------------------------------------
'''
raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-2222",
    "38050 111 22 11   ",
]
'''

def normalize_phone(phone_number):
    p1 = r"[\+\d]+"
    phone_number = ''.join(re.findall(p1, phone_number))
    if len(phone_number) == 10:
        phone_number = '+38' + phone_number
    elif len(phone_number) == 12:
        phone_number = '+' + phone_number
    return phone_number

'''
result = []
for phone in raw_numbers:
    result.append(normalize_phone(phone))
print(result)
'''
#4--------------------------------------------------
'''
users = [
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "Jane Smitt", "birthday": "1980.01.29"}
]
'''

def get_upcoming_birthdays(users=None):
    tdate = dtdt.today().date()
    birthdays = []
    for user in users:
        bdate = user["birthday"]
        bdate = dtdt.strptime(bdate, "%Y.%m.%d").date()
        year_now = dtdt.today().year
        bdate = bdate.replace(year = year_now)
        week_day = bdate.isoweekday()
        days_between = (bdate - tdate).days
        if 0<=days_between < 7:
            if week_day < 6:
                birthdays.append({"name": user["name"], 'congratulation_date': bdate.strftime("%Y.%m.%d")})
            else:
                if (bdate+dt.timedelta(days=1)).weekday()==0:
                    birthdays.append({'name':user['name'], 'congratulation_date':(bdate+dt.timedelta(days=1)).strftime("%Y.%m.%d")})
                elif (bdate+dt.timedelta(days=2)).weekday()==0: 
                    birthdays.append({'name':user['name'], 'congratulation_date':(bdate+dt.timedelta(days=2)).strftime("%Y.%m.%d")})
    return birthdays

#print(get_upcoming_birthdays(users))
