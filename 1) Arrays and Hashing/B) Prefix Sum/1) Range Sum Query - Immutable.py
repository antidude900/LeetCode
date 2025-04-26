"""
Apporach:
In this question, we have to find the sum of the numbers between a given range say between left and right inclusive
For this, we can use the prefix sum algorithm!
Here as we only care about the range given by the left and right index and dont need any personal searching of numbers,
we don't need hash map or set!
So, simply we make another list say prefix_sums where we store our precomputation such that for a index in the given list say nums, 
we add all the numbers below it and including itself. 
Thus a value in a index of the prefix_sums gives the sum of all the numbers upto that index from beginning in the nums list.

Now, to finding the sum of all numbers of between left and right, we just get the prefix sum of right 
and then subtract the prefix sum of the index below left which leaves us with only the sum of numbers between left and right!
"""

prefix_sum = []
prefix = 0
for num in nums:
    prefix+=num
    prefix_sum.append(prefix)
   
def sumRange(left: int, right: int) -> int:
    return prefix_sum[right]-(prefix_sum[left-1] if left>0 else 0)
