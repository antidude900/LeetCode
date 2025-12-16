"""
Approach: Given a list of numbers which may contain duplicates, we have to find all possible subsets from them.
Its same as the Subsets problem. But the only thing thats different is that we now have duplicates in the list and nwo there comes another case to handle so that we dont create mutliple same outputs.
(Yeah one way would be just to make the list containing all the subesets as a set. But still it wont solve the reduncancy of doing a process resulting a already got output. For efficiency, its better to not do the process at all!)

But lets see before how this can cause in the making of duplicate outputs:
Say we have [1,2,2,3]. And we chose not to take 2 at the 2nd layer. This leads to one of the subsets: [1,2,3] in the 4th layer. But this same output can be achieved at the 4th layer again but taking 2 in the second layer.
So how do we solve the problem? Well if we are saying that if we are not taking 2 at the 2nd layer, the for that branch formed we wont be taking any 2 at all at any depth of the branch! 
which means that the decision of not taking 2, does applies for any other further decision for that branch at other layers too. Now we wont be getting [1,2,3] in the 4th layer.

But a confusion might come and you may ask "What if we need the second 2 and not the first 2? It wont even be possible as we are always removing the second 2 while removing the first one!"
The simple thing is that the position of 2 doesnt matter! What matters is that we have 2 or not. So the "What if we need the second 2 and not the first 2?" meaning having only one of the two which leads to the answer: 
[1,2,3] is simply given by the branch taking the 2 at the second layer and then not taking at the 3r layer which can give a output: [1,2,3] at the fourth layer! 

So yeah, though it might feel that removing all the occurence of a number in any layer for that branch when once decided to not use that number in a layer might lead to losing some of the output, still those outputs will be
achieved from the other branch where we decided to take that number. For sure, the output wont be achieved from the number of the specific index we want, but it doesnt matter which index's number we use to make the number if both the 
index's number are same!
"""

def subsetsWithDup(nums: List[int]) -> List[List[int]]:
    subsets, currset = [], []
    nums.sort()  #sorting the list so that we can check if the number at the next layer is same as the number in the first layer
  
    def backtrack(i):
        if i==len(nums):
            subsets.append(currset.copy())
            return 
        
        currset.append(nums[i])
        backtrack(i+1)
        currset.pop()
      
        while i+1<len(nums) and nums[i] == nums[i+1]:  #if we are deciding to not use the number at the current layer, we wont be using that number in any layer at all for the branch
            i+=1
        backtrack(i+1)
      
    backtrack(0)
    return subsets
