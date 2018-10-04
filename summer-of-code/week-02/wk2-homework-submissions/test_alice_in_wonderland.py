import unittest

from alice_in_wonderland import alice_letter_counter

class TestAlice(unittest.TestCase):

	def test0(self):
		expected = [['a: 9805'], ['b: 1746'], ['c: 3004'], ['d: 5470'], ['e: 15398'], ['f: 2382'], ['g: 2944'], ['h: 7890'], ['i: 8636'], ['j: 235'], ['k: 1290'], ['l: 5211'], ['m: 2467'], ['n: 8053'], ['o: 9478'], ['p: 1968'], ['q: 220'], ['r: 6612'], ['s: 7270'], ['t: 12202'], ['u: 3978'], ['v: 963'], ['w: 2952'], ['x: 176'], ['y: 2584'], ['z: 80']]
		self.assertEqual(alice_letter_counter(), expected) 

unittest.main()