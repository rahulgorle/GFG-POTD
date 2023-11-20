class Solution:
    def sumK(self, root, k):
        def count_paths_with_sum(node, target_sum, current_sum, prefix_sums):
            if not node:
                return 0

            current_sum += node.data
            result = prefix_sums[current_sum - target_sum]

            prefix_sums[current_sum] += 1

            result += (count_paths_with_sum(node.left, target_sum, current_sum, prefix_sums) +
                       count_paths_with_sum(node.right, target_sum, current_sum, prefix_sums))

            prefix_sums[current_sum] -= 1

            return result

        prefix_sums = defaultdict(int)
        prefix_sums[0] = 1  # Initialize with the sum of an empty path

        return count_paths_with_sum(root, k, 0, prefix_sums) % MOD
