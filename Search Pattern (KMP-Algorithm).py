#User function Template for python3

class Solution:
    def search(self, pattern, text):
        occurrences = []  # List to store starting positions of pattern occurrences
        m, n = len(pattern), len(text)
        lps = self.calculate_lps(pattern)

        i, j = 0, 0  # Pointers for text and pattern
        while i < n:
            if pattern[j] == text[i]:
                i += 1
                j += 1

            if j == m:
                occurrences.append(i - j + 1)
                j = lps[j - 1]
            elif i < n and pattern[j] != text[i]:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1

        return occurrences


    def calculate_lps(self, pattern):
        m = len(pattern)
        lps = [0] * m
        length, i = 0, 1

        while i < m:
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1

        return lps
