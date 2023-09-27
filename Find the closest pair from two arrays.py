class Solution:
    def printClosest(self, arr, brr, n, m, x):
        # Initialize variables to store the closest sum and the pair.
        closest_sum = float('inf')
        result_pair = [0, 0]

        # Initialize two pointers, one for each array.
        i = 0  # Pointer for arr
        j = m - 1  # Pointer for brr

        while i < n and j >= 0:
            current_sum = arr[i] + brr[j]

            # Check if the current pair has a sum closer to x.
            if abs(current_sum - x) < abs(closest_sum - x):
                closest_sum = current_sum
                result_pair[0] = arr[i]
                result_pair[1] = brr[j]

            # If the current sum is less than x, move the pointer in arr to the right.
            if current_sum < x:
                i += 1
            # If the current sum is greater than or equal to x, move the pointer in brr to the left.
            else:
                j -= 1

        return result_pair
