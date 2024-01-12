from collections import deque

class Solution:
    def modifyQueue(self, queue, k):
        temp_queue = deque(queue[:k][::-1])
        del queue[:k]
        queue[:0] = temp_queue
        return queue
