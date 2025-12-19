"""
Approach: Given a list of numbers, return all possible permuations.
Here, we need each permuation to include all the numbers(and only once) and also the change of order of each number in the permuation will result in a new permuation!

So here we have a size constraint like of combination i.e the size of permuation should be equal to the size of the list.
And we use the constraint as our stopping condition and return the permuation made upto this point.

But we wont have any index conditiont though! Why? We will see that later on in the main logic of our recusion body.

As the order of the number matters, now a number can make permutation with its previous numbers(We cant do that in subset and combination as order doesnt matter and we assume that as a duplicate result)
So for each number, we have to start iterating from the start of the list. Thats why we dont need to pass current index for our recursion function.
What we do need a list containing a record of which indexes are used and which arent because we can use a number only once per permuation.

You might think of using a index as a decider to do so but it wont work. Suppose we use the logic "if the current index we are seeing is less than current index, its already seen",
this logic may hold true for the those deep recursive stacks where u actually used the values. But what for the origin recursive stack which we made for the current integer.
The recursion just started and we are assuming that we have used the value before it for making the permuation! So it always wont work!

Another logic you might apply is of the subset II where we sort the numbers and skip all those numbers which we decide not taking. 
But this one doesnt work at all because the concept is way different. There we were skipping the numbers of decision of not taking the number for a combination at all!
But here we have to include all numbers and the only reason we can skip a number is because we have already used it not because we decide to not use the number at all!
"""

def permute(nums: List[int]) -> List[List[int]]:
    perms, perm = [],[]
  
    def backtrack(pick):
        if len(perm) == len(nums):
            perms.append(perm.copy())
            return
          
        for i in range(len(nums)):  #For each recurstion stack, we are iterating from start
            if not pick[i]:  #pick holds True or False for each index. if that index's pick is true, it means we have already used it and we skip else we use it
                perm.append(nums[i])
                pick[i] = True  #after using the index's number in our permutation, we mark it as true
                backtrack(pick)  

                #after we finished recursing for this index, we remove it from our combination and also mark it as not picked for the fresh recursion of our next index
                perm.pop()  
                pick[i] = False
        
    backtrack([False]*len(nums))  #at start, no numbers are used. so the initial pick value for each number's index is False
    return perms
