# test_soc_wk1_cert_Daniella_DSouza.py
import unittest
from soc_wk1_cert_Daniella_DSouza import TimeMachine

class TestTimeMachine(unittest.TestCase):
	"""Tests for class TimeMachine"""
	def test_calc_hours_in_a_leap_year(self):
		machine = TimeMachine()
		hours = machine.calc_hours_in_a_year(1992)
		self.assertEqual(hours, 8784)
	
	def test_calc_hours_in_a_year(self):
		machine = TimeMachine()
		hours = machine.calc_hours_in_a_year(1900)
		self.assertEqual(hours, 8760)

	def test_calc_minutes_in_a_decade(self):
		""" Calculate minutes for the years 2000 ... 2009 """
		machine = TimeMachine()
		minutes = machine.calc_minutes_in_a_decade(2000)
		self.assertEqual(minutes, 5260320)


		pass

	def test_calc_age_in_seconds(self):

		pass

	def test_days_32bit_timeout(self):


		pass

	def test_days_64bit_timeout(self):

		pass

unittest.main()