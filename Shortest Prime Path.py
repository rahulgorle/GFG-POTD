#User function Template for python3
from collections import deque

class Solution:
    def sieve_of_eratosthenes(self, limit):
        is_prime = [True] * (limit + 1)
        is_prime[0] = is_prime[1] = False
        for num in range(2, int(limit**0.5) + 1):
            if is_prime[num]:
                for multiple in range(num*num, limit + 1, num):
                    is_prime[multiple] = False
        return is_prime

    def find_shortest_path(self, start, end, is_prime):
        queue = deque()
        queue.append([start, 0])
        visited = {start}

        while queue:
            current_number, level = queue.popleft()

            if current_number == end:
                return level

            for digit_index in range(4):
                for new_digit in range(10):
                    if not digit_index and not new_digit:
                        continue

                    new_number = current_number[:digit_index] + str(new_digit) + current_number[digit_index+1:]

                    if new_number not in visited and is_prime[int(new_number)]:
                        visited.add(new_number)
                        queue.append([new_number, level + 1])

        return -1

    def solve(self, num1, num2):
        prime_limit = 10000
        is_prime = self.sieve_of_eratosthenes(prime_limit)
        num1_str, num2_str = str(num1), str(num2)
        result = self.find_shortest_path(num1_str, num2_str, is_prime)
        return result

