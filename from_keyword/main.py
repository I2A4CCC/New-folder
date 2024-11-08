# create import date time and bday_message.py

import datetime

# finding todays date
today = datetime.date.today()
# creating your next bday
next_bd = datetime.date(2025, 1, 2)
# creating a variable that finds the diffrence
time_dif = next_bd - today

if today == next_bd:
    print(random_message) # type: ignore
else:
    print(f'My next birthday is {time_dif} days away!')


