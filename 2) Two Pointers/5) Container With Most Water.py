"""
Approach:
Lines of different height will be at different points unarranged. 
You can make container with two of the lines where the minimum height between the lines gives the height of the container
(Because if water put more than that height, then the water will flow out from that side with less height)
and the distance between the two lines gives the length of the container.
So now we have to find those two lines which gives the container of maximum area.
For this we can take two pointer one from leftmost and one from rightmost(to maximize length)
Now, we have to focus to find the max hieght. When updating the pointers in any way, the length will decrease by 1 for sure.
So the decision we can only take while updating the pointers is about height.
Simply the line whose height is greater than the other is kept and the other is changed
"""

def maxArea(height: List[int]) -> int:
    max_area = 0
    i = 0
    j = len(height)-1
    max_height = max(height)
    
    while (i<j):
        
        curr_area = min(height[i],height[j])*(j-i)    #calculating area = height_of_container*length of container
        max_area = max(max_area, curr_area)    
        
        if (max_height*(j-i)<=max_area):    
            break    #max_height among the all heights is constant(we took this so to give (j-i) the best possible height it can get)
                     #(j-i) changes by decreasing with each pointer update.So max_height*(j-i) also decreases with each pointer update.
                     #which means if max_height*(j-i) is already less that the max_area we have found upto now,
                     #theres no chance it will find area more than the current max_area because it will again decrease with the pointer update
                     #and it cant find any other height greater than max_height
                     #so there is no other area greater than the current max_area. thus current max_area is our final max_area
    
        if height[j]>height[i]:
            i+=1
        else:
            j-=1
    return max_area
    
