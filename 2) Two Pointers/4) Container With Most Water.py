"""
Approach:

"""

def maxArea(height: List[int]) -> int:
    max_area = 0
    
    i = 0
    j = len(height)-1
    while (i<j):
        max_area = max(max_area, min(height[i],height[j])*(j-i))
    
        if height[j]>height[i]:
            i+=1
        else:
            j-=1
    return max_area
