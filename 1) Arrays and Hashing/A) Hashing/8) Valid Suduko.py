"""
Approach:
Here, we just have to see if number from 1 to 9 doesnt repeat in any row, col or square in a 3*3 grid

For this we make a dict which key stores the index of the row/col/square it is(0-8) and its value stores the list of values in that row/col/square.
As the check of whether a value already exists inside the list of values should be done, using set to store the list of values is optimal.
Also for the square, we require 2 indicies for its location and as we are using the key for storing the index, we cannot use list for keys so we use tuples as keys for storing the 2 index.
(as row and col are in a single dimension i.e row is in horizontal direction and col in vertical direction only but for the square,
its goes only upto 3 steps in horizontal direction and after then it goes 1 step down in vertical direction and so on. 
So, as squares move in 2 direction that is in 2D, we need two indices for its location.)

For a value in board[r][c], we have to check the the respective row,col and square i.e row[r],col[c] and square[r//3,c//3] to check if the value exists there or not.
(r//3,c//3 groups the 9 rows into 3 groups and 9 cols into 3 groups thus grouping numbers into 3*3=9 squares. Thus (r//3,c//3) gives the row and col of the 9 squares.

If the value already exists, then the sudoko is invalid else update it will the value to keep of the record that this value now exists in the row/col/square.
"""

def isValidSudoku(board: List[List[str]]) -> bool:
    rows = defaultdict(set)
    cols = defaultdict(set)
    squares = defaultdict(set)
  
    for r in range(len(board)):
        for c in range(len(board[0])):
            if (board[r][c] == "."):
                continue
            
            if (board[r][c] in rows[r] or
                board[r][c] in cols[c] or
                board[r][c] in squares[(r//3,c//3)]):
                return False
            
            rows[r].add(board[r][c])
            cols[c].add(board[r][c])
            squares[(r//3,c//3)].add(board[r][c])
          
    return True    #if no duplicates exists in any row/col/squares, its a valid suduko
