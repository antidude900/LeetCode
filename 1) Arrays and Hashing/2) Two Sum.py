"""
Approach:
There is a pattern you cann learn from this question. 
Whenever you have to find a number which when done basic arithmetic(add,subract,product,divide) with another number such that it gives the target value;
we first take a number from the given data as current num and apply basic equation for eg: current_num (+,-,*,/) num_to_find = target value
As we have the current_num and the target value, we can find the num_to_find the equation. 

Here also in two sum, we need two numbers that add up to give a target value. 
So we take a number from the given data for value ofcurrent_num and using the equation, we find the value for num_to_find.
Then if num_to_find exists in the given set of data, we have a solution for the two sum problem.

As trying to find the num_to_find directly in the given list will take O(n), we instead make a dictionary where we store the value in such a way that:
the key in the dictionary gives the value of the number in the list and the value in the dictionary gives the index of the number in the list
"""


def twoSum(nums: List[int], target: int) -> List[int]:
    scanned={}
    for i in range(len(nums)):
        second = target-nums[i]
        
        if second in scanned:
            return [scanned[second],i] 
        
        scanned[nums[i]] = i
