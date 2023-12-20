class Solution:
    def findWinner(self, n, A):
        # Calculate the XOR of all elements in the array
        xor_value = 0
        for num in A:
            xor_value ^= num

        # If the XOR is already 0, player 1 wins
        if xor_value == 0:
            return 1
        else:
            # If the number of elements is even, player 1 wins
            # If the number of elements is odd, player 2 wins
            return 1 if n % 2 == 0 else 2
