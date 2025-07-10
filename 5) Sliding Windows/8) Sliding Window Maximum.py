"""
Approach: Given an array of integers, we have to find the maximum number for each sliding window of size k.
One easy way that can come into your mind is just compare all the elements of each sliding window.
But this will take O(n*k) time complexity. How can we improve it more? Well by removing redundancy.
Suppose we got a number say 'x' which is greater than any other number before it in the window. Then for further increasing size or sliding of the window, we dont require those lesser values.
So we dont go through them for the max finding process at all! So which data structure to use for keeping track of "from where we start comparision"?
(You might be thinking of a single variable for this. But it wont work as we have to also store all the lower values after the highest value too. You might be wondering why?
Because, if the window is of max size, we have to slide it and thus the value which was smaller than the highest value can now be the new highest value! So yeah we can direclty remove the lower values 
left to the highest values but cant do the same for the lower values to the right as they might become the highest value later)

well how about a stack? yes a stack would work for this purpose but there is again the case where we have to slide the window and thus thought the highest value, we have to remove it from the stack.
But according to our setup of decreasing all lesser values to the left, the highest value will be the leftmost element. Then how will we be able to delete the leftmost element from stack?
So we use deque(double ended queue) where can insert and remove from both sides! And as we are tracking "from where we start comparision", we store index in the deque. 
"""

def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
    q = deque()
    l = r = 0
    output = []
    
    while r<len(nums):
        while q and nums[q[-1]]<nums[r]:    #removing all lesser value to the left of the new value
            q.pop()
        q.append(r)    #after removing all lesser values to its left, we finally add it to the deque
        
        if l>q[0]:    #if the value is outside the window(meaning its index is less than the left index of the window), we stop tracking it
            q.popleft()
        
        if (r-l+1) >= k:    #if the size of the window we have made till now is of max size, we start getting our max values for the window and then slide it
            output.append(nums[q[0]])
            l+=1
        r+=1
    return output
