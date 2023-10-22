class Solution:
    def numberOfPaths(self, M, N):
        MOD = 10**9 + 7
        
        # Calculate the binomial coefficient (M-1 + N-1 choose M-1)
        def binomial(n, k):
            res = 1
            for i in range(k):
                res = (res * (n - i)) % MOD
                res = (res * pow(i + 1, MOD - 2, MOD)) % MOD
            return res

        return binomial(M + N - 2, M - 1)
