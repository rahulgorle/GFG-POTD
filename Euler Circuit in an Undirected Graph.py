class Solution:
	def isEularCircuitExist(self, v, adj):
		return all(len(v_adj) % 2 == 0 for v_adj in adj)
