"""
Approach:
Here we just have to find a index for which the sum of elements left to it is equal to the sum of elements right to it

For this we simply calculate pivot_sum like before and then check:
if the prefix sum of the element just left to that index i.e the sum of all the elements left to it
is equal to
the sum of remaning elements to the right i.e prefix_sum[index_of_last_element]-prefix_sum[index_observing_rn] 
"""

def pivotIndex(self, nums: List[int]) -> int:
    prefix  = 0
    prefixSum = []
    
    for num in nums:
        prefix+=num
        prefixSum.append(prefix)
        
    for i in range(len(prefixSum)):
        left = prefixSum[i-1] if i>0 else 0
        right = prefixSum[-1]-prefixSum[i]
    
        if left==right:
            return i
    return -1
