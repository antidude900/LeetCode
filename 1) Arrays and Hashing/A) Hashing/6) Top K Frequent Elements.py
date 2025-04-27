"""
Approach:
We just have to give the top k most frequent elements.
For this: we first count the frequency of each element(using heap for faster access the previous value to increment or use the collector library)
[in my case, i found that collector library decreases efficiency]
Then, we just need to sort according to the frequency(in descending order for highest to come first) and then return the the first k of those
I used various sorting algorithm such as tim sort, heap sort and heap sort with limit of k and here are the results:

Heap sort with limit of k did well than simple heap sort but the tim sort did the best!!!
So i will use tim sort but i will list the other two as well.
"""

  
