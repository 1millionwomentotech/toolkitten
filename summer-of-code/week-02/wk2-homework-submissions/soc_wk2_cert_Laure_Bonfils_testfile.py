import unittest
from soc_wk2_cert_Laure_Bonfils import continent_counter, world 

# # WARNING: print(world) and print(continent_counter) need to be commented in the soc_wk2_cert_Laure_Bonfils file to be able to run this test file.

# M = "land"
# o = "water"
# world = [[o,o,o,o,o,o,o,o,o,o,o],[o,o,o,o,M,M,o,o,o,o,o],[o,o,o,o,o,o,o,o,M,M,M],[o,o,o,M,o,o,o,o,o,M,o],[o,o,o,M,o,M,M,o,o,o,o],[o,o,o,o,M,M,M,M,o,o,o],[o,o,o,M,M,M,M,M,M,M,M],[o,o,o,M,M,o,M,M,M,o,o],[o,o,o,o,o,o,M,M,o,o,o],[o,M,o,o,o,M,o,o,o,o,o],[o,o,o,o,o,o,o,o,o,o,o]]

class TestDay2(unittest.TestCase):
    def test0(self):
        self.assertEqual(continent_counter(world, 5, 5),24)
        
unittest.main()

# continent_counter(world,5,5)
# print(world)

