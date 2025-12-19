"""
Approach: Given a list of numbers and a target k, we have to find all possible combinations of the numbers which result to a sum = k. You can use a number only once per combination and there are duplciate numbers too!
This is a same problem as our Combination Sum problem but here we can only use a a number only once! So if we just do i+1 int the next recursion stack of our decision of taking number in index 'i' right?
Yeah, thats enough for a number only one constraint(understand that we are saying a number of a specific index once, so we can again use the number if it comes in another index)
But we also have a new problem of having duplicate numbers! But this a problem we have solved earlier too in the subset II!
Yeah so when we decide to not use a number, we simply skip all the ocurrance of that number so that we wont get the same answers again! 
For this we sort the list so that all same occurance becomes consecutive and our iteration logic becomes simpler.
"""

def combinationSum2(candidates: List[int], target: int) -> List[List[int]]:
    combs, comb = [],[]
    candidates.sort()
    def backtrack(i,total):
        if total == target:
            combs.append(comb.copy())
            return 
        if total>target or i==len(candidates):
            return 
        
        comb.append(candidates[i])
        backtrack(i+1,total+candidates[i])
      
        comb.pop()
        while i+1<len(candidates) and candidates[i] == candidates[i+1]:
            i+=1
        backtrack(i+1,total)
      
    backtrack(0,0)
    return combs
