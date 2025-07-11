"""
Approach:
Given two arrays both sorted in ascending order, we have to find the median of the combined array. So yeah we can just combine both the arrays in a single array and then find median.
But the question asks for log time. Thus using binary search will the best. But using binary search for what?
We use binary search for finding the mid of one array such that we find mid for another array and thus the left and right parts of both the arrays are the portion of the left and right part
of the combined array.

But how do we do that. well say total be the size of the combined array. so while dividing the array to two parts, we get left part of size half = total/2
now we take the smaller array among the two and then find the mid for that array. thus the left section for that array will be of size midA+1
and hence the size of the left portion we have to make from the larger array will be of size half-(midA+1) and its mid index will be half-(midA+1)-1 = half-midA-2
Now after finding mids for both the arrays we have to verify if this left portions really works to make a combined left portion.
For that we have to check for both the left portion if their greatest number is smaller than the least number of the right portion of the another array.
If yes, their mergining wont conflict with each other's right portion(meaning it will still be sorted) and thus the combined left portion will be valid.
The remaning portions from both sides will be the right portion. 

Now, we find median. if odd total length, the median falls towards the right section as the left portion size is taken as the floor half of total(so the right will contain more values)
If even length, both will be of same size and the numbers contributing to the medain falls on both the portion(highest of left and lowest of right)
Also to update the pointers, we update them such that it brings us closer to satisfying the condition of validation.
"""

def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    A = nums1 if len(nums1)<len(nums2) else nums2    #let the smaller array to be A
    B = nums1 if A != nums1 else nums2    #and bigger array be B
    total = len(A)+len(B)
    half = total//2
    l,r = 0, len(A)-1    #pointers to find the mid of A
    
    while True:
        midA = (l+r)//2    
        midB = half-midA-2 
      
        Aleft = A[midA] if midA>=0 else float("-inf")    #suppose no section of A will serve in the left section of combined, then r will get less that 0. 
                                                         #and then we have to set the left portion for A as -inf to validate the check condition: Aleft<=Bright
        Aright = A[midA+1] if midA+1<len(A) else float("inf")    #suppose all section of A will serve in the left section of combined, then l will get equal to the total size of A. 
                                                                 #and then we have to set the right portion for A as inf to validate the check condition: Bleft<=Aright
        Bleft = B[midB] if midB>=0 else float("-inf")    #similar as the corresponding case
        Bright = B[midB+1] if midB+1<len(B) else float("inf")    #similar as the corresponding case
      
        if Aleft<=Bright and Bleft<=Aright:
            if total%2 == 0:    
                return (max(Aleft,Bleft)+min(Aright,Bright))/2    #if even, max from the left portion and min from the right portion will contribute to the median
            else:
                return min(Aright,Bright)    #if odd, only the min of the right portion will contribute to the medain
            
        elif Aleft>Bright:    #if the highest number of the left portion of A is greater than the right portion of B, we cannot take it in the combined left portion. 
                              #thus we update r = midA-1 to find a smaller highest number for the left portion of A which may sastify the condition
            r = midA-1
        else:    #and if the highest number if the left portion of B is greater than the right portion of A, we cannot take it in the combined left portion. 
                 #thus we update l = midA+1 to find a higher highest number for the left portion of A thus also increasing the min of the right portion which may sastify the condition
            l = midA+1
