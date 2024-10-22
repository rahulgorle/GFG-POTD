from collections import Counter
class Solution:
    def sameOccurrence(self, arr, x, y):
        cnt = Counter({0: 1})
        s, ans = 0, 0
        for e in arr:
            if e == x:
                s += 1
            elif e == y:
                s -= 1
            ans += cnt[s]
            cnt[s] += 1
        return ans
