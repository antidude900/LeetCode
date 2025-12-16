"""
Approach: Given a list of numbers, we have to find all possible subsets from them. 
For this, we can use recursion as step for making subset from each element is the set. We start from a index 'i' and start making a set with index after it: i+1,i+2,... until we reached the end of the number.
After that, the set is appended to the full list of subsets. Now we make a set not including the index 'i'. Note that this process of not taking the index also applies for the first recursion we started with index 'i' where we might
not take i+1 ot i+2 or both! Note that the current index can go to index after it for making a subset and cant go backwards i.e to the index before it to avoid any duplicates.
We can visualize all of this as a binary tree! Each index has its own layer and in that layer we decide to either add the value at that index to the subset or not. So we make two different branches for each node. It looks something like this:
          []
        /    \
      [1]    []
     /  \    /  \
 [1,2] [1] [2]  []

 Note that we got 2 subsets at the first layer [1] [0] i.e 2^1 and then for each such subset we make two branches. So the number of subsets made in the next layer i.e the 2nd layer becomes 2*2 = 2^2. SImilarly if there was another number say 3
 then there would have been a 3rd layer where for each subset in the 3rd layer we make two branches so we will have 2*2*2=2^3. So the total no of subsets we get at the end is 2^n where n is the no of layer i.e the no of elements in the list.

An output can have max n elements. So to handle/process the output, we require O(n) time complexity. So for all the outputs i.e 2^n outputs, we require a total time complexity of n*2^n
"""

def subsets(nums: List[int]) -> List[List[int]]:
    subsets, currset = [], []  #subsets storing all possible state
                               #current set for a specific branch(new elements get added while going more deep into a branch and the number that was added in a layer is removed when backtracking out of the layer to the upper layer)
    def backtrack(i):
        if i==len(nums):  #after the last layer i.e we seen all elements and now have got the output for that specific branch
            subsets.append(currset.copy())
            return 
        
        curret.append(nums[i]) #In the layer, this is the branch taking the new element coming at that layer
        backtrack(i+1)
        currset.pop()  #removing this number we just put in the current set so that we can make new set for other branche
      
        backtrack(i+1)  #In the layer, this is the branch taking the new element coming at that layer
    
    backtrack(0)
    return subsets
