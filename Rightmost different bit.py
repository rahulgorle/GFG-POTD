class Solution:
    def posOfRightMostDiffBit(self,m,n):
        xor = m^n
        if xor == 0:
            return -1
        position = 1
        while xor:
            if xor & 1:
                return position
            else:
                xor = xor >> 1
                position += 1
