class Solution:

	

	def findMaxSum(self,arr, n):

		# code here

		res=0

		pre=0

		cur=0

		for i in range(n):

		    cur=pre+arr[i]

		    pre=res

		    res=max(cur,res)

		return res
