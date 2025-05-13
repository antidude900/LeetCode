"""
Approach:
Given a 2D matrix, we have to find whether a given number exists in that matrix or not.
You may think of making a hashmap but making a hash map for m*n matrix will take time of O(m*n)
So instead we use binary search! First find the correct row using binary search and then at that row, we iterate through each column again using binary search
So to find correct row it will take log m time and for correct column log n. So total time is O(log(m)+log(n)) = O(log(m*n)) which is better than O(m*n)
"""

def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    startRow, endRow = 0, len(matrix) - 1
  
    while startRow <= endRow:    #binary search of row
        midRow = startRow + (endRow - startRow) // 2    #is equivalent to (startRow+endRow)/2. But this method will prevent overflow of number
        
        if matrix[midRow][0] <= target <= matrix[midRow][-1]:    
            left, right = 0, len(matrix[midRow]) - 1
            while left <= right:    #binary search of column of the correct row
                mid = left + (right - left) // 2
                if matrix[midRow][mid] == target:
                    return True
                elif matrix[midRow][mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return False
            
        elif target > matrix[midRow][-1]:
            startRow = midRow + 1
            
        else:
            endRow = midRow - 1
    return False
