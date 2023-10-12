import unittest

def check(happy):
    return happy <=5

class Happy(unittest.TestCase):

    def test(self):
        self.assertTrue(check(10))

if __name__=='__main__':

    unittest.main()