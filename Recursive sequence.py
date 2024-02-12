class Solution:
    def sequence(self, n):
        result = 0  # Initialize the result variable to store the sum of the sequence
        current_number = 1  # Initialize the current number in the sequence
        mod = (10**9) + 7  # Modulus value for the result
       
        # Loop through each element in the sequence
        for i in range(n):
            temp_product = 1  # Initialize a temporary variable to store the product of the sequence elements
           
            # Calculate the product of consecutive numbers starting from 1 up to i+1
            for j in range(1, i + 2):
                temp_product *= current_number
                current_number += 1  # Move to the next number for the next iteration
           
            result += temp_product  # Add the product to the result
       
        return result % mod  # Return the result modulo the specified modulus
