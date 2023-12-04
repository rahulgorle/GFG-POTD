class Solution:
    def isSumString(self, S):
        n = len(S)

        for i in range(1, n):
            for j in range(i + 1, n):
                num1 = int(S[:i])
                num2 = int(S[i:j])

                if self.check_sum_string(S[j:], num1, num2):
                    return 1

        return 0

    def check_sum_string(self, s, num1, num2):
        if not s:
            return True

        num_sum = num1 + num2
        sum_str = str(num_sum)

        if s.startswith(sum_str):
            return self.check_sum_string(s[len(sum_str):], num2, num_sum)
        else:
            return False
