"""
Approach: Given a matrix where '1' represents land and '0' represents water, we have to find the total no of islands. We suppose to have water outside the boundary for the edge lands.
Remember that islands are made by a number of lands connected together and that group of land is surrounded by water on both four sides.
So, how can we do that? well we navigate through a peice of lands to its ajdacent lands until we find no adjacent lands to the group. it means thats a single island.
After the navigation finishes i.e we have no adjacent lands left in our navigation, we can mark that as a island and then start a new navigation through another position if it holds a land.
For every land navigated in a navigation, we can assume that as water so that later from any adjacent land, we come back to it again while navigating which can create a infinite loop.
This also helps while starting a new navigation to prevent starting from the same piece of land from the earlier island which causes mistake in island couting.
"""

def numIslands(grid: List[List[str]]) -> int:
    ROWS,COLS = len(grid),len(grid[0])
    total = 0
    
    def dfs(r,c):
        if r<0 or c<0 or r==ROWS or c==COLS or grid[r][c]=="0":  #if its a water, then we dont navigate in that position
            return
          
        grid[r][c] = "0"  #marking the land as water after successfull navigation to prevent future navigation to the same island

        # navigating horizontally or vertically(we dont need to navigate diagonally becuase if theres land, we will get there with a series horizontal and vertical movements)
        dfs(r-1,c)  #trying to navigate down
        dfs(r,c-1)  #trying to navigate left
        dfs(r+1,c)  #trying to navigate up
        dfs(r,c+1)  #trying to navigate right

        #all the navigation finishing means we have water all sides and no lands
      
    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == "1":  #if we find a position where we have land, we navigate to find all adjacent lands to it and count all as a single island
                dfs(r,c)
                total+=1
    return total
