class Solution:
    def romanToDecimal(self, S):
        roman_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        decimal = 0
        prev_value = 0

        for char in S[::-1]:
            current_value = roman_dict[char]
            if current_value < prev_value:
                decimal -= current_value
            else:
                decimal += current_value
            prev_value = current_value

        return decimal
