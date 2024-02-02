class Solution:
    def atoi(self,s):
        try:
            temp = int(s)
        except ValueError:
            return -1
        return temp
