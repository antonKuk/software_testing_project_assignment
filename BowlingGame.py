class BowlingGame:
    def __init__(self):
        self.rolls = []

    def roll(self, pins):
        """appends values to rolls[] list"""
        self.rolls.append(pins)

    def score(self):
        """
        checks every value in rolls[] list as:
        1.is it a "strike"?
        2.is it a "spare"?
        3.calculates result accordingly
        :return: result (integer)
        """
        result = 0
        roll_index = 0
        for frameIndex in range(10):
            if self.isStrike(roll_index):
                result += self.strikeScore(roll_index)
                roll_index += 1
            elif self.isSpare(roll_index):
                result += self.spareScore(roll_index)
                roll_index += 2
            else:
                result += self.frameScore(roll_index)
                roll_index += 2
        return result

    def isStrike(self, roll_index):
        """
        checks if given rolls[] list index points to a "strike" value
        roll_index: an integer :argument
        boolean value :return
        """
        return self.rolls[roll_index] == 10

    def isSpare(self, roll_index):
        """
        checks if given rolls[] list index points to a part of a "spare" value
        roll_index: an integer :argument
        boolean value :return
        """
        return self.rolls[roll_index] + self.rolls[roll_index + 1] == 10

    def strikeScore(self, roll_index):
        """
        calculates "score" frame result with bonuses
        :param roll_index: int
        :return: result integer
        """
        return 10 + self.rolls[roll_index + 1] + self.rolls[roll_index + 2]

    def spareScore(self, roll_index):
        """
        calculates "spare" frame result with bonuses
        :param roll_index: int
        :return: result integer
        """
        return 10 + self.rolls[roll_index + 2]

    def frameScore(self, roll_index):
        """
        calculates normal frame result
        :param roll_index: int
        :return:
        """
        return self.rolls[roll_index] + self.rolls[roll_index + 1]
