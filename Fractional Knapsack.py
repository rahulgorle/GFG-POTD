#User function Template for python3

class Item:
    def __init__(self, val, w):
        self.value = val
        self.weight = w

class Solution:
    def fractionalknapsack(self, capacity, items, num_items):
        sorted_items = sorted(items, key=lambda x: x.value / x.weight, reverse=True)
        total_value = 0

        for item in sorted_items:
            take = min(capacity, item.weight)
            total_value += (take * item.value / item.weight)
            capacity -= take

            if capacity == 0:
                break

        return total_value


