class Solution:
    def romanToInt(self, input):
        charValue = {"I": 1, "V": 5, "X": 10,
                     "L": 50, "C": 100, "D": 500, "M": 1000}
        if(len(input)==1):
            return charValue[input]

        if charValue[input[0]] >= charValue[input[1]]:
            return charValue[input[0]] + self.romanToInt(input[1:len(input)])
        else :
            return - charValue[input[0]] + self.romanToInt(input[1:len(input)])