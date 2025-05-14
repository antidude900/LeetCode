"""
Approach:
We have to find the combination of bars connected which gives the largest array(for the connected section)
Let's go through some oobservations which will make this problem easy!
If the right bar to current bar is less, we cannot go more right with the current bar as hollow.
So we can finnaly calculate the bar area i.e height*(from where we started to where it ended)
Thus we can use a stack where if the new bar has smaller height than the top of the one, we pop out the top bar.
We do this pop until the top is smaller.(For each top popped, for where it ended: take the index of that new bar(because it was able to make its connected area upto that bar))
Also, the point the new bar reached after all that popping(which will be given by latest popped bar) is the index from where the new bar starts its connected area

If there are still any bars left in that stack, it means those bars connected area stretched until the very end. 
Now we calculate all those bar areas with the end index being the end of the heights list
"""

def largestRectangleArea(heights: List[int]) -> int:
    stack = []
    max_area = 0
  
    for i,h in enumerate(heights):
        start = i
        while stack and stack[-1][1]>h:
            index,height = stack.pop()
            max_area = max(max_area, height*(i-index))
            start = index
        stack.append((start,h))
    
    for i,h in stack:
        max_area = max(max_area,h*(len(heights)-i))    #we did len(heights) instead of len(heights)-1 
                                                       #because we want the width upto the back of the last bar not upto the front of the last bar
    return max_area

#But here we have to store both height and index. how about only storing the index? 
#If we are only storing the index in the stack, for sure we will need the original index of the element to get its height  
#so how do we get its starting index? We simply see the index of the element below it in the stack as its the nearest element smaller than it at the left which is from where it starts!

def largestRectangleArea(self, heights: List[int]) -> int:
    stack = [-1]   #This helps in two ways. To stop the popping of the elements from stack at the end(when we reach the final iteration)
                   #As we have to see the previous element in the stack to find the start, 
                   #it handles the edge case of only one element remaining in the stack(giving its index as its width)
    heights.append(0)    #This starts the popping of the elements of the stack at the final iteration until we reach that -1 in the stack
    area = 0
    for i in range(len(heights)):
        while heights[i] < heights[stack[-1]]:
            h = heights[stack.pop()]
            w = i - stack[-1] - 1    #Here we are doign end of the current bar(as i is  the index of the start of the bar after it) - start of the nearest bar smaller to its left. 
                                     #But the width starts from the end of that nearest bar smaller than it to its left.
                                     #So we have to do decrease that extra width taken i.e the width of that bar = 1
            area = max(area, h * w)
        stack.append(i)
    
    return area
