"""
Approach:
We are given a string which contains just the characters: '(', ')', '{', '}', '[' and ']'. We have to check if the Paratheses placement is valid or not.
Lets use stack to keep track of their position!
For opening parentheses, we simply add it to the stack. The real fun comes for closing parentheses!
We first make a hashmap to map every closing paretheses with itrs opening one.
Then if we encounter one, then we check if the top of the stack matches with the opening parathesis of it or not?
If yes, we found a pair which is valid and thus pop out that opening paranthesis from the stack.
Else, its valid because we cant have the a closing bracket come which doesnt match the latest opening bracket! 
"""

def isValid(s: str) -> bool:
    stack = []
    closeBrackets ={')':'(','}':'{',']':'['}
    for c in s:
        if c in closeBrackets:
            if stack and stack[-1] == closeBrackets[c]:
                stack.pop()
            else:
                return False
        else:
            stack.append(c)
    
    return True if not stack else False
