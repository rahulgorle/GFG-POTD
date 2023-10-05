class Solution:
    def substrCount(self, s, k):
        def atMostKDistinct(s, k):
            left, count, result = 0, 0, 0
            freq = [0] * 26

            for right in range(len(s)):
                if freq[ord(s[right]) - ord('a')] == 0:
                    count += 1
                freq[ord(s[right]) - ord('a')] += 1

                while count > k:
                    if freq[ord(s[left]) - ord('a')] == 1:
                        count -= 1
                    freq[ord(s[left]) - ord('a')] -= 1
                    left += 1

                result += right - left + 1

            return result

        return atMostKDistinct(s, k) - atMostKDistinct(s, k - 1)
