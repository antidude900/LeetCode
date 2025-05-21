"""
Approach:
Here we have to find duplicates such that the difference between their indices is atmost k.
For this we implement a sliding window which keeps on increasing its right part and taking values checking if it already contains that value.
If the length of the sliding widnow exceeds 'k', the we move the left part ahead.
"""

def containsNearbyDuplicate(nums: List[int], k: int) -> bool:
    if len(nums) == len(set(nums)): 
        return False
        
    window  = set()
    left= 0
    for right in range(len(nums)):        
        if right-left>k:    #check the window length first before checking for the element inside to avoid checking element in a window of size>k.
            window.remove(nums[left])
            left+=1

        if nums[right] in window:
            return True
          
        window.add(nums[right])
    return False
