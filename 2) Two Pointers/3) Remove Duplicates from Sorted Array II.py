"""
Approach:
Here we let duplicates to exist atmost 2 for each element.
One way is by keeping count of each number and it its count<2(i.e count = 0 or 1) then we increase the pointer to the array where we have atmost two duplicate for each element.
(Can overwrite the given one)

But why need to keep count of each number when we can just see see 2 index before the current one(we dont care about the 1 index down because a duplicate is accepted)
"""

def removeDuplicates(nums: List[int]) -> int:
    l = 0
    for num in nums:
        if l < 2 or num != nums[l - 2]: #if the index is simply less than 2, duplicate checking will be valid fore sure. Else, we have to do the duplicate checking
            nums[l] = num
            l += 1
        #the hash map way for storing count is similar to this. only the if statement changes using count and a extra step of updating hash map is done inside if block
    return l
