class Solution:
   
    def countOccurence(self, numbers, n, k):
        # Dictionary to store the count of occurrences for each element
        element_counts = {}
       
        # Count occurrences of each element in the input list
        for number in numbers:
            element_counts[number] = element_counts.get(number, 0) + 1
       
        # Count elements that appear more than n/k times
        count_above_threshold = 0
        threshold = n // k
        for element, count in element_counts.items():
            if count > threshold:
                count_above_threshold += 1
       
        return count_above_threshold
