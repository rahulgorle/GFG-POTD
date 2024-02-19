import heapq
class Solution:
    def minValue(self, s, k):
        # Count the frequency of each character in the string
        char_freq = {}
        for char in s:
            char_freq[char] = char_freq.get(char, 0) + 1
       
        # Convert frequencies to negative values for min heap
        neg_freq = [-char_freq[char] for char in char_freq]
       
        # Increase k smallest frequencies by 1
        for _ in range(k):
            heapq.heapify(neg_freq)
            neg_freq[0] += 1
       
        # Calculate and return the result
        res = 0
        for freq in neg_freq:
            res += (freq * freq)
       
        return res
