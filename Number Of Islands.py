class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        count = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1':
                    self.dfs(grid, row, col)
                    count += 1
        return count

    def dfs(self, grid, row, col):
        #If out of range or not an island
        # 0 <= row < len(grid) 0 <= col < len(grid[0])
        if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or grid[row][col] != "1":
            return
        #Replace searched squares with #
        grid[row][col] = "#"
        #4-way search
        self.dfs(grid, row + 1, col)
        self.dfs(grid, row - 1, col)
        self.dfs(grid, row, col + 1)
        self.dfs(grid, row, col - 1)  