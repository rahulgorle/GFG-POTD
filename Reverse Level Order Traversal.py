from collections import deque

def reverseLevelOrder(root):
    que = deque()
    visited = []
    que.append(root)
    while que:
        current = que.popleft()
        visited.append(current.data)
        if current.right:
            que.append(current.right)
        if current.left:
            que.append(current.left)
    return visited[::-1]
