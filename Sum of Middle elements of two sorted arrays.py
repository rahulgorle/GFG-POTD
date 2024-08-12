import bisect

class Solution:
    def sum_of_middle_elements(self, arr1, arr2):

        for i in arr2:
            bisect.insort(arr1, i)
            
        leng = len(arr1)
        return arr1[leng // 2] + arr1[leng // 2 - 1]
