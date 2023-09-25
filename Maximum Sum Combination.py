import heapq

class Solution:
    def maxCombinations(self, N, K, A, B):
        # Sort the arrays A and B in non-decreasing order.
        A.sort()
        B.sort()

        # Create a max heap to store the sum combinations.
        max_heap = []

        # Initialize the heap with the largest sum combination.
        heapq.heappush(max_heap, (-(A[N - 1] + B[N - 1]), N - 1, N - 1))

        # Create a set to keep track of visited indices.
        visited = set()
        visited.add((N - 1, N - 1))

        # Initialize the result list.
        result = []

        while K > 0:
            # Pop the maximum sum combination from the heap.
            current_sum, i, j = heapq.heappop(max_heap)
            result.append(-current_sum)
            K -= 1

            # Generate and push the next potential sum combinations.
            if i > 0 and (i - 1, j) not in visited:
                visited.add((i - 1, j))
                heapq.heappush(max_heap, (-(A[i - 1] + B[j]), i - 1, j))
            if j > 0 and (i, j - 1) not in visited:
                visited.add((i, j - 1))
                heapq.heappush(max_heap, (-(A[i] + B[j - 1]), i, j - 1))

        return result
