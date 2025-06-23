"""
Approach:
Given a rotated array, we have to find the target number. 
Here we apply binary search. In a simple sorted array, we knew wheter to change left or right only by looking the target and the mid.
But as this is rotated, we first have to check if the mid lies in the left sorted sub-section or the right one.
Then we have to check if the target lies in the section or not and change the pointers according to that
"""

def search(nums: List[int], target: int) -> int:
    left , right = 0, len(nums)-1
  
    while left<=right:
        mid = left+(right-left)//2
        if target == nums[mid]:
            return mid
        
        if nums[left]<=nums[mid]:    #checking if the mid is in the left sorted section
            if target<nums[left] or target>nums[mid]:    #if the target doesnt lie in the left section, we go to the right section
                left = mid + 1
            else:    #if it does lie in the left section, we stay there
                right = mid-1
        
        else:    #or in the right sorted section
            if target>nums[right] or target<nums[mid]:    #if the target doesnt lie in the right section, we go to the left section
                right = mid - 1
            else:    #if it does lie in the right section, we stay there
                left = mid + 1
    return -1
