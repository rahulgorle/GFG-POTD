from collections import Counter
class Solution:
    def oddEven(self, s : str) -> str:
        count = Counter(s)
        ans = 0
        
        for key in count:
            if count[key] & 1 == ord(key) & 1: ans += 1
        
        return "ODD" if ans & 1 else "EVEN"
