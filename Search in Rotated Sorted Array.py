class Solution:
    def search(self, arr, target):
        right = len(arr) - 1
        left = 0
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                return mid
            if arr[left] <= arr[mid]:
                if arr[left] <= target and target <= arr[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if arr[mid] <= target and arr[right] >= target:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1
