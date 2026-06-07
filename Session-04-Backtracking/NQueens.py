class Solution:

    def arrange_board(self, chess):
        new_board = []
        for row in chess:
            new_board.append("".join(row))
        return new_board

    def placeQueen(self, row, cols, diag, a_diag, chess, n, possible_ans):

        if row == n:
            possible_ans.append(self.arrange_board(chess))
            return

        for col in range(n):

            if col in cols or (row - col) in diag or (row + col) in a_diag:
                continue
            
            chess[row][col] = 'Q'
            cols.add(col)
            diag.add(row - col)
            a_diag.add(row + col)
            
            self.placeQueen(row + 1, cols, diag, a_diag, chess, n, possible_ans)
            
            chess[row][col] = '.'
            cols.remove(col)
            diag.remove(row - col)
            a_diag.remove(row + col)

    def solveNQueens(self, n: int) -> List[List[str]]:

        possible_ans = []
        chess = [["."] * n for i in range(n)]
        cols = set()
        diag = set()
        a_diag = set()
        self.placeQueen(0, cols, diag, a_diag, chess, n, possible_ans)        
        return possible_ans