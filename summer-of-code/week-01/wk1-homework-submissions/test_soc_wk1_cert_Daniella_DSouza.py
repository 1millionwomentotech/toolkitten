# test_soc_wk1_cert_Daniella_DSouza.py
import unittest
import time
from soc_wk1_cert_Daniella_DSouza import TimeMachine

class TestTimeMachine(unittest.TestCase):
	"""Tests for class TimeMachine"""

	def setUp(self):
		self.machine = TimeMachine()

	def test_calc_hours_in_a_leap_year(self):
		
		hours = self.machine.calc_hours_in_a_specific_year(1992)

		self.assertEqual(hours, 8784)
	
	def test_calc_hours_in_a_year(self):
		
		hours = self.machine.calc_hours_in_a_specific_year(1900)
		self.assertEqual(hours, 8760)

	def test_calc_minutes_in_a_decade(self):
		""" Calculate minutes for the years 2000 ... 2009 """
		
		minutes = self.machine.calc_minutes_in_a_decade(2000)
		self.assertEqual(minutes, 5258880)



	def test_calc_age_in_seconds(self):
		age = 1
		# To keep things simple. check the number of seconds in 1 year
		# I am ignoring leap year for now
		expected = 31536000

		seconds = self.machine.calc_age_in_seconds(1)
		self.assertEqual(seconds, 31536000)


	def test_days_32bit_timeout(self):

		pass

	def test_days_64bit_timeout(self):

		pass

unittest.main()