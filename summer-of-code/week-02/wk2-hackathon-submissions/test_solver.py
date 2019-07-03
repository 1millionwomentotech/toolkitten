from unittest import TestCase
import solver

class TestSolver(TestCase):

    def setUp(self):
        self.board = [['l', 'w', 'k', 'x'], ['k', 'c', 'm', 'h'], ['d', 'u', 'x', 't'], ['k', 'o', 't', 'i']]

    def test_decode_word(self):
        word = ((0,0), (0,1), (1, 1), (2,1), (3,2))
        self.assertEqual(solver.decode_word(word, self.board), 'lwcut')
