"""
Given: Same setup as the previous question 'Number of island', just we nave to count the max area among the islands instead of counting the total no islands.
When reaching a water, we return 0 as it contributes nothing for the area of a island. And when we finish navigation from a land, 
we return 1(as it cotrinutes unit area) plus the area of the total lands we found after further navigation after it.
Remember to mark each navigated land as water so that it wont further contribute in the area counting in the future.
Also only after a whole navigation finishes from the start of our search, we get the area of the island. Then we can compare the area with the area of the biggest island upto now.
"""

def maxAreaOfIsland(grid: List[List[int]]) -> int:
    ROWS, COLS = len(grid),len(grid[0])
    max_area = 0
  
    def dfs(r,c):
        if r<0 or c<0 or r==ROWS or c==COLS or grid[r][c] == 0:
            return 0
        
        grid[r][c]=0
        return 1+dfs(r-1,c)+dfs(r,c-1)+dfs(r+1,c)+dfs(r,c+1)
    
    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == 1:
                max_area = max(max_area,dfs(r,c))
    return max_area
