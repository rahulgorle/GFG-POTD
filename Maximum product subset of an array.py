class Solution:
    def findMaxProduct(self, arr):
        MOD = 10**9 + 7

        if len(arr) == 1:
            return arr[0]

        max_neg = float('-inf')
        product = 1
        count_neg = 0
        count_zero = 0
        non_zero_count = 0
        
        for num in arr:
            if num == 0:
                count_zero += 1
            else:
                non_zero_count += 1
                if num < 0:
                    count_neg += 1
                    max_neg = max(max_neg, num)
                product = (product * num) % MOD

        # If the array has only zeros
        if non_zero_count == 0:
            return 0

        # If the count of negatives is odd, remove the largest negative number
        if count_neg % 2 != 0:
            if non_zero_count == 1 and count_zero > 0:
                return 0
            product = (product * pow(max_neg, MOD-2, MOD)) % MOD
        
        return product
