"""
Apporach: Return the shortest path in the the matrix for going from top left to bottom right. 
The length of the path is the no of cells present in the path. We can move horizontally, veritcally and even diagonally.
Any cell with value of 1 is blocked and we can't go through it.

We can do our classic DFS, but the problem is that DFS explores one path completely before exploring alternative paths. 
As a result, the first path that reaches the destination is not necessarily the shortest one.
So, we would need to explore all possible paths and keep track of the minimum length found which gets very expensive!

But we don't have to explore through every possible paths! 
We just have to explore through all those cells 'x' steps away from the starting cell until we get a 'x' step at which the cell is the end cell.
So first we go through all the cells which are 1 step away from the first cell. There, if we find any cell which is the end cell, we stop.
Else, we go to the cells which are 2 steps away from the second cell. And we go on doing this process till we find the end cell.

Before reaching the end cell by 'x' steps, as we have gone through all cells which takes smaller no of steps (x-1,x-2,x-3,...);
we are guarenteed that we haven't missed any shorter path.
Thus we can apply BFS going a layer at a time, and finding the layer where our required cell is.
(layer 'x' contains all the cells 'x' step away from the starting cell)

And as we have to explore through the shallowest layer at first for finding the shortest path, we use a queue to access the layers in a FIFO nature.
"""

def shortestPathBinaryMatrix(grid: List[List[int]]) -> int:
  if grid[0][0] == 1:    #if the top-left cell is blocked, we can't even start
      return -1

  ROWS, COLS = len(grid), len(grid[0])
  directions = ([0,1], [0,-1], [1,0], [-1,0], [1,1], [-1,-1], [1,-1], [-1,1])    #going through all 8 directions

  queue = deque([(0, 0, 1)])    #starting from the top left cell
  grid[0][0] = 1    #marking it as blocked to not visit it again

  while queue:
      r, c, d = queue.popleft()    #exploring the shallower layer first

      if r == ROWS - 1 and c == COLS - 1: 
          return d

      for dr, dc in directions:
          nr, nc = r + dr, c + dc

          if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 0:
              queue.append((nr, nc, d + 1))    #going to the next layer increase the length by 1
              grid[nr][nc] = 1  

  return -1
