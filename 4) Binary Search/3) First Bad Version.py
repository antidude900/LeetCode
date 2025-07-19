"""
Approach:
Given a API isBadVersion() and an array of versions, we have to find the first bad version.
For this we will be applying the binary search. Until a bad version is found, we only update the left pointer.
Why? Because if the mid doesnt contain bad version theres no way that the down ones are the bad versions. So we update the elft pointer to see after that mid.
And when there is bad version, we store it and then start seeing down to it if there is any more bad version. So we update the right pointer.
However, we even dont need to store that bad version explictly. 
When there is no further bad version, the left will reach the right and the mid being right, we will be doing left=right+1 which reaches the bad version.
This is done using the fact that the right will be just left to the earliest bad version(if any).
But this fails when there is no bad version at all(However this could also be fixed my putting a edge case at the end)
"""

def firstBadVersion(n: int) -> int:
    left = 0 
    right = n
    res = 0
    while (left<=right):
        mid = left+(right-left)//2
        
        if isBadVersion(mid):
            right = mid-1
        else:
            left = mid+1
    
    return left
