class Solution:
    def solve(self, col, board, n, sol):
        if col == n:
            sol.append(board[:])
        for row in range(1, n + 1):
            if all(board[i] != row and abs(board[i] - row) != col - i for i in range(col)):
                board[col] = row
                self.solve(col + 1, board, n, sol)
    
    def nQueen(self, n):
        sol = []
        self.solve(0, [0] * n, n, sol)
        return sol
