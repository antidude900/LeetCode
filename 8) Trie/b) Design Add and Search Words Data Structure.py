"""
Approach: Here, for making a add and search words data structure, we do the the same implemenation as the Trie and use add and search of it.
But theres a catch! This version also allows "." which this character can be matched to any letter. So we just need to adjust the search functionality.

'.' makes the traverse a bit complex. Now we have to go through all the childrens of the current node because all the childrens satisfy as the next letter because of '.'
But the traversal is same for each children so we can just use just run a recursive function. 
The recursive function is given a index which denotes the current place of the target word we are in rn. We also pass one of the node to start traversal from that node.
(Initially we start from index 0 and the root node)
so now we start searching for letters of the word starting from the given index. If the character is not a '.', then we handle it like we handled it in our normal trie search.
But if its a '.', we then pass all the children node of the current node to the recursive function to check if any branch fulfills the search. The search is fulfilled if
any of the branch ends succesfully as a full word. If any branch succeed, then we go backtracking upto the first "." (returing all Trues). 
But if none of the branch succeed, then we backtrack upto the latest "." (returing all False) and not the first "." because that branch failed but other branch might succeed.
"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.endOfWord = True

    def search(self, word: str) -> bool:
        def dfs(i,root):
            curr = root
            for j in range(i,len(word)):
                c = word[j]
                if c == ".":
                    for child in curr.children.values():
                        if dfs(j+1,child):
                            return True
                    return False
                else:
                    if c not in curr.children:
                        return False
                    curr = curr.children[c]
            return curr.endOfWord
        return dfs(0,self.root)

#Stack Version (Just replicating recursion in stack to reduce overhead, but not alot much faster than the recursion one)
class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.word = True

    def search(self, word: str) -> bool:
        stack = [(0, self.root)]

        while stack:
            idx, node = stack.pop()
            if idx == len(word):
                if node.word:
                    return True
                continue
                
            ch = word[idx]
            if ch == '.':
                for child in node.children.values():
                    stack.append((idx + 1, child))
                continue

            if ch in node.children:
                stack.append((idx + 1, node.children[ch]))

        return False


