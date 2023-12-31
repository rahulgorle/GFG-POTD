from typing import List

class Solution:
    def solve(self,dp,ind,coins,summ):
        if ind==len(coins):
            if summ==0:
                return False
            if  summ==2024 or summ%20==0 or summ%24==0:
                return True
            else:
                return False
        if dp[ind][summ]!=None:
            return dp[ind][summ]
        
        dp[ind][summ]=self.solve(dp,ind+1,coins,summ+coins[ind]) or self.solve(dp,ind+1,coins,summ)
        return dp[ind][summ]
    def isPossible(self, N : int, coins : List[int]) -> bool:
        # code here
        dp=[[None]*2025]*367
        return self.solve(dp,0,coins,0)
