"""
Approach:
Given a elevation map, we have to find how much water can be trapped in that map i.e between the bars inside the map.
For this we will be checking each location of the map horizontally and see if water can be placed in that location or not. And if yes, how much?

You should have prior knowledge of the container with most water problem. 
There to find how much water can be put between two bars, we found the minimum between the height of the two bars to find the height of the container.
But which two bars to choose for that location? Well we take the maximu height bar on its left and then maximum height bar on its right.
(Think of a valley between two hills. there can be multiple high bumps in the valley but to get out from the valley, we dont care about the bumps but the two biggest hills)
Water can't go more up than those two bars. Moreover, the water can't go more up than the minium among the two bars(because it will overflow from that side)

Also, the location we are checking from may not be in the ground but also at some height. 
so we should also deduct that height to get the actual maximum height we can stack water upto.

There are three ways to perform this which in theory have same time complexity(when the constant is ignored) but different space complexity.
"""

#Prefix & Suffix Arrays

def trap(height: List[int]) -> int:
    n = len(height)
    if n == 0:
        return 0
    
    leftMax = [0] * n    #prefix array to store the maximum height at 'i' index's left
    rightMax = [0] * n   #suffix array to store the maximum height at 'i' index's right
    
    leftMax[0] = height[0]    #here we can see that the leftmax at index 'i' is also including its own height in the comparision. this will be explained at end
    for i in range(1, n):
        leftMax[i] = max(leftMax[i - 1], height[i])    #why including its own height in the comparision of maximum height at its left will be explained at end.

    
    rightMax[n - 1] = height[n - 1]
    for i in range(n - 2, -1, -1):
        rightMax[i] = max(rightMax[i + 1], height[i])
    
    res = 0
    for i in range(n):
        res += min(leftMax[i], rightMax[i]) - height[i]    #finding the mimimum side of the container and then finding the relative height
    return res
    """
    Here, while finding the leftmax or rightmax at index 'i', we are also including its own height in the comparision.
    This is because when doing: min(leftMax[i], rightMax[i]) - height[i], if the minimum value between leftmax[i] and rightmax[i] is less than height[i]
    (for eg:for index 1 at: 1,2,3 the min(1,3)-2 = 1-2 = -1), 
    it means that theres no place to keep water at that location as the location is itself bigger than the mimimum side of the container which makes it prone to oveflow from beginning.
    But adding -1 to res is wrong! we should have added 0! so, if we included the height of that location in the leftmax of that location, 
    it solves the problem by giving 0 instead of -1 if it is greater than minimum side of the container. 
    (for eg:for index 1 at: 1,2,3 the min(2,3)-2 = 2-2 = 0).
    But you might be feeling if including the height will affect the comparision between leftmax and righmax? Well, no! Because we are including it in both of them!
    Say without including height, leftmax=a rightmax=b and height=h; then if we include height we will have a+h and b+h. 
    So when comparing a+h and b+h, as h is common in both we ignore h and just compare a and b!
    """

#Two Pointers

def trap(height: List[int]) -> int:
    if not height:
        return 0
        
    l, r = 0, len(height) - 1
    leftMax, rightMax = height[l], height[r]
    res = 0
    
    while l < r:
        """
        lets  understand how the pointers get updated!
        Suppose left pointer had less leftMax than the rightmax of the right pointer.
        Here comes two cases: 
        Case 1: the other values are greater than the rightmax of the rightmax.
        well then the leftmax will be be also less than the other values! so leftmax is the minimum side and we fit water according to that side
        Case 2: the other values are less than the rightmax of the rightmax.
        well then we dont care about the other values. the comparision was always about the maximum left and the maximum right height
        (at beginning, there will be only one height at the left side. so we dont have to worry about the maximum left)

        But what if leftMax had more value that rightmax? then we will be uncertain while comparing the leftmax with the other values.
        what if we had other values smaller than rightmax? Then we cant take rightmax as the minimum side!
        So its always better to analyze the the pointer whose corresponding side is less because it will make it the minimum side!
        """
        if leftMax < rightMax: #here we cant say that including height on both the leftmax and rightmax wont affect the comparision because the pointers are on different heights!
                               #but here the leftmax and rightmax for the index was compared without including the height of the index itself
                               #as the result was calculated for the next index with the comparision of the leftmax and rightmax of the previous one
            l += 1    #going to the next index
            leftMax = max(leftMax, height[l])    #now we can include the height in the leftmax so to prevent the -1 result problem.
            res += leftMax - height[l]    #calculating the relative height of the water to be stakced
        else:
            r -= 1
            rightMax = max(rightMax, height[r])
            res += rightMax - height[r]
    return res
