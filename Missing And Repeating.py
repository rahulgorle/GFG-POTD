class Solution:
    def findTwoElement( self,arr): 
        n = len(arr)
        S = n * (n + 1) // 2
        S_sq = n * (n + 1) * (2 * n + 1) // 6
        actual_sum = sum(arr)
        actual_sum_sq = sum(x * x for x in arr)


        diff_sum = actual_sum - S
        diff_sum_sq = actual_sum_sq - S_sq


        sum_y_x = diff_sum_sq // diff_sum
        y = (diff_sum + sum_y_x) // 2
        x = sum_y_x - y
        
        return (y, x)
