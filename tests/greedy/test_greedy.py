import unittest
from py_dsa.greedy import hand_of_straights
class TestGreedy(unittest.TestCase):
    def test_hand_of_straights(self):
        s = hand_of_straights.Solution_counter()
        self.assertEqual(True, s.isNStraightHand([1,2,3,6,2,3,4,7,8], 3))
        self.assertEqual(False, s.isNStraightHand([1,2,3,4,5], 4))
        self.assertEqual(False, s.isNStraightHand([8,10,12], 3))
        self.assertEqual(True, s.isNStraightHand([1,2,3,4,5], 1))
        self.assertEqual(True, s.isNStraightHand([1], 1))
    
    def test_hand_of_straights_2(self):
        s = hand_of_straights.Solution_map()
        self.assertEqual(True, s.isNStraightHand([1,2,3,6,2,3,4,7,8], 3))
        self.assertEqual(False, s.isNStraightHand([1,2,3,4,5], 4))
        self.assertEqual(False, s.isNStraightHand([8,10,12], 3))
        self.assertEqual(True, s.isNStraightHand([1,2,3,4,5], 1))
        self.assertEqual(True, s.isNStraightHand([1], 1))

if __name__ == '__main__':
    unittest.main()