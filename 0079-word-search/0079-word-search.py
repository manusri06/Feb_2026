class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def bt(r,c,indx):
            if indx==len(word):
                return True
            if r>=m or r<0 or c<0 or c>=n or board[r][c]!=word[indx]:
                return False
            temp = board[r][c]
            board[r][c] = '#'
            found = bt(r,c-1,indx+1) or bt(r,c+1,indx+1)or bt(r+1,c,indx+1) or bt(r-1,c,indx+1)
            board[r][c] = temp
            return found
        


        m = len(board)
        n = len(board[0])

        for r in range(m):
            for c in range(n):
                if bt(r,c,0):
                    return True
        return False

