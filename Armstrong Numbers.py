class Solution:
    def armstrongNumber (self, n):
        return "Yes" if n == ((n % 10) ** 3) + (((n // 10) % 10) ** 3) + ((n // 100) ** 3) else 'No'
