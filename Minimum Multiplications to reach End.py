from typing import List, Tuple
from collections import deque

class Solution:
    def minimumMultiplications(self, arr: List[int], start: int, end: int) -> int:
        if start == end:
            return 0
        
        visited = set()
        queue = deque([(start, 0)])  # Queue stores (current_value, steps)
        
        while queue:
            current, steps = queue.popleft()
            
            for num in arr:
                new_value = (current * num) % 100000
                
                if new_value not in visited:
                    visited.add(new_value)
                    queue.append((new_value, steps + 1))
                    
                    if new_value == end:
                        return steps + 1
        
        return -1
