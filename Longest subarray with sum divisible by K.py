class Solution:
    def longSubarrWthSumDivByK(self, nums, length, k):
        remainder_index_map, current_remainder_sum, max_length = {0: -1}, 0, 0

        for i in range(length):
            current_remainder_sum = (current_remainder_sum + nums[i]) % k
            max_length = max(max_length, i - remainder_index_map.get(current_remainder_sum, i))

            remainder_index_map.setdefault(current_remainder_sum, i)

        return max_length
