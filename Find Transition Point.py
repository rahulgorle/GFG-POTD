class Solution:
    def transitionPoint(self, arr, n):
        left, right = 0, n - 1
        transition_point = -1  # Initialize the transition point as -1

        while left <= right:
            mid = left + (right - left) // 2  # Calculate the middle index

            if arr[mid] == 1:
                transition_point = mid  # Update the transition point
                right = mid - 1  # Continue searching on the left side
            else:
                left = mid + 1  # Continue searching on the right side

        return transition_point
