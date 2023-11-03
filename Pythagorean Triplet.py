class Solution:

    def checkTriplet(self, arr, n):
        # Create a set to store the squares of elements in the array
        square_set = set(x * x for x in arr)

        for i in range(n):
            for j in range(i + 1, n):
                # Check if the sum of the squares of two elements is in the set
                if (arr[i] * arr[i] + arr[j] * arr[j]) in square_set:
                    return True

        return False
