class Solution:
    
    def grayToBinary(self, n):
        num = str(bin(n))
        ans = num[2]
        prev = num[2]
        for i in range(3, len(num)):
            ans += str(int(num[i]) ^ int(prev))
            prev = ans[-1]
        return int(ans, 2)
