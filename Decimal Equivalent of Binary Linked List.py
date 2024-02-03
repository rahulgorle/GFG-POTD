class Solution:
    def decimalValue(self, head):
        MOD, decimal_value = 10**9 + 7, 0

        while head:
            decimal_value = (decimal_value << 1 | head.data) % MOD
            head = head.next

        return decimal_value
