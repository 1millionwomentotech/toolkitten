"""soc_wk1_cert_Daniella_DSouza.py

Basic Exercises for Certification:

Write a program that tells you the following:

Hours in a year. How many hours are in a year?
Minutes in a decade. How many minutes are in a decade?
Your age in seconds. How many seconds old are you? (I'm not going to check your answer, so be as accurate—or not—as you want.)
Andreea Visanoiu​: I'm 48618000 seconds old hahaha. Calculate @Andreea Visanoiu's age.
Here are some tougher questions:

How many days does it take for a 32-bit system to timeout, if it has a bug with integer overflow?
How about a 64-bit system?
Calculate your age accurately based on your birthday (maybe use time of day e.g. 8:23am if you know it, use 12:00 noon midday) - 
you will need Python modules."""

class TimeMachine():
	"""									"""

	def __init__(self):
		"""		"""
		self.days_in_leap_year = 366
		self.days_in_year = 365


	def leap_year(self, year):
		""" If the year is evenly divisible by 4 but not by 100 it is leap
			If the year is evenly divisible by 4 as well as by 100 and 400 it is a leap year"""

		if (year % 4 == 0):
			if (year % 100 == 0):
				if (year % 400 == 0):
					return True
			else:
				return True

		return False

	def calc_hours_in_a_year(self, year):
		"""									"""
		hours = 0

		# Leap year
		if (self.leap_year(year) == True):
			hours = self.days_in_leap_year * 24
		else:
			hours = self.days_in_year * 24

		return hours

	def calc_minutes_in_a_decade(self, startingyear):
		"""	Minutes in a decade is the sum of the minutes in each year of the decade """
		decade = [startingyear + i for i in range(0,10)]

		print(decade)

		minutes_in_decade = 0

		for j in range(len(decade)):
			minutes_year = self.calc_hours_in_a_year(decade[j]) * 60
			minutes_in_decade += minutes_year

		return minutes_in_decade

	def calc_age_in_seconds(self, age):
		"""									"""
		pass

	def days_32bit_timeout(self):
		"""									"""
		pass

	def days_64bit_timeout(self):
		"""									"""
		pass

	def calc_age(self, birthdate_time):
		"""									"""
		pass


