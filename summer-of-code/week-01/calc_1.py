import datetime

# calculator
# Write a program that tells you the following:
# -Hours in a year. How many hours are in a year?
# -Minutes in a decade. How many minutes are in a decade?
# -Your age in seconds. How many seconds old are you? (I'm not going to check your answer, so be as accurate—or not—as you want.)
# -Andreea Visanoiu​: I'm 48618000 seconds old hahaha. Calculate @Andreea Visanoiu's age.
# -Calculate your age accurately based on your birthday (maybe use time of day e.g. 8:23am if you know it, use 12:00 noon midday) - you will need Python modules.


# Print solution
def print_solution(num, date_format_1, date_format_2):
    print("There are " + str(num) + " " + date_format_1 + " per " + date_format_2 + ".")


# Hours in a year
def hours_per_year():
        return 24 * 365


# Minutes in a decade
def minutes_per_decade():
    return (hours_per_year() * 60) * 10


# Your age in seconds
def age_in_seconds(age):
    print("You are " + str(((((int(age) * 365) * 24) * 60) * 60)) + " seconds old.")


# Andreea Visanoiu​: 48618000 seconds old. Calculate @Andreea Visanoiu's age.
def year_from_sec(second):
    print(str(((((int(second) / 60) / 60) / 24) / 365)))


def age_from_sec(second):
    years = second // (60 * 60 * 24 * 364) 
    second -= years * (60 * 60 * 24 * 364)
    months = second // (30 * 24 * 60 * 60)
    second -= months * (30 * 24 * 60 * 60)
    days = second // (24 * 60 * 60)
    print("You are " + str(years) + " years " + str(months) + " months " + str(days) + " days old.")


# Calculate your age accurately based on your birthday
def accurate_age(b_year, b_month, b_day):
    actual_year = 2018
    actual_month = 7
    actual_day = 18
    actual_year_to_sec = (actual_year - 1900) * 364 * 24 * 60 * 60
    actual_month_to_sec = (actual_month - 1) * 30 * 24 * 60 * 60
    actual_day_to_sec = (actual_day - 1) * 24 * 60 * 60

    birtday_year_to_sec = (b_year - 1900) * 364 * 24 * 60 * 60
    birtday_month_to_sec = (b_month - 1) * 30 * 24 * 60 * 60
    birthday_day_to_sec = (b_day - 1) * 24 * 60 * 60

    actual_date_after_1900_in_sec = actual_year_to_sec + actual_month_to_sec + actual_day_to_sec
    bday_date_after_1900_in_sec = birtday_year_to_sec + birtday_month_to_sec + birthday_day_to_sec

    actual_age_in_sec = actual_date_after_1900_in_sec - bday_date_after_1900_in_sec

    age_from_sec(actual_age_in_sec)

print_solution(hours_per_year(), "hours", "year")

print_solution(minutes_per_decade(), "minutes", "decade")

age_in_seconds(30)

year_from_sec(48618000)

accurate_age(1988, 7, 19)

print(1+2)
print(3)
print(10 % 2)
print(11 % 2)