class Solution:
	def topK(self, nums, k):
    		# Create a dictionary to store the frequency count of each unique element
        freq_count = {}
        for num in nums:
            freq_count[num] = freq_count.get(num, 0) + 1
    
        # Sort the unique elements based on frequency counts and element values
        sorted_nums = sorted(freq_count.keys(), key=lambda x: (-freq_count[x], -x))
    
        # Return the top k elements
        return sorted_nums[:k]
