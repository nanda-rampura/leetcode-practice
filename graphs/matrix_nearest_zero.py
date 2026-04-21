from collections import deque
from typing import List


class MatrixNearestZero:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        queue = deque()
        rows = len(mat)
        cols = len(mat[0])

        for row in range(rows):
            for col in range(cols):
                if mat[row][col] == 0:
                    queue.append((row,col))
                else:
                    mat[row][col] = -1
                    

        directions = [[-1,0],[1,0],[0,1],[0,-1]]
        while queue:
            r, c = queue.popleft()

            for d in directions:
                nr = r + d[0]
                nc = c + d[1]

                if 0 <= nr < rows and 0 <= nc < cols and mat[nr][nc] == -1:
                    mat[nr][nc] = mat[r][c] + 1
                    queue.append((nr,nc))
    
        return mat