class Solution:
    def subArraySum(self,arr, tar):
        cumulative_sum = 0
        sum_counts = {0: 1}  
        count = 0
        for num in arr:
            cumulative_sum += num
            if (cumulative_sum - tar) in sum_counts:
                count += sum_counts[cumulative_sum - tar]
            if cumulative_sum in sum_counts:
                sum_counts[cumulative_sum] += 1
            else:
                sum_counts[cumulative_sum] = 1
                
        return count
