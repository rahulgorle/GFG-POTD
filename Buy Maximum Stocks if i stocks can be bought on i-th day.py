from typing import List

class Solution:
    def buyMaximumProducts(self, total_items: int, budget: int, prices: List[int]) -> int:
        items_with_prices = sorted(enumerate(prices, start=1), key=lambda item: item[1])
        current_position, purchased_stock = 0, 0

        while current_position < total_items:
            item_index, item_price = items_with_prices[current_position]
            total_cost = item_index * item_price

            if total_cost <= budget:
                budget -= total_cost
                purchased_stock += item_index
                current_position += 1
            else:
                purchased_stock += budget // item_price
                break

        return purchased_stock
