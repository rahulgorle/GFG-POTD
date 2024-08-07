class Solution:
    def kthElement(self, k, arr1, arr2):
        return sorted(arr1 + arr2)[k - 1]
