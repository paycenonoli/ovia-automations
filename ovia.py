def is_adult(age):
    if age >= 18:
        print('Your are an adult')
    else:
        print('You are a minor')

is_adult(16)


import datetime

def is_valid_day(day):
    try:
        datetime.datetime.strptime(day, '%A')
        return True
    except ValueError:
        return False

day = "Monday"


print(is_valid_day(day))
