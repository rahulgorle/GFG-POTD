class Solution:
    def getMinDiff(self, arr, n, k):
        arr.sort()
        overall_difference = arr[n - 1] - arr[0]

        for i in range(1, n):
            if arr[i] - k < 0:
                continue

            current_min = min(arr[0] + k, arr[i] - k)
            current_max = max(arr[i - 1] + k, arr[n - 1] - k)
            overall_difference = min(overall_difference, current_max - current_min)

        final_result = overall_difference
        return final_result
