"""
Approach:
Here we just have to make a stack with the basic functionalities like push,pop,top and one extra function of getting the min from the stack.
Getting min might not seem that difficult if we just make a min property to keep track of the minimum while every element is pushed.

But theres more to it! What if we pop the minimum element? You might say ok, then i will keep track of the second minimum element!
But what if we pop the second miniumum element? You see? This apporach will require you to keep track of first,second,third,...and so on!

There is a better approach to it! Its similar to the upoone where we have to keep track of multiple minimum element,
But not the first second third minimum element for each push but rather only the most minimum element for each push!
We will be making another stack with to which for every push for the main stack, we will be pushing it in the min stack if the new element is the new min
This way though we pop out the minimum element, we will be having the record of which was the minimum element before it was pushed!

Another way is using maths! Instead of keeping the element itself in the stack,we keep its difference with the current non-updated min element(explained later)
So to get the real value, we just do val = diff + min (as we did diff = val - min to store the value)
But what about keeping track of the change in the minimum? It is necessary to find out the new min if the current min gets popped.
Lets take a example: [5,3]. At first min is 5. After 3 comes, we upload 3-5(diff = val-min) giving us -2. 
So a negative diff will denote that new min came after the new element and thus the new min is the new element itself.
But ok, how to calculate the prev min, its easy! As we did diff = new_min-prev_min, we get prev_min by: prev_min=diff+new_min.

However the two stack is faster than the math one. it might be because its faster to just push and pop a element in the stack rather than performing mathematical operations!
"""

#Two Stack
class MinStack:

    def __init__(self):
        self.stack = []
        self.min = []

    def push(self, val: int) -> None:
        if not self.min or val <= self.min[-1]:
            self.min.append(val)
        self.stack.append(val)

    def pop(self) -> None:
        val = self.stack.pop()
        if self.min and self.min[-1] == val:
            self.min.pop()

    def top(self) -> int:
        if not self.stack:
            return None
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min[-1]

#One Stack With Maths
class MinStack:
    def __init__(self):
        self.min = float('inf')
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(0)
            self.min = val
        else:
            self.stack.append(val - self.min)
            if val < self.min:
                self.min = val

    def pop(self) -> None:
        if not self.stack:
            return
        
        pop = self.stack.pop()
        
        if pop < 0:
            self.min = self.min - pop

    def top(self) -> int:
        top = self.stack[-1]
        if top > 0:
            return top + self.min
        else:
            return self.min

    def getMin(self) -> int:
        return self.min
