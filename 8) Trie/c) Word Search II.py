"""
Approach: Given a m*n board containing letters and a list of words, we have to find all the words we can make from m*n board that is in the list of words.
We can move either horizontal or vertical in the board and cannot use the letter of the same position at the board twice for the same word.
So for each move we make, checking if that move makes us near to any of the word in the the list of words, it becomes redundant to check. So thats why we build a prefix map.
In this way we dont have to go through each word and only go to the specific branch in the prefix tree that is containing the letters of the word we made. If no such branch
then we can say that no word can be made by the move and we backtrack to the previous move. Also if we already found a branch that already matched with a word in the board,
we start removing the letter of the word in the prefix tree from the end and continue removing all such letters which lead only to that previous answer.
For eg: If we get a answer: apple, we first remove e. now we backtrack to l and check if l has any other childrens left after the deletion of e. If not it means that l 
contained only one answer and that was with e after it. So we even remove l and then backtrack up so on. This is known as pruning. It removes redundant moves/paths.
If we know that the second p in the 'apple' only leads to p->l->e which is the answer we already got and doesnt lead to any other new words, then why even check that path!
We wont be getting any new answers from there. This makes our search faster. 
Moreover, this applies to a unsuccesfull branch too! If the branch was unsucessfull in making a word, we go on removing nodes from the branch which only leads back to failure.

"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None
        
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        #Building the prefix tree 
        root = TrieNode()
        for word in words:
            curr = root
            for ch in word:
                if ch not in curr.children:
                    curr.children[ch] =  TrieNode()
                curr =  curr.children[ch]
        	curr.word = word 	#Here we have to return the word as answer after finding the word. so saving the whole word at the end so it becomes easy to return the answer

        rows, cols = len(board), len(board[0])
        result = []

        """
        We use a recursive function so that we can navigate through all moves. We pass on r,c for giving the current letter we got from the move we made
        and also give node to give reference of where we have reached in the prefix tree after all the successfull moves. Note that the letters should be in order
        to make the corresponding word. So its really important to keep track of what letter we got from our current move and where we are at in making our word
        after all the previous moves.
        """

        def dfs(r, c, node): 
            if r < 0 or c < 0 or r >= rows or c >= cols: #If we get any invalid position while moving, ignore it
                return
            
            ch = board[r][c]

            """
            '#' is used to denote that the letter has already been used for the same word. So cant use it again. So we backout from this move
            if the letter we got from the current move is not there after the previous letter in the prefix tree, 
            we cant form any such word with this current letter that is in the list of words. So we backout from this move
            """
            if ch == '#' or ch not in node.children: 
                return

            """
            after being sure that our current move is valid, we set the letter we got from the move as the current node in the prefix tree so to check
			the next move's letter with our current letter. But before that, we check that if the node is the last node in that branch. If yes we got our answer,
			so we append it to the result and set its word value to None so that we dont create a duplicate answer. Also if this node doesnt have any children meaning
			it doesnt create any new words after it, we can simply remove it as it only leads to the duplicate answer(which we will be doing in pruning)
            """
            next_node = node.children[ch] 

            if next_node.word:
                result.append(next_node.word)
                next_node.word = None   # avoid duplicates

            board[r][c] = '#' #Setting character of this position as "#" so that we mistakely dont use it again for the making of same word 

            #now we try on different moves for continuing our process of making that word
            dfs(r + 1, c, next_node) 
            dfs(r - 1, c, next_node)
            dfs(r, c + 1, next_node)
            dfs(r, c - 1, next_node)

            """
            when we reach this point, we have tried every single way to try to make the word from the character we intially started it. So now we set it back to its
			original value so that it can be used when making a new word
			"""
            board[r][c] = ch

            """
            Now we do the pruning process as mentioned above. If a node has no children, meaning it leads to no further new words and it itself is not a word
         	(Happens if it was not a word from start or was first a word but then we got answer from that and now set it as not a word to not get duplicate answer),
         	then that node is useless so we just remove it i.e remove the children list of its parent node
            """
            if not next_node.children and next_node.word is None:
                del node.children[ch]

        #We try making a word will each letter present in the board
        for r in range(rows):
            for c in range(cols):
                if board[r][c] in root.children: #If only if there is a word in the list of words that starts with the letter, we try making a word out of it
                    dfs(r, c, root)

        return result
