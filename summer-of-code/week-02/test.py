import unittest
from week2_day1 import calculator
from week2_day1 import full_name
from week2_day1 import secret_formula
from week2_day1 import break_words
from week2_day1 import sort_words
from week2_day1 import count_letters_dict
from week2_day1 import count_letters

#Day 1
class test_calc(unittest.TestCase):
	"""docstring for test_calc"""
	def test0(self):
		self.assertEqual(calculator(2,5,'*'), 10)
	def test1(self):
		self.assertEqual(calculator(5,3,'-'),2)
class test_full_name(unittest.TestCase):	
	"""docstring for test_full_name"selff """
	def test0(self):
		self.assertEqual(full_name("Tatsiana", "Odebunmi"),"Tatsiana Odebunmi")
class test_secret_formula(unittest.TestCase):

	"""docstring for test_secret_formula"unittest.TestCasef """
	def test0(self):
		self.assertEqual(secret_formula(1000), (500000, 500, 5))
		
class test_break_words(unittest.TestCase):
	"""docstring for test_break_words"""
	def test0(self):
		self.assertEqual(break_words("1 million women to tech"),
			(["1","million","women", "to", "tech"]))
class test_sort_words(unittest.TestCase):
	"""docstring for test_sort_words"""
	def test0(self):
		self.assertEqual(sort_words(["1", "million", "women", "to", "tech"]),
			(["1", "million","tech", "to", "women"]))

#day3	
class test_alice_dict(unittest.TestCase):
	"""docstring for test_alice_dict"""		
	
	def test0(self):
		dict_let={'A': 9804,'B': 1746,  'C': 3003, 'D': 5469, 'E': 15396,
		 'F': 2383, 'G': 2944, 'H': 7890, 'I': 8634, 'J': 235, 'K': 1290,
		 'L': 5211, 'M': 2466, 'N': 8053, 'O': 9480, 'P': 1968, 'Q': 220,
		 'R': 6612, 'S': 7269, 'T': 12204, 'U': 3979, 'V': 963,
		 'W': 2952, 'X': 176, 'Y': 2584,'Z': 80}
		self.assertDictEqual(count_letters_dict("alice_in_wonderland.txt"),(dict_let))

class test_alice_list(unittest.TestCase):
	def test0(self):
		list_let=[['A', 9804], ['B', 1746], ['C', 3003], ['D', 5469], ['E', 15396],
		['F', 2383], ['G', 2944], ['H', 7890], ['I', 8634], ['J', 235], ['K', 1290],
		['L', 5211], ['M', 2466], ['N', 8053], ['O', 9480], ['P', 1968], ['Q', 220],
		['R', 6612], ['S', 7269], ['T', 12204], ['U', 3979], ['V', 963], ['W', 2952],
		['X', 176], ['Y', 2584], ['Z', 80]]	
		self.assertEqual(count_letters("alice_in_wonderland.txt"),(list_let))
unittest.main()
		