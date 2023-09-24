class Solution:
    def duplicates(self, arr, n): 
    	# code here
        # Initialize a list to store the result
        result = []
        
        # Traverse the input array and use it as a frequency counter
        for i in range(n):
            index = arr[i] % n  # Map the value to a valid index
            arr[index] += n     # Increment the count at the mapped index
        
        # Traverse the array again to find elements occurring more than once
        for i in range(n):
            if arr[i] // n > 1:
                result.append(i)
        
        # Sort the result list in ascending order
        result.sort()
        
        if not result:
            result = [-1]
        
        return result
