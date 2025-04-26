"""
Approach:
Its approach is build upon the approach of:Range Sum Query - Immutable

Here, a index in the prefix_sum matrix(2d list) stores the sum of all the values in the box where the box is formed by:
the upmost left of the box is the 0th row and 0th col of the nums matrix.
the bottom right of the box is the ith row and jth column of the index in the prefix_sums matrix

So, how do we do the sum at a index say 'i'('i' is made of (row,col)) ? Its simple. 
the value of the index in the prefix sum just left to 'i'(row-1,col) holds the sum of all values left to it and in the same row
the value of the index in the prefix sum just top of 'i'(row,col-1) holds the sum of all values inside the box whose bottom right corner is just at the top of 'i'


Now, for a given upperleft corner(r1,c1) and bottomright corner(r2,c2), how do we find the sum of values inside that box?
first we simply take the prefix sum of the bottomright corner i.e the sum of values inside the box of upperleft corner(0,0) and bottomright corner(r2,c2)
Now to reduce the box upperleft corner to (r1,c1), we remove the unwamted box at top of our total box i.e remove the box whose bottomright corner is direclty above (r1,c2)
then we remove the unwanted box at the left of our total box i.e remove the box whose bottomright corner is direclty left of (r2,c1)
But theres a problem we face! While we subract both the unwanted upper and lower box, we subtract their intersection portion of those boxes to each other twice.
first time, it gets subtracted from the unwanted boxes but the next time as those value dont exist in the unwanted boxes, it gets subtraced from our required box!
So at end, we add the box whose bottomright corner is diagonally up of (r1,c1) which is the intersecting box!

Also, for the whole process we use padding at the top and left of the prefix_sum matrix to avoid out of boundary error.
"""

rows = len(matrix) 
cols = len(matrix[0])
prefix_sum = [[0] * (cols+1) for _ in range(rows+1)]    #adding a layer padding
for row in range(rows):
    prefix = 0
    for col in range(cols):    #here we find the prefix sum of row+1,col+1
        prefix+=matrix[row][col]    #the (row,col) which is diagonally above row+1,col+1 element int the prefix sum will be direclty left to the same element at given matrix(no padding)
                                    #in this way, we add all the values to its left at the same row
        above = prefix_sum[row][col+1]    #adding the box top of it
        prefix_sum[row+1][col+1] = prefix+above 

def sumRegion(row1: int, col1: int, row2: int, col2: int) -> int:
    r1,c1,r2,c2 = row1+1,col1+1,row2+1,col2+1 #for using the (row,col) in the prefix_sums, we first incremenet it by 1 to adjust with the padding in the prefix_sums
    total_size = prefix_sum[r2][c2] 
    above = prefix_sum[r1-1][c2]
    left = prefix_sum[r2][c1-1]
    return total_size - above - left + prefix_sum[r1-1][c1-1]
