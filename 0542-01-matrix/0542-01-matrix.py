class Solution:
    def isValid(self, i, j, n, m, ans):
        if i >= 0 and i < n and j >= 0 and j < m and ans[i][j] == -1:
            return True
        return False

    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n, m = len(mat), len(mat[0])
        ans = [[-1 for i in range(m)] for j in range(n)]
        q = []
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    ans[i][j] = 0
                    q.append((i, j, 0))
        
        row = [1, 0, -1, 0]
        col = [0, 1, 0, -1]

        while q:
            i, j, d = q.pop(0)
            for k in range(4):
                x, y = i + row[k], j + col[k]
                if self.isValid(x, y, n, m, ans):
                    ans[x][y] = d+1
                    q.append((x, y, d+1))
        
        return ans