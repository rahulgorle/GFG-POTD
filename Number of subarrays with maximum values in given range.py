class Solution:
    def countSubarrays(self, array, length, lower_limit, upper_limit):
        def count_subarrays_with_limit(array, length, limit):
            start_index = 0
            subarray_count = 0

            for i in range(length):
                if array[i] > limit:
                    start_index = i + 1
                subarray_count += i - start_index + 1

            return subarray_count

        # Count subarrays with elements less than or equal to the upper limit
        count_upper_limit = count_subarrays_with_limit(array, length, upper_limit)

        # Count subarrays with elements less than or equal to the lower limit - 1 to get the final result
        count_lower_limit_minus_one = count_subarrays_with_limit(array, length, lower_limit - 1)

        return count_upper_limit - count_lower_limit_minus_one
