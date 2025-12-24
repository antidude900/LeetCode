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
        res = backtrack(r+1,j,i+1) or backtrack(r-1,j,i+1) or backtrack(r,j+1,i+1) or backtrack(r,j-1,i+1)
        board[r][j] = word[i]
        return res
    count = Counter(word)
    if count[word[0]]>count[word[-1]]:
        word = word[::-1]
    
    
    for r in range(ROWS):
        for j in range(COLS):
            if backtrack(r,j,0): return True
    return False
     
        
