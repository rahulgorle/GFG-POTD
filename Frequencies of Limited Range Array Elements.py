class Solution:
    # Function to count the frequency of all elements from 1 to N in the array.
    def frequencyCount(self, arr, N, P):
        freq = [0] * N

        for i in range(N):
            if arr[i] <= N:
                freq[arr[i] - 1] += 1

        for i in range(N):
            arr[i] = freq[i]
