class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seenRow = {}
        seenColumn = {}
        seenBox = {
            0: set(),
            1: set(),
            2: set(),
            3: set(),
            4: set(),
            5: set(),
            6: set(),
            7: set(),
            8: set()
        }
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if board[i][j] not in seenRow:
                    seenRow.setdefault(board[i][j], set()).add(i)
                else:
                    if i in seenRow[board[i][j]]:
                        return False
                    else:
                        seenRow[board[i][j]].add(i)
                if board[i][j] not in seenColumn:
                    seenColumn.setdefault(board[i][j], set()).add(j)
                else:
                    if j in seenColumn[board[i][j]]:
                        return False
                    else:
                        seenColumn[board[i][j]].add(j)
                box_idx = (i // 3) * 3 + (j // 3)
                if board[i][j] not in seenBox[box_idx]:
                    seenBox[box_idx].add(board[i][j])
                else:
                    return False
        return True
