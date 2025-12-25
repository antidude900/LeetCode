"""
Approach: Given a m*n grid of characters, we have to find if a given word exists on the grid or not.
For this, we just check everytime if the current character we have in the grid rn is present in the current index of the word. If yes, we go on adding more characters to it from there 
otherwise we go back to the previous charater and try adding new characters to it.  Also for the previous character, we mark it as '.' in the grid so that we know that we have already used that in our word
and cant use again in the same word formation where the previous character is used. 

This is enough for the soultion. But we can add some optimizations.
1) If the len(word) is greater than the total no of characters in the grid, we cannot make the word at all. So we already know that the word doesnt exists in the grid at all.
2) If we start searching from a character that appears many times in the word, the search may begin from many places on the board only if that character is also common on the board. 
In that case, the algorithm starts many paths that seem valid at first, but fail later when a more restrictive character cannot be placed next to them. This causes a lot of wasted time.
To reduce this, we reverse the word so that the search starts from a character that appears fewer times in the word. Fewer occurrences usually mean stricter placement rules, so wrong paths fail earlier.
This heuristic helps mainly when a frequent character in the word is also frequent on the board. If that character is not common on the board, the search already stops early and there is no major inefficiency. 
In that case, reversing the word does not help much, but it also does not make things worse.

Moreover; we can implement board count instead of word count and check if the first letter appears more in the board more than the last one (in that we reverse). But its computationally expensive whereas word count
is already a very good heuristic evaluation which is cost efffective and also reduces the rutime by a sigificant amount. 
"""

def exist(board: List[List[str]], word: str) -> bool:
    ROWS, COLS = len(board),len(board[0])
    if len(word)> ROWS*COLS:
        return False
    def backtrack(r,j,i):
        if i == len(word):
            return True
        if r<0 or j<0 or r == ROWS or j == COLS or board[r][j] == "." or word[i]!=board[r][j]:
            return 
    
        board[r][j] = "."
        res = backtrack(r+1,j,i+1) or backtrack(r-1,j,i+1) or backtrack(r,j+1,i+1) or backtrack(r,j-1,i+1) #If one of them passes, meaing the word exist and we can stop our search
        board[r][j] = word[i]
        return res
        
    count = Counter(word)
    if count[word[0]]>count[word[-1]]:
        word = word[::-1]
    
    for r in range(ROWS):
        for j in range(COLS):
            if backtrack(r,j,0): return True         
    return False
     
        
