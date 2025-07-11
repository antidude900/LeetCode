"""
Approach:

"""

def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    A = nums1 if len(nums1)<len(nums2) else nums2
    B = nums1 if A != nums1 else nums2
    total = len(A)+len(B)
    half = total//2
    l,r = 0, len(A)-1
    
    while True:
        midA = (l+r)//2
        midB = half-midA-2 
      
        Aleft = A[midA] if midA>=0 else float("-inf")
        Aright = A[midA+1] if midA+1<len(A) else float("inf")
        Bleft = B[midB] if midB>=0 else float("-inf")
        Bright = B[midB+1] if midB+1<len(B) else float("inf")
      
        if Aleft<=Bright and Bleft<=Aright:
            if total%2 == 0:
                return (max(Aleft,Bleft)+min(Aright,Bright))/2
            else:
                return min(Aright,Bright)
            
        elif Aleft>Bright:
            r = midA-1
        else:
            l = midA+1
