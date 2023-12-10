class Solution:
    # Function to check whether there is a subarray present with 0-sum or not.
    def subArrayExists(self, arr, n):
        # Your code here
        # Return true or false
        
        # Create an empty set to store running sums
        sum_set = set()
        
        # Initialize the running sum to 0
        curr_sum = 0
        
        # Traverse the array
        for num in arr:
            # Add the current element to the running sum
            curr_sum += num
            
            # Check if the current sum is zero or if it is already in the set
            if curr_sum == 0 or curr_sum in sum_set:
                return True
            
            # Add the current sum to the set
            sum_set.add(curr_sum)
        
        # If no subarray with a sum of zero is found, return False
        return False
