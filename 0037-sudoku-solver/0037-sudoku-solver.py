class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row = [[] for i in range(9)]
        col = [[] for i in range(9)]
        box = [[] for i in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    row[i].append(board[i][j])
                    col[j].append(board[i][j])
                    box[(i//3)*3+(j//3)].append(board[i][j])
        
        def bt(r,c):
            if r==9:
                return True
            if c==9:
                return bt(r+1,0)
            if board[r][c]!=".":
                return bt(r,c+1)
                
            boxid = (r//3)*3+(c//3)
            for num in "123456789":
                if num not in row[r] and num not in col[c] and num not in box[boxid]:
                    board[r][c] = num
                    row[r].append(num)
                    col[c].append(num)
                    box[(r//3)*3+(c//3)].append(num)

                    if bt(r,c+1):
                        return True
                    board[r][c] = "."
                    row[r].remove(num)
                    col[c].remove(num)
                    box[(r//3)*3+(c//3)].remove(num)
            return False
        bt(0,0)

