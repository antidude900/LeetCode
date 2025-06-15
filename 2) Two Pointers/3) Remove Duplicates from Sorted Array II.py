"""
Approach:
Here we let duplicates to exist atmost 2 for each element.
One way is by keeping count of each number and it its count<2(i.e count = 0 or 1) then we increase the pointer to the array where we have atmost two duplicate for each element.
(Can overwrite the given one)

But why need to keep count of each number when we can just see see 2 index before the current one(we dont care about the 1 index down because a duplicate is accepted)
"""

def removeDuplicates(nums: List[int]) -> int:
    i = 2
    for j in range(2,len(nums)):
        if nums[j] != nums[i-2]: #why not j-2? its because if we take the index of the old array 'j' to see its 2nd before one, it might not work due to the improper tracking
                                 #as we wont be checking 2nd before from where we got after the change 'i' but rather anywhere from the string which might result to 
                                 #one element matching with its first occurance
                                 #so to avoid that, we are seeing 2nd before from our new array. the number trying to come in the new array will be checked with the 2nd last element
                                 #of the new array, as at the end the thing we want is that the i and i-2 to not match for the new array. 
            nums[i] = nums[j]
            i+=1
    return i

#as we dont need specially need the index 'j', we can just iterate through the num instead by index
def removeDuplicates(nums: List[int]) -> int:
    l = 0
    for num in nums:
        if l < 2 or num != nums[l - 2]: #if the index is simply less than 2, duplicate checking will be valid fore sure. Else, we have to do the duplicate checking
            nums[l] = num
            l += 1
        #the hash map way for storing count is similar to this. only the if statement changes using count and a extra step of updating hash map is done inside if block
    return l
