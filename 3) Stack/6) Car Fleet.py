"""
Approach: We are given two arrays, one for the position of the car and another for the speed of the car(same index between the two arrays represents the position and speed of a car)
Now we have to see how many fleet reach the target. When a car has to overtake another car, then they become a fleet(as we cant overtake as we have a 1D path)
and so they reach the target at the same time

So where to start observing from. from the lowest position to the highest position or vice versa?
Well if we start seeing from the lowest position and thus we start comaring it to its ahead one, it might give a wrong result!
Because the speed of the car ahead might decrease because it has to overtake the car ahead of it! 
But as we havent done that calculation, we will only be working with its original speed and thus can lead to mistake!
So we have to go from the highest to the lowest calculating time for each(time = (final-intial)/speed)
If they lower position reach in lower lime than higher position, then they become a fleet and thus reach at the time by higher position!
So the next lowest position time is to be compared with that higher position!

We can thus first sort the position and then for each position which reaches in lower time than their higher one is appended to the stack as a seperate fleet(as it didnt combine with the higher one)
"""

def carFleet(target: int, position: List[int], speed: List[int]) -> int:
    car = [(p,s) for p,s in zip(position,speed)]
    car.sort(reverse=True)
    stack = []
    for p,s in car:
        time = (target-p)/s
        if not stack or time>stack[-1]:
            stack.append(time)
    return len(stack)

#But one thing you may have realized it all this moment we just are playing with the top value of the stack. so why not store the top value as a variable rather than making a stacl!
#this will save the overhead time to build and operate the stack and also save memory!
#Another optimization we can do is that we can sort the index according to the position it holds rather than sorting the whole tuple containing (position,speed)
#Same optimization could have been done for the stack one too! hahaha! thats why see other solutions too if your didnt do that good!

def carFleet(target: int, position: List[int], speed: List[int]) -> int:
    idx = sorted(range(len(position)), key=lambda i: position[i])
    fleet = 0
    prev_time = 0
    for i in idx[::-1]:
        time = (target-position[i])/speed[i]
        if time>prev_time:
            fleet+=1
            prev_time = time
    return fleet
