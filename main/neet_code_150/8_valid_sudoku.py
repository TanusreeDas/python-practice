'''
You are given a a 9 x 9 Sudoku board board. A Sudoku board is valid if the following rules are followed:
Each row must contain the digits 1-9 without duplicates.
Each column must contain the digits 1-9 without duplicates.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without duplicates.
Return true if the Sudoku board is valid, otherwise return false
Note: A board does not need to be full or be solvable to be valid.
Constraints:
board.length == 9
board[i].length == 9
board[i][j] is a digit 1-9 or '.'.

Best Approach: We can reduce the space complexity using bitmask, will try that later.
'''

class Solution:
    @staticmethod
    def is_valid_sudoku_brute_force(board: list[list[str]]) -> bool:
        #logic fow rows
        for row in range(9):
            seen = set()
            for i in range(9):
                if board[row][i] == '.':
                    continue
                if board[row][i] in seen:
                    return False
                seen.add(board[row][i])
        #logic fow cols
        for col in range(9):
            seen = set()
            for j in range(9):
                if board[j][col] == '.':
                    continue
                if board[j][col] in seen:
                    return False
                seen.add(board[j][col])
        #logic fow square
        for square in range(9):
            seen = set()
            for k in range(3):
                for l in range(3):
                    row = (square//3) * 3 + k
                    col = (square % 3) * 3 + l
                    if board[row][col] == '.':
                        continue
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])

        return True

if __name__ == "__main__":
    sol = Solution()
    board = [["1","2",".",".","3",".",".",".","."],
             ["4",".",".","5",".",".",".",".","."],
             [".","9","8",".",".",".",".",".","3"],
             ["5",".",".",".","6",".",".",".","4"],
             [".",".",".","8",".","3",".",".","5"],
             ["7",".",".",".","2",".",".",".","6"],
             [".",".",".",".",".",".","2",".","."],
             [".",".",".","4","1","9",".",".","8"],
             [".",".",".",".","8",".",".","7","9"]]

    print(f"Input board is {board}")
    print(f"Given Sudoku is valid: {sol.is_valid_sudoku_brute_force(board)}")