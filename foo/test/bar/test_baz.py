import unittest

from foo.bar.baz import plus


class TestBaz(unittest.TestCase):
    def test_plus(self):
        a, b = 2, 2
        self.assertEqual(plus(a, b), 4)


if __name__ == '__main__':
    unittest.main()
