"""
Apporach:
In this question, we are given a interget say 'n' which denotes the pair of paranthesis we are given. Now using those paranthesis,
we are required to generate all combinations of well-formed parentheses.

There are two rules you should know before starting to form them:
1) As there are 'n' pair of paranthesis, there are 'n' open brackets and 'n' close brackets because each pair has a open bracket and a close bracket.
2) In the process of forming a valid combination, we need to make sure that in each iteration we dont have closing brackets than open brackets as that is already invalid!

Following these rules, we recursively increase the open and close brackets until we have used all of those open and close brackets.
"""

def generateParenthesis(n: int) -> List[str]:
    stack = []
    res = []
    def backtrack(openN,closeN):
        if openN == closeN == n:
            res.append("".join(stack))
            return
          
        if openN<n:
            stack.append('(')
            backtrack(openN+1,closeN)
            stack.pop() #poping is important to remove the changes we have done in one branch of recursion so that the another branch of recursion dont get affected 
                        #(as the branches have different stack strucure)
        
        if closeN<openN:
            stack.append(')')
            backtrack(openN,closeN+1)
            stack.pop()
            
    backtrack(0,0)
    return res
