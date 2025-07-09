"""
Approach:

"""

def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
    q = deque()
    l = r = 0
    output = []
    
    while r<len(nums):
        while q and nums[q[-1]]<nums[r]:
            q.pop()
        q.append(r)
        if l>q[0]:
            q.popleft()
        
    
        if (r-l+1) >= k:
            output.append(nums[q[0]])
            l+=1
        r+=1
    return output
