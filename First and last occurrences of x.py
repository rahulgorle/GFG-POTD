class Solution:
    def find(self, arr, n, x):
        def find_first_occurrence(arr, n, x):
            left, right = 0, n - 1
            first_occurrence = -1

            while left <= right:
                mid = left + (right - left) // 2

                if arr[mid] == x:
                    first_occurrence = mid
                    right = mid - 1
                elif arr[mid] < x:
                    left = mid + 1
                else:
                    right = mid - 1

            return first_occurrence

        def find_last_occurrence(arr, n, x):
            left, right = 0, n - 1
            last_occurrence = -1

            while left <= right:
                mid = left + (right - left) // 2

                if arr[mid] == x:
                    last_occurrence = mid
                    left = mid + 1
                elif arr[mid] < x:
                    left = mid + 1
                else:
                    right = mid - 1

            return last_occurrence

        first_index = find_first_occurrence(arr, n, x)
        last_index = find_last_occurrence(arr, n, x)

        return [first_index, last_index]
