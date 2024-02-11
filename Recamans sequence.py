class Solution:
    def recamanSequence(self, n):
        if n < 2:
            return [i for i in range(n)]
       
        visited = {0, 1}
        sequence = [0, 1]
        current = 1

        for i in range(2, n + 1):
            current = current - i if current - i >= 0 and current - i not in visited else current + i
            visited.add(current)
            sequence.append(current)

        return sequence
