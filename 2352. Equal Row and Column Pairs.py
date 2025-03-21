from collections import defaultdict
class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row_map = defaultdict(int)
        
        # Store the row occurrences in the hashmap
        for row in grid:
            row_map[tuple(row)] += 1
        count = 0
        for j in range(len(grid)):
            col = [grid[i][j] for i in range (len(grid))]
            count+=row_map[tuple(col)]
        return count
        
sol = Solution()
print(sol.equalPairs([[3,2,1],[1,7,6],[2,7,7]]))