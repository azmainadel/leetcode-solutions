# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        while True:
            row = rand7()
            column = rand7()
            
            index = column + (row - 1) * 7
            
            if index <= 40:
                return 1 + (index - 1) % 10
        