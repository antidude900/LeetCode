"""
Approach:
From numbers ranging from 1 to n, we create a array containing n+1 numbers. There is only one repeated number and we have to find and return it.
For this we can use floyd's algorithm but setting up a linked list. for the linked list, the number itself points to another number by acting as a index.
Thus if a number is repeated, the same index will come twice and will be pointed by more than one number and thus a cycle is formed.

Now we can use the floyd algorithm that we learnt on Linked List II.
"""

def findDuplicate(nums: List[int]) -> int:
    slow, fast = 0,0    #the head for the linked list will the index 0
    while True:
        slow = nums[slow]    #the number will be used as index to carry out the node.next operation
        fast = nums[nums[fast]] 
        
        if slow == fast:
            break
            
    slow2 = 0 
    while True:
        slow2 = nums[slow2]
        slow = nums[slow]

        if slow == slow2:    #note that we contain numbers from 1 to n. so theres no way a number points to 0. 
                             #thus the head of the linked list can't be the head of the cycle. So, it doesn't matter if we check the == condition before or after the update
            return slow
            

