class Solution:
    def DivisibleByEight(self,s):
        num = int(s[-3:])
        return 1 if num % 8 == 0 else -1
