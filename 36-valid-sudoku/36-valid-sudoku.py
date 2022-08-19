class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in board:
            yeet = [j for j in i if j != '.']
            if len(set(yeet)) != len(yeet):
                return False
        for i in range(9):
            yeet = [board[j][i] for j in range(9) if board[j][i] != "."]
            if len(set(yeet)) != len(yeet):
                return False
        for k in [
                    [1,1], [1,4], [1,7],
                    [4,1], [4,4], [4,7],
                    [7,1], [7,4], [7,7]
                 ]:
            i,j = k[0], k[1]
            temp = []
            temp.append(board[i - 1][j - 1])
            temp.append(board[i - 1][j])
            temp.append(board[i - 1][j + 1])
            temp.append(board[i][j - 1])
            temp.append(board[i][j + 1])
            temp.append(board[i + 1][j - 1])
            temp.append(board[i + 1][j])
            temp.append(board[i + 1][j + 1])
            temp.append(board[i][j])
            
            temp = [i for i in temp if i != "."]
            if len(set(temp)) != len(temp):
                return False
        return True