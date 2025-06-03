"""
Approach:
Given a string and a integer 'k' where we change 'k' amount of characters from the substring, we have to find the length of the longest substring containing the same letter.

We can simply use a hashmap to keep count of all the characters in the substring. Then we can keep track of the maximum frequency from that substring.
"""

#Simple
def characterReplacement(s: str, k: int) -> int:
    count = {}
    res = 0
    l = 0
    maxf = 0
    for r in range(len(s)):
        count[s[r]] = 1 + count.get(s[r], 0)
        maxf = max(maxf, count[s[r]])
        
        while (r - l + 1) - maxf> k:
            count[s[l]] -= 1
            maxf=max(count.values())
            l += 1
        res = max(res, r - l + 1)
    return res


"""
Optimization:
There are some very clever optimizations you can apply on the above basic solution.

First thing to be clear is that suppose we go to length of say x for observation. 
Then it is sure that its previous size x-1 was a valid size as if it wasnt the algorithm would have decreased it and we would have never got to size of x for observation.
which also implies that we cant get to the point of observing a size of x if x-1 wasnt valid at all. Same goes for x-2 to be valid for x-1 to be observed and so on.

Now lets get to the first optimization where we didnt recalculate maxf when the size of the substring was decreased. So, why did we do that?
Lets take an example! "AAABBCCD". Suppose we had k=2. The first valid size is 5 with maxf=3. thus size 5 is valid as 5-3 <= k.
As we are always looking for longer length, we will be increasing the size of the substring and thus we now have a size of 6. "AAABBC"
Now what for size 6? well 3 wont work as 6-3=3>k. so we need maxf>3 i.e wee need to be increasing maxf.
But recalculating of maxf when the size of the substring was decreased beats the whole purpose ass the maxf will either decrease or stay same in that substring decreasing case.
So we keep the maxf=3 as the minimimum standard for maxf for a new longer valid size. This forces the algorithm to search a better maxf than 3 for a longer length validation.
Thus, the maxf of the current solution acts as the boundary for the future solution's maxf which should be greater than the boundary.

This also helps you in the while loop part. How? lets undertand by continuing our example and using the old maxf statergy.
When reaching "AAABBC", we get a invalid size and thus decrease the substring by the left so we have "AABBC". 
Here size=5 and maxf=2. this will say that this substring is invalid again and we again decrease the size by 1. now size 4 and maxf 1 and thus again decreasing the size leading to size 3 and maxf=2.
Still here we dont get a bigger size and all those decreasing of size was of no use! We already knew from start that if it was invalid, 
getting a new solution from it is impossible as we are decreasing the size due to invalid case and thus getting a longer length than the past solution isn't possible.
Just decreasing the size once and brining it back to its previous valid size would have been enough!

Thats what maxf does in the new technique! as we dont change maxf and only decrease the size, 
At the first iteartion of the while loop we will be decreasing the invalid length by 1. this gives us the previous length before the invalid length.
That length is the maximum valid length till now(If confused about this statement, again read the first part of this optimization explanation "First thing to be clear is")
Now we have our maximum valid length and the maxf of it(as we havent changed maxf in the invalid case and it still remains the maxf of the previous length which is the maximum valid length till now. 
the maxf though however changes in the valid case but for in that case, we have a new solution and thus we dont have to care about the whole invalid case hassle. To learn more, read the below note:
[Note: while extending our substring, if we had found a new maxf when doing maxf = max(maxf, count[s[r]]), then there would have been no case of invalid as we are increasing length by 1 
and we have got a new maxf>old maxf. say the new maxf would be 1 higher than the old one. then, old_length+1-(old_maxf+1) = old length+old_maxf which was <k and thus if valid.
If new maxf was more higher than old one, it is more better meaning "with this new maxf, we can make a new longer valid substring with more less replacement that the previous one.
So yeah, if we found a new max_f greater than old maxf, we would have found a new solution and we then dont need to go through the whole invalid case!])

Thus we are back to our previous valid size! (Note: We wont be at the valid substring. It will just maintain the valid size. 
And its ok because we are only concerned about the size of the longest substring and not the content of the longest substring)
Another optimization here also does the same thing which is changing the 'while' statement to "if".
So though this while->if optimization isnt necessary, still its better for reading purpose as "while" statement in the code can mislead to to a multiple iteration case but in reality it runs only once.


and the final optimization! here, we dont need to calculate res = max(res, r - l + 1) for each window extend and just return r-l+1 at the end! how?
As discussed above, it we get a invalid size, then it goes back to its previous valid size. So at the end of our iteration, we will always be end at the latest valid size.

To summarize the optimization, our optimized algorithm only increase the maxf if possible (through maxf = max(maxf, count[s[r]])) and never decreases the maxf 
which makes it focus on only the valid cases and ignore every invalid case(by not updating maxf for each iteration or by removing the while loop or both)
"""
def characterReplacement(s: str, k: int) -> int:
    count = {}
    l = 0
    maxf = 0
    
    for r in range(len(s)):
        count[s[r]] = 1 + count.get(s[r], 0)
        maxf = max(maxf, count[s[r]])
        if (r - l + 1) - maxf > k:
            count[s[l]] -= 1
            l += 1
            
    return  r - l + 1
