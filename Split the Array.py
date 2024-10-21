class Solution:
    def countgroup(self, arr): 
        MOD = 10 ** 9 + 7
        tot_xor = 0
        for i in arr:
            tot_xor ^= i
        if tot_xor != 0:
            return 0
        n = len(arr)
        res = (pow(2, n - 1, MOD) - 1) % MOD
        
        return res
