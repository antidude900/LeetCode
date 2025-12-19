"""
Approach: Given two integers n and k, find all possible combinations of size k where u can use numbers ranging from 1 to n.
A combination problem is simply like a subset problem. the only thing that differs is the size constraint. There is size constraint in combination that every combination has to be a specific fixed size.
But in subsets, the size of every subset may differ from each other and thus there is no size constraint.
So the only stopping condition in subset was the depth i.e the index. If the index reaches the end of the choices we can use, then we simply stop the recursion and return the subset we have made till now.
For the combination, one of the stopping condition is simply the same as the subset but we dont return the combination at this point and just backtrack to the previous recursion function calling it.
The second stopping condition is that the length of the combination reaches size k and yeah here we return the combination we have made till now!

As combination is just a special case of subset, every other things we do are the same
"""

def combine(n: int, k: int) -> List[List[int]]:
    combs, comb = [], []
    def backtrack(i):
        if len(comb) == k:
            combs.append(comb.copy())
            return 
        
        if i>n:
            return 
        
        comb.append(i)
        backtrack(i+1)
        comb.pop()
        backtrack(i+1)
    backtrack(1)
    return combs
