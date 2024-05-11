class Solution:
    def jugglerSequence(self, n):
     sequence = [n]
     while n != 1:
        if n % 2 == 0:
            n = int(n ** 0.5)
        else:
            n = int(n ** 1.5)
        sequence.append(n)
     return sequence
