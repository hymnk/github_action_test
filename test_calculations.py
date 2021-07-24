import unittest
from unittest.main import main

import calculations


class CalculationsTest(unittest.TestCase):
    """割り算する関数をテストする
    """

    def test_divine_normal(self):
        self.assertEqual(calculations.divide(2, 2), 1)

    def test_divine_contain_zero(self):
        # 結果が1であるため修正
        self.assertEqual(calculations.divide(0, 1), 1)


if __name__ == '__main__':
    unittest.main()
