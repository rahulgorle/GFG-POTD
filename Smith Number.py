class Solution:
    def smithNum(self, n):
        s1 = self.calculateSum(n)
        s2 = 0
        i = 2
        count = 0
        while n != 1:
            if n % i == 0 and i <= 9:
                s2 += i
                n = n // i
                count += 1
            elif n % i == 0 and i > 9:
                s2 += self.calculateSum(i)
                n = n // i
                count += 1
            else:
                i += 1

        if s1 == s2 and count > 1:
            return 1
        return 0

    def calculateSum(self, num):
        total_sum = 0
        while num != 0:
            total_sum += num % 10
            num = num // 10
        return total_sum
