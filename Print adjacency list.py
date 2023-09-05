from typing import List

class Solution:
    def printGraph(self, V: int, edges: List[List[int]]) -> List[List[int]]:
        # Initialize an empty adjacency list with V empty lists.
        adjacency_list = [[] for _ in range(V)]

        # Populate the adjacency list based on the provided edges.
        for edge in edges:
            u, v = edge
            adjacency_list[u].append(v)
            adjacency_list[v].append(u)  # Since it's an undirected graph.

        # Sort the neighbors for each node for consistency.
        for i in range(V):
            adjacency_list[i].sort()

        return adjacency_list

# Driver Code
class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self):
        arr=[int(i) for i in input().strip().split()]  # array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()

class IntMatrix:
    def __init__(self) -> None:
        pass
    def Input(self,n,m):
        matrix=[]
        # matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix
    def Print(self,arr):
        for i in arr:
            for j in i:
                print(j,end=" ")
            print()
