"""
Approach:
Here, we have to find three numbers which give sum of 0
Its very simple!(But the edge cases are daunting!) First we take a number say val. Then apply 2 pointer for the sorted array finding the remaining two values!
(As we need to find the total which includes the 3 values which results to 0, be sure include val in the sum of two pointer as well)
"""


def threeSum(nums: List[int]) -> List[List[int]]:
    triplets = []
    nums.sort()
    for i, val in enumerate(nums):
        if val>0: 
            break    #This optimization is done to avoid searching if it is guarenteed theres no three sum
                     #can three positive values sum return 0? No!(If you say, if all 3 are 0 then its possible. But 3 is neither positive nor negative)
                     #So we atleast need one of the value to be negative! And then we apply two pointer for the rest array
                     #suppose while iterating through all the non-positive numbers of the array we still didnt get any solution! This means theres no solution at all!
            
        if i>0 and val == nums[i-1]:    #we will evaluate all the possible solutions where val is in the solution, so theres no need to check it again!
            continue
        
        left,right = i+1,len(nums)-1 #apply two pointer for the lest of the array
        while left<right:
            total = val+nums[left]+nums[right]
            if total == 0:
                triplets.append([val,nums[left],nums[right]])
                left += 1 #after finding one solution, still there might be other. so wee keep on finding others
                          #you might think there might be another soltuion with the same left
                          #but having two same values i.e val and left, we cannot expect another different number to give us the solution.
                while (nums[left] == nums[left-1] and left<right):    #heres the same thing as above! if the new left is same as the previous left, the above problems arises again!
                    left+=1
            elif total>0:
                right-=1
            else:
                left+=1
    return triplets
            
