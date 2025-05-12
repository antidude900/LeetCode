"""
Approach:
Given a sorted array of numbers, we have to find the given target.
For this we use the logic we use while going through a word dictionary irl.
"""

def search(nums: List[int], target: int) -> int:
    left = 0
    right =  len(nums)-1
    while(left<=right):
        mid = (left+right)//2 
        if nums[mid] == target:
            return mid
        elif nums[mid]<target:
            left = mid+1
        else:
            right = mid-1
    return -1
