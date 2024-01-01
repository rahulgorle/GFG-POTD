class Solution:
    def canPair(self, nums, k):
        n = len(nums)
        if n % 2:
            return 0

        arr = [0] * (k + 1)
        for num in nums:
            arr[num % k] += 1

        if arr[0] % 2:
            return 0

        if k % 2 == 0 and arr[k // 2] % 2:
            return 0

        for i in range(1, k // 2 + 1):
            if arr[i] != arr[k - i]:
                return 0

        return 1
