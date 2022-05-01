import unittest
import BowlingGame


class TestBowlingGame(unittest.TestCase):

    def setUp(self):
        """sets BowlingGame for testing"""
        self.game = BowlingGame.BowlingGame()

    def testGutterGame(self):
        """tests 'all zeros' score for BowlingGame.py"""
        for i in range(0, 20):
            self.game.roll(0)
        self.assertEqual(self.game.score(), 0)

    def testAllOnes(self):
        """tests 'all ones' score for BowlingGame.py"""
        self.rollMany(1, 20)
        self.assertEqual(20, self.game.score())

    def testOneSpare(self):
        """tests 'one spare' score for BowlingGame.py"""
        self.game.roll(5)
        self.game.roll(5)
        self.game.roll(3)
        self.rollMany(0, 17)
        self.assertEqual(self.game.score(), 16)

    def testOneStrike(self):
        """tests 'one strike, one frame < 10 and rest of zeros' score for BowlingGame.py"""
        self.game.roll(10)
        self.game.roll(4)
        self.game.roll(3)
        self.rollMany(0, 16)
        self.assertEqual(self.game.score(), 24)

    def testPerfectGame(self):
        """tests 'all strikes' score for BowlingGame.py"""
        self.rollMany(10, 12)
        self.assertEqual(self.game.score(), 300)

    def testManySpare(self):
        """tests 'all spares' score for BowlingGame.py"""
        self.rollMany(5, 21)
        self.assertEqual(self.game.score(), 150)

    def rollMany(self, pins, rolls):
        """appends some number(pins) to rolls[] list from BowlingGame.py number of times (rolls)"""
        for i in range(rolls):
            self.game.roll(pins)

