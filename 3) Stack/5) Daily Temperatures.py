"""
Apporach:
Given an array of temperatures, we have to return an array in which the ith position holds the no of days we have to wait after the ith position in the given array to get a warmer temperature!
We can use a stack to keep the record of each of the tempearture whose days have not been found. 
Now should we keep the higher in the top or bottom? Well think of this. So lets take a example for both cases where the new temperature is smaller than the top.

As its a case where we dont find the result, we expect to handle this case in minimum effort. So lets see which way will help us achieve this!
Suppose we keep the higher at top. We know the new temperature is small than the top one, but we cant be sure if its less than the elements below top!
So we have to check for others too and thus we dont handle the case in minimum effort!

But if we keep the lower temperature at top and the new temperature is less than the top one, than it will be for sure less than the others below it too! 
Here we handled this case in minimum effort so we will do this way. For the new temperature which is bigger than the top, 
we go on popping(as we found the higher temperature and thus can now calculate the result) until we reach the top which is greater than the new temperature.
"""

def dailyTemperatures(temperatures: List[int]) -> List[int]:
    stack  = []
    n = len(temperatures)
    ans = [0]*n
    for i in range(n):      
        while stack and temperatures[i]>temperatures[stack[-1]]:
            prev_i = stack.pop()
            ans[prev_i] = i-prev_i
        stack.append(i)
    return ans
