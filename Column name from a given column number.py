class Solution:
    def colName(self, n):
        result = ''
        while n > 0:
            # Decrement n to account for 1-based indexing
            n -= 1
            # Find the remainder when divided by 26
            remainder = n % 26
            # Convert remainder to a letter and prepend it to the result
            result = chr(ord('A') + remainder) + result
            # Update n to the quotient when divided by 26
            n //= 26
        return result
