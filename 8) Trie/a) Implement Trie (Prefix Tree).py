###
Approach: A Trie is simply a binary tree used to store strings where each letter of the string is treated as a node.Due to the tree traversal it makes the string search faster. 
But we already have hashset for that then why need Trie? Well because we cant search a for a substring among the strings. For example we have a string apple in the hashset
and now we need to find a substring 'app'? We cant do that in the hashmap but we can do that in the Trie as each letter sequence is a branch in itself in the tree and we can
traverse through the branches to find that substring. As it keeps tracks of all the prefix of the string, we also call it a 'Prefix Tree'.

Each Node in the tree can have upto 26 different branches! To store them all we can use a hashset. But wait! Each of those letter can also have 26 differet branches. Thats why
to store for all the nodes, we make a node class that stores all the branches of it as children. Now using hashset is not optimal because we have to store the whole node and 
if we store the letter of that node inside the node, then searching for that letter in the hashset cant be done in O(1) time. Hence we now use a hashmap that stores the letter 
as the key and its node as the value!

For inserting a word, we can start the root node which stores all the starting letters as children Then we check if the first character of the word is the children of the root
node. If not, it means our Trie has not word starting with that letter. So we make a node for that letter and then store it as a children of the root node.
Then we move on to the children node we just created. But if we arleady had that letter in the children of the root node, we directly go the node of that letter.
Now we repeat the same process for this node as well. 

The Trie implementation wants us to make two different implementation of search. One is 'search' and one is 'startsWith'. For 'search', we are only successfull if the 
word that we are searching for is a whole word and not a prefix/substring of a string whereas 'startsWith' is fine with the word being a substring or full string.
Thus for 'search', we have to create another property for the node that is 'ends' which denotes if the letter is the last letter of the word or not. While finishing the search
for the word and being sucessfull, we check if the last node we went through was the last node in the branch or not. If yes, the letter associated it with was the last letter
of the word else it wasnt. Hence in 'insert', we have to specify the last node as the ending by making its property of 'ends' as True(default it is false).

Now for searching, the flow is same as 'insert'. We just have to instead flag as False when a letter is not a children of the current node meaning we cant go further for the
search as theres no word in the trie where the letter we are in rn comes after the letter associated to the current node(i.e the previous letter and 
the children of the current node is the candidate to the next letter).If we were successfull throughout the whoel search, then at the end we return the 'ends' property 
of the last node which conveys that if the last node is the last letter then yes we found the word, but if it isnt then we didnt find the word and found just a substring.Due

And for the startsWith, its the same as "searching" but at the end we dont have to check for the property 'ends' and just can return True because we dont care if its a whole
word or a subtring.
###


class TrieNode:
    def __init__(self):
        self.children = {}
        self.ends = False

class Trie:

    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.ends = True
        

    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.ends
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True
