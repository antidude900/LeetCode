"""
Approach:
We are given an array say arr and a number say k, then we have to return the no of of contiguous sub-arrays where each of those sub-array have its sum of elements equals k.
For this, we will start taking sub-arrays from the start of arr and go on adding numbers to the sub-array from arr.
For each sub-array, we will be checking if the there is the prefix sum that if we subtract from the sum of the whole suarray will give k!
Here the prefix sum denotes the elements that we can be removing from the sub-array we took to get the sub-array we want whose sum equals k!
As it prefix sum meaning it adds up the elements from start, the contingous nature of sub-array is guarenteed.
So we are going to store the prefix sum in a hash map to check if we have any choices to remove elements to get sum k.
(Why not hash-set?:
There might be multiple ways to remove the elements which give sum k. so we use a hash map to store how many prefix_sum we have that can give k when they are removed
)
"""

def subarraySum(nums: List[int], k: int) -> int:
    res = 0    #it stores the total no of the required sub-array possible
    currentSum = 0    #it stores the sum of the sub-array at each iteration
    prefixSum={0:1}    #this is for the base case! suppose we dont need to remove any elements to make the sum k. thus prefix_sum=0 denotes that!
    for num in nums:    
        currentSum+=num    
        diff = currentSum-k    #diff is the sum which we should be removing from the sum of the current sub-array. 
        res += prefixSum.get(diff,0)    #so we check if any prefix_sum=diff exists or not. 
                                        #If yes, the amount of such prefix_sum gives the total no of ways we can remove ahead elements to get the required sub-array
                                        #so if there are 'n' no of ways we can remove ahead elements to get the required sub-array, then there are 'n' such sub-array we can make!
        
        prefixSum[currentSum] = 1+prefixSum.get(currentSum,0)    #updaing the prefix_sum
                                                                 #as non-negative integers also exists in the array, the same prefix sum can occur
                                                                 #in that case, we have to increase the frequency/amount of that prefix sum
    return res
