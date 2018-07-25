# Intro to Python testing
# Testing Taxonomies: https://wiki.python.org/moin/PythonTestingToolsTaxonomy

# Python unittest reference https://docs.python.org/3/library/unittest.html

import unittest

from day1 import moo

# moo(2)

class TestMoo(unittest.TestCase):

  def test0(self):
    self.assertEqual(moo(0), '')
  def test1(self):
    self.assertEqual(moo(1), 'moo')
  def test2(self):
    self.assertEqual(moo(2), 'moomoo')
  def test3(self):
    self.assertEqual(moo(3), 'moomoomoo')

unittest.main()
