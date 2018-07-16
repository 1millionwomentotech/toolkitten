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

minutes = "minutes"
hours = "hours"
year = "year"
decade = "decade"

print_solution(hours_per_year(), hours, year)

print_solution(minutes_per_decade(), minutes, decade)

print(1+2)
print(3)
print(10 % 2)
print(11 % 2)
