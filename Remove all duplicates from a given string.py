class Solution:
	def removeDuplicates(self,str):
	    # code here
	    l1 = ""
	    for i in str:
	        if i not in l1:
	            l1 += i
	        else:
	            continue
	    return l1
