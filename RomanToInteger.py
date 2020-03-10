class Solution:
    def romanToInt(self, input):
        charValue = {"I": 1, "V": 5, "X": 10,
                     "L": 50, "C": 100, "D": 500, "M": 1000}
        sum = 0

        for char in range(len(input)-1):
            if(charValue[input[char]] < charValue[input[char+1]]):
                sum = sum - charValue[input[char]]
            else:
                sum = sum + charValue[input[char]]
        sum = sum + charValue[input[len(input)-1]]

        return sum
