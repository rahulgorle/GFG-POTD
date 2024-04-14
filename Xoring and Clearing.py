class Solution:
    def printArr(self, n, arr):
        # printing array elements with spaces
        for i in arr:
            print(i, end=" ")
        print()
    def setToZero(self, n, arr):
        # setting all elements to zero
        arr[:] = [0] * len(arr)
        
    def xor1ToN(self, n, arr):
        l = []
        # doing xor with indices
        for i in range(len(arr)):
            res = arr[i] ^ i
            l.append(res)
        arr[:] = l
