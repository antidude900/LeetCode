"""
Approach: In a m*n grid, there are cells with one of the three values:
0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.

The flow of time here is calculated in minutes and each minute a rotten orange makes fresh organges adjcent to it(not diagonally) stale.
So, we have to return the mininum number of minutes at which all the oranges in grid becomes rotten. If not possible, we return -1.

We can see that this problem matches with our Shortest Path question. The only difference is that we measure in terms of minutes rather than cells.
So, we apply BFS in this case too. But here, even though our queue gets emptied, still there is a possibility that we havent completed the whole process.
What if there is a fresh orange whose adjacent cells doesn't contain any oranges?

So at the end to know if we really have made every oranges rotten; we first count the total no of fresh oranges in the grid at start and decrement it
every time we go through a adjacent fresh orange.
"""

def orangesRotting(grid: List[List[int]]) -> int:

    ROWS, COLS = len(grid), len(grid[0])
    queue = deque()
    direction = [(0,1),(1,0),(0,-1),(-1,0)]
    fresh = 0

    for row in range(ROWS):    
        for col in range(COLS):
            # when couting the no of fresh oranges, we also track the rotten oranges from where we can start exploring
            # this makes the exploration logic alot simple as before if we had explored from any cell, we had to handle cases for all types of values in that cell
            if grid[row][col] == 2:
                queue.append((row,col,0))
            elif grid[row][col] == 1:
                fresh+=1

    m = 0    #counting no of minutes
    while queue:
        r,c,m = queue.popleft()
        for dr,dc in direction:
            nr, nc  = r+dr, c+dc
            if nr<0 or nc<0 or nr == ROWS or nc == COLS:
                continue
            if grid[nr][nc] != 1:    #if its not a fresh orange, the process of spreading rotteness won't go through that path
                continue
            
            grid[nr][nc] = 2    #making the fresh orange rotten
            fresh-=1
            queue.append((nr,nc,m+1))    #going through this path as other oranges adjacent to this orange will also get rotten next minute
    
    return -1 if fresh else m    #if any fresh orange is left even after the queue empties, it's not possible to make all oranges rotten
