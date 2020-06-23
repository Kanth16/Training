import unittest
import phoneno
class check_phno(unittest.TestCase):
    def test_phno(self):
        a="abc99ef67d8992"
        status=phoneno.phno(a)
        self.assertEqual(status,"99678992df")
    def test_phno1(self):
        a="as9867dfgf5432ed1"
        status=phoneno.phno(a)
        self.assertEqual(status,"986754321d")
if __name__=="__main__":
    unittest.main()