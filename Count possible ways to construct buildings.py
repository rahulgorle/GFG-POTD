class Solution:
	def TotalWays(self, N):
        a = 1
        b = 1
        mod = 10 ** 9 + 7
        for i in range(N):
            c = a + b
            a = b
            b = c % (mod)
        return (b**2) % mod
