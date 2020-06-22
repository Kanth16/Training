import unittest
import addut
class checkadd(unittest.TestCase):
    def test_check_add(self):
        a,b=1,5
        status=addut.test_add(a,b)
        self.assertEqual(status,6)
    def test_check_add1(self):
        a,b=3,1
        status=addut.test_add(a,b)
        self.assertEqual(status,4)
if __name__=="__main__":
    unittest.main()