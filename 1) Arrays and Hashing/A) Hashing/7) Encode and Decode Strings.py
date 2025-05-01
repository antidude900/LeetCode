"""
Approach:
Here we have to encode a list of strings into a single string and we can also decode back the signle string into list of strings.
A simple approach might come in mind to just add a certain symbol between the single strings when combining them all and based on that symbol, we can decode it back to multiple strings!

(Will be referring single string as word to avoid confusion)
But there's a edge case! What if the symbol which we are using to seperate the individual words also comes in the list of words???)
So using only symbol is not enough. what if we use the lenght of each words along with the symbol. 
Here symbol will be used to determine the end of the string which gives the length of its respective word
And as we are keeping track of the length of each words, then we also know the start of the string which gives the length of its respective word.
So as we know the start and end of the string which gives the length of its respective word, there will be no confusing in distinguising which is the word and which is the length!
"""

def encode(strs: List[str]) -> str:
    res = ""
    for s in strs:
        res+=str(len(s))+"#"+s    #length+symbol+word
    return res
    
def decode(s: str) -> List[str]:
    i = 0 
    res  = []    #to store the list of worfs
    while(i<len(s)): 
        j = i+1    #to check if the next character after it is # or not for determining the end of string which determines the length of the respective word  
        while (s[j]!="#"):    #if its not #, then go on searching for it
            j+=1
        
        length = int(s[i:j])    #the string upto it from where we started searching gives the length
        i = j + 1    #start of the word
        j += length + 1    #end+1 of the word(as slicing s[i:j] includes characters starting from s[i] to s[j-1]
        res.append(s[i:j]) 
        i =  j    #the new start for checking the string which gives the length of the respective word
    return res
