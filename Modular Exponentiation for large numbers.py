class Solution:
	def PowMod(self, x, n, m):
		if(n == 1):
		    return x
		if(n == 0):
		    return 1
		ans = self.PowMod(x, n // 2, m)
		if(n % 2 == 0):
		    return (ans * ans) % m
		elif(n % 2 == 1):
		    return (x * ans * ans) % m
