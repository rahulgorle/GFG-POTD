class Solution:
    def min_sprinklers(self, gallery, n):
        sprinkler_ranges = sorted([(i - g, i + g) for i, g in enumerate(gallery) if g != -1], reverse=True)
        current_position, max_reachable_position, sprinkler_count = 0, 0, 0

        while current_position < n:
            if sprinkler_ranges and sprinkler_ranges[-1][0] <= current_position:
                start, end = sprinkler_ranges.pop()
                max_reachable_position = max(max_reachable_position, end + 1)
            elif max_reachable_position > current_position:
                current_position = max_reachable_position
                sprinkler_count += 1
            else:
                return -1

        return sprinkler_count
