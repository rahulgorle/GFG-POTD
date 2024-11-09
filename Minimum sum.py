class Solution:
    def minSum(self, arr):
        arr.sort(reverse=True)
        n = len(arr)
        while arr[n - 1] == 0:
            n -= 1
        output = []
        carry = 0
        for i in range(1, n, 2):
            carry, r = divmod(arr[i - 1] + arr[i] + carry, 10)
            output.append(str(r))
        if n & 1:
            carry += arr[n - 1]
        if carry:
            output.append(str(carry))
        return "".join(reversed(output))
