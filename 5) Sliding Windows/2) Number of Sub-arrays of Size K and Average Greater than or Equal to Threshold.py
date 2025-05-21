"""
Approach:
Given an array, we have to find the no of subarrays of size 'k' whose average is greater or equal to the given threshold.
Now hearing about subarray which is contiguous and has a fixed size, sliding windows is the best technique that follows those constraints!
For the average, we keep track of the sum in the sliding window and when the sliding window slides/moves, we remove the past one and add the new one from the window.
"""

def numOfSubarrays(arr: List[int], k: int, threshold: int) -> int:
    #initializing our sliding window fully filled
    target = k * threshold    #converting the search for average to search for some as: sum = average*n. But if want to do with average, then we have to do window_sum/k for each check.
    window_sum = sum(arr[:k])    #first k elements sum
    count = 1 if window_sum >= target else 0
    
    for i in range(k, len(arr)):    #iterating starting from the element just after the initial window
        window_sum += arr[i] - arr[i - k]    #adding the current one in the sum and removing the first item in the window as now the window is slided
        if window_sum >= target:    
            count += 1
    return count
