import unittest
import max1
class check_max1(unittest.TestCase):
    def test_tc1(self):
        a=[1,1,1,0,0,1,0,1,1,0]
        status=max1.maxi1(a)
        self.assertEqual(status,3)
    def test_tc2(self):
        a=[1,1,1,0,1,1,1,1,1,0,0,1,1,0,0]
        status=max1.maxi1(a)
        self.assertEqual(status,5)
if __name__=="__main__":
    unittest.main()