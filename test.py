import unittest
from RateCards import rateCardA, rateCardB


class TestSum(unittest.TestCase):
    def testRateCardA(self):
        result = rateCardA()
        testResultData = {'Cabinet': 1000, 'verge': 50, 'road': 100, 'Chamber': 200, 'Pot': 100}
        self.assertEqual(result, testResultData)

    def testRateCardB(self):
        result = rateCardB()
        testResultData = {'Cabinet': 1200, 'verge': 40, 'road': 80, 'Chamber': 200, 'Pot': 20}
        self.assertEqual(result, testResultData)


if __name__ == '__main__':
    unittest.main()
