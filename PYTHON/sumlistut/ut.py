import unittest
import longlist
class check_sum(unittest.TestCase):
    def test_pair1(self):
        a,val=['1','2','4','5','6'],9
        status=longlist.llist(a,val)
        self.assertEqual(status,3)
    def test_pair2(self):
        a,val=['1','2','3','4','5','6'],15
        status=longlist.llist(a,val)
        self.assertEqual(status,5)
if __name__=="__main__":
    unittest.main()