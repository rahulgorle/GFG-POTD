class Solution:
     def max_of_subarrays(self, k, arr):
        n = len(arr)
        list2 = []
        current_max = max(arr[:k])
        list2.append(current_max)
        for i in range(1, n - k + 1):
            if arr[i - 1] == current_max:
                current_max = max(arr[i : i + k])
            else:
                current_max = max(current_max, arr[i + k - 1])
            list2.append(current_max)
        return list2
