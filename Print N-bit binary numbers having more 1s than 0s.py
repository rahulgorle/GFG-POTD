class Solution:

	def NBitBinary(self, n):
        binary_numbers = []

        def generate(number, length, zero_count):
            # Base case
            if length == n:
                binary_numbers.append(number)
                return
            # Recursive case
            generate(number + "1", length + 1, zero_count)
            if zero_count * 2 < length:
                generate(number + "0", length + 1, zero_count+1)

        generate("", 0, 0)
        return binary_numbers
