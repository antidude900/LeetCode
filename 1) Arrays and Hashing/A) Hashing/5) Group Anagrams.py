"""
Approach:
This is problem is built upon the Valid Anagram Problem. Instead of two strings, we are given multipe string and then we have to group the anagrams together!

For each word, we make a list where the index represents the letter(0 for a, 1 for b and so on) and the value at that index represents the frequency of that letter.
Then we use that list as the key of the dictionary and thus every word which has that same list of frequeny is added to the list of that key. 
In this way grouping of anagrams is done
"""

def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    frequencies = defaultdict(list)
    for word in strs:
        count = [0]*26    #as there are 26 alphabets
        #instead of the ascii method,we can just simply sort the word and use that as the key for the frequencies dict
        #it might sound worse in theory but it performs more well(maybe because of the length of strings being small)
        for letter in word:
            count[ord(letter) - ord('a')] += 1    #for statring indexing from 0
        frequencies[tuple(count)].append(word)    #cant use list as the key so turning it into tuple
    
    return list(frequencies.values()) #returning only the values i.e the list of words grouped together as anagrams
    

#More efficient pne is by simply sorting the word and using htat as the key:
def groupAnagrams(strs):
    frequencies= defaultdict(list)
        
    for word in strs:
        sorted_word = ''.join(sorted(word))
        frequencies[sorted_word].append(word)
        
    return list(frequencies.values())
