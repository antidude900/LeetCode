"""
Approach: Here instead of the size 'k' being the constraint for the combination, the sum of the elements in the combination is the constraint where they have to be target.
So we replace our previous primary stopping condition with this new constraint and for sure the index stopping condition remains the same.
Also a new stopping condition can be added ! If the sum of our combination gets greater than the target, we need to stop because there are no negative integers in the given choices;
So its fixed that the sum will get more bigger and wont ever be equal to target. 

And instead of doing the sum of the list everytime, we can just pass the previosuly calculated sum and then further modify it in our new recursion stack as needed and keep on passing it!
"""

def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
    combs, comb = [],[]
    def backtrack(i,total):
        if total == target:
            combs.append(comb.copy())
            return 
          
        if total>target or i==len(candidates):
            return 
        
        comb.append(candidates[i])
        backtrack(i,total+candidates[i])  #If we are including the current index's number in the combination, we add it to the sum
      
        comb.pop()
        backtrack(i+1,total)  #else we dont add it
      
    backtrack(0,0)  #the initial sum is 0
    return combs
