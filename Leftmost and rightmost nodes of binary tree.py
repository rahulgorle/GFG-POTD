import sys
from collections import defaultdict

sys.setrecursionlimit(10**6)

def traverse(root, level, nodes_per_level):
    if root is None:
        return
    nodes_per_level[level].append(root.data)
    traverse(root.left, level+1, nodes_per_level)
    traverse(root.right, level+1, nodes_per_level)

def printCorner(root):
    nodes_per_level = defaultdict(lambda: [])
    traverse(root, 1, nodes_per_level)
    
    for depth,nodes in nodes_per_level.items():
        if len(nodes)==1:
            print(nodes[0], end=' ')
        else:
            print(nodes[0], nodes[-1], sep=' ', end=' ')
