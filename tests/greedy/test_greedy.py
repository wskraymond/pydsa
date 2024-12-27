import unittest
from py_dsa.greedy import hand_of_straights, merge_triplets_to_form_target_triplet
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
    
    def test_triplets_to_form_target(self):
        s = merge_triplets_to_form_target_triplet.Solution()
        self.assertEqual(True, s.mergeTriplets([[2,5,3],[1,8,4],[1,7,5]], [2,7,5]))
        self.assertEqual(False, s.mergeTriplets([[3,4,5],[4,5,6]], [3,2,5]))
        self.assertEqual(True, s.mergeTriplets([[2,5,3],[2,3,4],[1,2,5],[5,2,3]], [5,5,5]))
    
    def test_triplets_to_form_target_2(self):
        s = merge_triplets_to_form_target_triplet.Solution_bitset()
        self.assertEqual(True, s.mergeTriplets([[2,5,3],[1,8,4],[1,7,5]], [2,7,5]))
        self.assertEqual(False, s.mergeTriplets([[3,4,5],[4,5,6]], [3,2,5]))
        self.assertEqual(True, s.mergeTriplets([[2,5,3],[2,3,4],[1,2,5],[5,2,3]], [5,5,5]))

if __name__ == '__main__':
    unittest.main()