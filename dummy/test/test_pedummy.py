import unittest
from app.pedummy import PEDUMMY

class TestPEDummy(unittest.TestCase):
    def setUp(self):
        self.p = PE24()

    def test_24(self):
        p = self.p
        self.fail('Write the dang test!')


if __name__ == '__main__':
    unittest.main()
