"""
Approach:
Koko has 'h' hours to eat piles of banana. She can only choose to move on next pile in an hour interval(cannot go in between)
Now we have to find the minimum integer speed 'k' with which she can each all the pile of banana in 'h' hours.

As Koko speed should be a integer, the minimum speed she can go with is 1. 
Also the first minimum speed its guarenteed to finish with is the maximum size of pile in the piles. 
Because if she can finish the maximum size pile in a hour, it can finish piles of length n in n hours.
And as given hours>=length of piles, i.e minimum given hours is 'n', it is guarented to finish the piles.
Note: If given hours< length of piles its impossible to finish the piles. because to go from one pile to another, we can do only in an hour interval. 
So though how much fast we finish a pile, we wont be able to navigate through all piles!
"""

def minEatingSpeed(piles: List[int], h: int) -> int:
    left = 1
    right = max(piles)
    while left<=right:
        k = left+(right-left)//2
        totalTime = 0
        for pile in piles:
            totalTime+=math.ceil(pile/k) #can only go to next pile in a hour interval. So though we take 1.3 hours to complete a pile, we can go to next pile when its 2 hours.
        if totalTime<=h:
            right = k-1
        else:
            left = k+1
    return left
