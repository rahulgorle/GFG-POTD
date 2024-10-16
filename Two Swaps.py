class Solution:
    def checkSorted(self, arr):
        new_arr = sorted(arr)
        if new_arr == arr:
            return True
        count = 0
        i = 0
        while i < len(arr) - 1:
            correct_index = arr[i] - 1
            if correct_index > len(arr)-1:
                return False 
            if arr[i] != i + 1:
                arr[i], arr[correct_index] = arr[correct_index], arr[i]
                count += 1
                if count == 2:
                    break 
            else:
                i += 1
        if count == 2:
            if arr == new_arr:
                return True 
        return False
