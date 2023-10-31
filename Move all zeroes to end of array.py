class Solution:
    def pushZerosToEnd(self, arr, n):
        non_zero_index = 0  # Initialize a pointer to keep track of non-zero elements
        
        # Traverse the array
        for i in range(n):
            if arr[i] != 0:
                # Swap the non-zero element with the element at non_zero_index
                arr[i], arr[non_zero_index] = arr[non_zero_index], arr[i]
                non_zero_index += 1
