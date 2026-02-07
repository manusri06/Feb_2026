class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0
        
        r = len(obstacleGrid)
        c = len(obstacleGrid[0])
        dp = [[0]*c for i in range(r)]

    
        for i in range(c):
            if obstacleGrid[0][i] != 1:
                dp[0][i] = 1
            else:
                break

        for i in range(1,r):
            if obstacleGrid[i][0] != 1:
                dp[i][0] = 1
            else:
                break

        for i in range(1,r):
            for j in range(1,c):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i-1][j]+dp[i][j-1]
        return dp[r-1][c-1]