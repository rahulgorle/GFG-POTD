class Solution:
    def wildCard(self,pattern, string):
        
        from functools import lru_cache
        
        m, n = len(pattern), len(string)
        
        @lru_cache(None)
        def match(i, j):
            nonlocal m, n
            if i == m and j == n:
                return True
            if i == m and j < n:
                return False
            if j == n:
                if pattern[i] == '*':
                    return match(i+1, j)
                return False
            if pattern[i] == '*':
                return match(i+1, j) or match(i, j+1)
            if pattern[i] == '?' or pattern[i] == string[j]:
                return match(i+1, j+1)
            return False
        return match(0, 0)
