class Solution:
    def checkBoxes(self, board, start_row, start_col):
        s = set()
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                curr = board[i][j]
                if curr in s and curr != ".":
                    return False
                else:
                    s.add(curr)
        
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        s = set()
        for i in range(0, 9):
            for j in range(0, 9):
                curr = board[i][j]
                if curr in s and curr != ".":
                    return False
                else:
                    s.add(curr)
            s.clear()

        for i in range(0, 9):
            for j in range(0, 9):
                curr = board[j][i]
                if curr in s and curr != ".":
                    return False
                else:
                    s.add(curr)
            s.clear()

        return (self.checkBoxes(board, 0, 0) and self.checkBoxes(board, 3, 0) and self.checkBoxes(board, 6, 0)
        and self.checkBoxes(board, 0, 3) and self.checkBoxes(board, 3, 3) and self.checkBoxes(board, 6, 3)
        and self.checkBoxes(board, 0, 6) and self.checkBoxes(board, 3, 6) and self.checkBoxes(board, 6, 6))
        