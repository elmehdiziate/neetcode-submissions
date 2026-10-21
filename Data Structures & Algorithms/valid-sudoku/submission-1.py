class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for l in board:
            seen_row = set()
            for item in l:
                if item in seen_row and item != '.':
                    return False
                seen_row.add(item)
        for l in zip(*board):
            seen_col = set()
            for item in l:
                if item in seen_col and item != '.':
                    return False
                seen_col.add(item)
        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                seen_box = set()
                
                for r in range(box_row, box_row + 3):
                    for c in range(box_col, box_col + 3):
                        item = board[r][c]
                        if item != '.':
                            if item in seen_box:
                                return False
                            seen_box.add(item)
        
        return True
        