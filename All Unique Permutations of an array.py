class Solution:
    def uniquePerms(self, elements, length):
        def generate_permutations(curr, remaining_length, curr_pos):
            if remaining_length == 0:
                result.add(tuple(curr[:]))
                return

            for i in range(curr_pos, len(curr)):
                curr[curr_pos], curr[i] = curr[i], curr[curr_pos]
                generate_permutations(curr, remaining_length - 1, curr_pos + 1)
                curr[curr_pos], curr[i] = curr[i], curr[curr_pos]

        elements.sort()
        result = set()
        generate_permutations(elements, length, 0)
        return sorted(list(result))
