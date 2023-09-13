class Solution:
    def findLargest(self, N, S):
        # Handle special cases where it's not possible to form the number
        if (S == 0 and N > 1) or S > 9 * N:
            return -1

        # Initialize an array to store the digits of the largest number
        largest_number = [0] * N

        # Fill the array with the largest possible digits
        for i in range(N):
            if S >= 9:
                largest_number[i] = 9
                S -= 9
            else:
                largest_number[i] = S
                S = 0

        # Convert the array to an integer and return
        return int(''.join(map(str, largest_number)))
