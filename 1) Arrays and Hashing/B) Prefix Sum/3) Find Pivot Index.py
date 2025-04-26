"""
Approach:
Here we just have to find a index for which the sum of elements left to it is equal to the sum of elements right to it

For this we simply calculate pivot_sum like before and then check:
if the prefix sum of the element just left to that index i.e the sum of all the elements left to it
is equal to
the sum of remaning elements to the right i.e prefix_sum[index_of_last_element]-prefix_sum[index_observing_rn] 
"""

def pivotIndex(nums: List[int]) -> int:
    n=len(nums)
    prefix_sum = [0]*(n+1)
    
    prefix = 0
    for i in range(len(nums)):
        prefix += nums[i]
        prefix_sum[i] = prefix
        
    for i in range(n):
        left = (prefix_sum[i-1] if i>0 else 0)
        right = (prefix_sum[n-1]-prefix_sum[i] if i<n-1 else 0)
        if left == right:
            return i
    return -1    #return -1 if theres no pivot Index
