"""
Approach:
A very easy question! We just have to evaluate the reverse polish notation aka the postfix expression where the operators are written after the operands.
So, we need to build a stack where we put operands. After a operator is found, we need to pop out two elements from the stack say A and B(A is at top and B after it)
Then we need to do B operator A and then again push it to the stack. The final remaining number at the stack is our evaluated result!
"""

def evalRPN(tokens: List[str]) -> int:
    stack = []
    res = 0
    ops = {    #instead of this we could also have simply made a list of operators and then used if elif for carrying out the operation 
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: int(a / b)  
    }
    for token in tokens:
        if token not in ops:
            stack.append(int(token))
        else:
            val1 = stack.pop()
            val2 = stack.pop()
            res = ops[token](val2,val1)
            stack.append(res)
    return stack[-1]
