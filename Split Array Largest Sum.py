class Solution:
    def splitArray(self, nums, length, segments):
        def count_segments(nums, max_sum):
            current_sum, segment_count = 0, 1

            for num in nums:
                current_sum += num

                if current_sum > max_sum:
                    current_sum = num
                    segment_count += 1

            return segment_count

        left, right = max(nums), sum(nums)

        while left < right:
            mid = left + (right - left) // 2
            segment_count = count_segments(nums, mid)

            if segment_count > segments:
                left = mid + 1
            else:
                right = mid

        return right
