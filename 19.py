# https://projecteuler.net/problem=19

def get_months(leap_year):
    return [31, 29 if leap_year else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_leap_year(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False


day_of_week = 2  # Jan 1900 was a Monday
sundays = 0

for year in range(1900, 2001):
    months = get_months(is_leap_year(year))
    for month in months:
        for day in range(month):
            if day_of_week < 7:
                day_of_week += 1
            else:
                day_of_week = 1
            if year == 1900:
                continue
            if day_of_week == 1 and day == 0:
                sundays += 1

print(sundays)
