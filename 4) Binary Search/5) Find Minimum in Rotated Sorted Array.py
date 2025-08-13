"""
Approach:
Given a sorted array but rotated any no of time, we have to find the minimum element.
For this we can take still use the sorted property. 
For eg: If the mid is greater than the element towards its right, it means its the number from the rotated part as in a sorted array in ascending order, the before element cant be greater than the after one.
So we dont need to see the left part of the mid because all of those part are rotated part too. So we only see the right half.
If the mid is less than the element towards its right, then it is in sorted order meaning its not of the rotated part. So we can be asuured that all the elements between will also be less.
But why are we checking to its right? well because the elements are being shifted from the right.
if we had done nums[m]>nums[l]: r = m, it will find the minimum for the rotated part which infact wont have the minimum. 
so u might think l=m to remove the rotated part but what if the array is rotated back to its fully sorted form. then instead of eliminating the roatated part, you are eliminating the part having minimum!
Hence its always to check from the right as it will start finding minimum from the non rotated part and also if not rotated at all it is shifting towards the left surely giving us the minimum.
So the left pointer may be of the rotate or not rotated part and thus according to that the condition changes but the right pointer is for sure to be of the non rotated part and thus it can be handled by 
a single condition
To conclude, its better to check from right and shift towards left rather than checking from left and shifting towards the left
(shifing towards the left is always a good idea as the array is sorted and hence the minimum will be at its left)
So we dont have to see the right half and we just see the left part(because we might have took mid between in the sorted portion meaning there can me more less ones in the left)
"""


def findMin(nums: List[int]) -> int:
    l, r = 0, len(nums) - 1
    while l < r:
        m = l + (r - l) // 2
        
        if nums[m] < nums[r]:
            r = m    #dont take r=m-1 like in first bad version because there we just needed a range to search. 
                     #so the r=m-1 and r=m really didnt mean anything as we could tune the range for both of them to be between l to m(exclusive) by the while loop (l<=r for r=m-1 and l<r for r=m)
                     #But here r=m-1 and r=m do mean alot because we take their value for comparision. because we to find another one less than the mid one not than the mid-1 one.
                     #for eg: [3,1,2] in the second pass we have to compare 3 and 1 for least one but if we did r=m-1, we would have been comparing 3 with itself.
        else:
            l = m + 1    

    return nums[l]
