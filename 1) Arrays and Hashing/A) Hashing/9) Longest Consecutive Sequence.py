"""
Approach:
Here from the given list of numbers, we have to make the longest sequence and then return the length of longest possible sequence.

First we change the nums list to a set to remove any duplicate elements(as same element using twice in the sequence isnt considered to increase the length of sequence)
[If it was considered then, we would have to use hashmap where key stores the number and value stores its frequency]
and to make the search for the next consecutive number after the current number fast!

We first start with a number. If another number consecutive to the current number in reverse direction exists, it means we have another smaller number to start our sequence.
So we dont start making sequence from the current number and skip(to make sequence after we reach that smaller number)

If theres no smaller consecutive number than it, than the current number is the start of our sequence with a length of 1.
Check if its consecutive number exists on the list of numbers. If yes increase the length of the sequence by 1 and go on till the sequence goes on.
After finishing the sequence, check if its length is greater than the length of the longest sequence observed at past. 
If yes, update the longest sequence length.
"""

def longestConsecutive(nums: List[int]) -> int:
    nums = set(nums)
    max_count = 0
    
    for num in nums:
        if num-1 in nums:
            continue
        
        count = 1
        next_num = num+1
        
        while next_num in nums:
            next_num+=1
            count+=1
          
        if count>max_count:
            max_count = count
            
    return max_count
