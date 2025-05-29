"""
Approach:
We are given a array of integers and using the minimum size of subarray, we have to make its sum >= to the given target and we hav to return the minimum size.
we use the sliding window alogrithm where we increase the right of the window until we get the sum of the substring >=target.
After that we have to find the length fo the subarray and if it is minimimum, store it as minimum and then decrease the size of the window from left
After removing that value from left if still the subarray is >=target, we again do the same thing above.
"""

def minSubArrayLen(target: int, nums: List[int]) -> int:
    currSum = 0
    left = 0
    min_length = float(inf)
    for right in range(len(nums)):
        currSum+=nums[right]
        while currSum>=target:
            min_length = min(min_length,right-left+1)
            currSum-=nums[left]
            left+=1
    return 0 if min_length == float(inf) else min_length
        
