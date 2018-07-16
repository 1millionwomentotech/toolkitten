# calculator
# Write a program that tells you the following:
# -Hours in a year. How many hours are in a year?
# -Minutes in a decade. How many minutes are in a decade?
# -Your age in seconds. How many seconds old are you? (I'm not going to check your answer, so be as accurate—or not—as you want.)
# -Andreea Visanoiu​: I'm 48618000 seconds old hahaha. Calculate @Andreea Visanoiu's age.


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


print_solution(hours_per_year(), "hours", "year")

print_solution(minutes_per_decade(), "minutes", "decade")

age_in_seconds(30)

year_from_sec(48618000)

print(1+2)
print(3)
print(10 % 2)
print(11 % 2)
