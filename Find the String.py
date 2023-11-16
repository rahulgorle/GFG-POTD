class Solution:
    def __init__(self):
        self.result = None

    def generate_strings(self, length, base):
        """
        Generates all possible strings of given length using the characters from 0 to base-1.
        """
        def dfs(n, k, current_string, result_set):
            """
            Depth-first search to generate all possible strings of length n.
            """
            if n == 0:
                result_set.add(current_string)
                return result_set

            for i in range(k):
                result_set = dfs(n - 1, k, current_string + str(i), result_set)

            return result_set

        ans_set = set()
        ans_set = dfs(length, base, '', ans_set)
        return ans_set

    def build_graph(self, strings, base):
        """
        Builds a graph where two strings are connected if they have a common suffix and differ only in the last character.
        """
        adjacency_dict = {}

        for s in strings:
            for j in range(base):
                neighbor = s[1:] + str(j)
                if neighbor in strings and neighbor != s:
                    if s in adjacency_dict:
                        adjacency_dict[s].append(neighbor)
                    else:
                        adjacency_dict[s] = [neighbor]

        return adjacency_dict

    def findString(self, N, K):
        """
        Finds the lexicographically smallest string such that each string of length N with characters from 0 to K-1
        is a suffix of the constructed string.
        """
        all_strings = self.generate_strings(N, K)
        graph = self.build_graph(all_strings, K)
        visited = set()

        def dfs(current_node, current_path):
            """
            Recursive function to find the lexicographically smallest string.
            """
            visited.add(current_node)

            if len(visited) == (K ** N):
                self.result = current_path
                return True

            for neighbor in graph[current_node]:
                if neighbor not in visited and dfs(neighbor, current_path + neighbor[-1]):
                    return True

            visited.remove(current_node)
            return False

        for start_node in all_strings:
            if dfs(start_node, start_node):
                return self.result

        return self.result
