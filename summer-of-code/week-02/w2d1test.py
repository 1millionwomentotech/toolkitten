import unittest

from w2d1 import moo

# moo(5)
# moo(3)
# 

class TestMoo(unittest.TestCase):

	def test0(self):
		self.assertEqual(moo(0),'')
	def test1(self):
		self.assertEqual(moo(1),'moo')
	def test2(self):
		self.assertEqual(moo(2),'moomoo')

unittest.main()