class Solution:
    def shuffleArray(self, arr, n):
        first_half = arr[0:n//2]
        second_half = arr[n//2:n]
        shuffled_result = []

        for i in range(len(first_half)):
            shuffled_result.append(first_half[i])
            shuffled_result.append(second_half[i])

        arr[:] = shuffled_result[:]
        return arr
