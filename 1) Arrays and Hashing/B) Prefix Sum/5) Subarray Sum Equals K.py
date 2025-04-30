"""
Approach:
Tommorow
"""

def subarraySum(nums: List[int], k: int) -> int:
    res = 0
    currentSum = 0 
    prefixSum={0:1}
    for num in nums:
        currentSum+=num
        diff = currentSum-k
        res += prefixSum.get(diff,0)
        prefixSum[currentSum] = 1+prefixSum.get(currentSum,0)
    return res
