class Solution:
    def palindromicPartition(self, string):
        n = len(string)
        # Initialize a table to store whether substrings are palindromes
        is_palindrome = [[False] * n for _ in range(n)]

        # Initialize a table to store the minimum cuts needed
        min_cuts = [0] * n

        for i in range(n):
            min_cuts[i] = i  # Maximum possible cuts
            for j in range(i, -1, -1):
                if string[j] == string[i] and (i - j < 2 or is_palindrome[j + 1][i - 1]):
                    is_palindrome[j][i] = True
                    if j == 0:
                        min_cuts[i] = 0
                    else:
                        min_cuts[i] = min(min_cuts[i], min_cuts[j - 1] + 1)

        return min_cuts[n - 1]
