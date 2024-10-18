from collections import Counter
class Solution:
    def getSingle(self,arr):
        frequencies = Counter(arr)
        for num, freq in frequencies.items():
            if freq % 2 != 0:
                return num
