class Solution:
    def kSubstrConcat(self, n, s, k):
        if n % k != 0:
            return 0

        unique_substrings, unique_substring_count = set(), 0

        for i in range(0, n, k):
            current_substring = s[i:i + k]

            if current_substring not in unique_substrings:
                if unique_substring_count == 2:
                    return 0
                else:
                    unique_substring_count += 1

                unique_substrings.add(current_substring)

        return 1
