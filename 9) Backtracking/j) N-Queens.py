"""
Approach: Given an integer n, we have a n*n board where we have to place n queens where no queen attack each other and return all such solutions.
For this we know that no queens should be in same row or same col or same diagonal. so we have to keep track of each row, col and diagonal.
But we can make it simpler by just putting a new queen in the next row not occupied. In such way, we just have to keep track at which column we kept it and also at the same time which diagonal.
For tracking the diagonal, we use positive and negative diagonal. positive diagonal keeps track of bottom left to top right diagonal and each square in such diagonal has a constant value of (r+c).
Similarly, negative diagonal keeps track of top left to bttom right diagonal and each square in such diagonal has a constant value of (r-c).
After we choose to keep a queen in a certain column, we specify in each tracker for col, positive diagonal and negative diagonal that this place has been occupied so that we dont put the queen in the next row in those places.
"""


def solveNQueens(n: int) -> List[List[str]]:
    cols = set()  #tracker for column
    posD = set()  #tracker for positive diagonal
    negD = set()  #tracker for negative diagonal
    board = [["."]*n for _ in range(n)]  #making the board where we have to put our queen
    res = []
  
    def backtrack(r):
        if r == n:  
            copy = [''.join(row) for row in board]  #makign copy of our board to put in the result(a row will be written as a string, so that we can write a solution in 1-D form)
            res.append(copy)
            return 
        
        for c in range(n):  #Going through each column in the row
            if c in cols or (r+c) in posD or (r-c) in negD: #checking if that column is valid to put our queen
                continue
            
            board[r][c] = 'Q' #if yes, we put our queen there and update trackers
            cols.add(c)
            posD.add(r+c)
            negD.add(r-c)
          
            backtrack(r+1) #going to the next row for the next queen
          
            board[r][c] = '.'  #removing all changes we did in our board for the placement in that column so that we can check the placement for another column
            cols.remove(c)
            posD.remove(r+c)
            negD.remove(r-c)
          
    backtrack(0)
    return res 
