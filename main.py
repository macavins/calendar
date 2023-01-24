import calendar

print(calendar.weekheader(3))
print()

# print(calendar.firstweekday())
print()

print(calendar.month(2023, 1, 4))

print(calendar.monthcalendar(2023, 3))
print()
print()

print(calendar.calendar(2023))

day_of_the_week = calendar.weekday(2023, 2, 11)
print(day_of_the_week)

is_leap = calendar.isleap(2023)
print(is_leap)

is_leap1 = calendar.isleap(2024)
print(is_leap1)

how_many_leap_days = calendar.leapdays(2000, 2024)
print(how_many_leap_days)

