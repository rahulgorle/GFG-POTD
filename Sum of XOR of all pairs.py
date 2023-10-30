class Solution:
    def sumXOR(self, arr, n):
        total_xor_sum = 0
        max_bit = 0
        
        # Find the maximum bit position
        for num in arr:
            max_bit = max(max_bit, num.bit_length())
        
        for bit in range(max_bit):
            count0 = 0
            count1 = 0
            
            for num in arr:
                # Count the number of elements with 0 and 1 at the current bit position
                if (num >> bit) & 1:
                    count1 += 1
                else:
                    count0 += 1
            
            # Calculate the XOR sum for the current bit position
            xor_sum = count0 * count1 * (1 << bit)
            total_xor_sum += xor_sum
        
        return total_xor_sum
