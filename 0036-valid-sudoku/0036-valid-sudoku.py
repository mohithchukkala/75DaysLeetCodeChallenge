class Solution(object):
    def isValidSudoku(self, board):
        rows=[set() for i in range(len(board))]
        cols=[set() for i in range(len(board))]
        boxes=[set() for i in range(len(board))]
        for r in range(len(board)):
            for c in range(len(board)):
                val=board[r][c]
                if val==".":
                    continue
                if val in rows[r]:
                    return False
                rows[r].add(val)

                if val in cols[c]:
                    return False
                cols[c].add(val)
                box_idx=(r//3)*3+(c//3)
                if val in boxes[box_idx]:
                    return False
                boxes[box_idx].add(val)
        return True
                
        
        