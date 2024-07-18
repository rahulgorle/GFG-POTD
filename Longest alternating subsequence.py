class Solution:
    def alternatingMaxLength(self, arr):
        dec,inc =1,1
        for i in range(1, len(arr)):
            if arr[i] > arr[i - 1]:
                inc = dec + 1
            elif arr[i] < arr[i - 1]:
                dec = inc + 1
        return max(inc, dec)
