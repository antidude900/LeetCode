"""
Approach: Remember the keypad mobile we used to have? each digit (except 1) was assigned to 3-4 characters. 
Here we are given a number and we have to return all possible letter combinations that the number could represent.
It means all the characters a digit represents can make combination with characters of other digits in the number

Note: As only one character can be typed through a digit, the length of character than a combination has equals to the length of the digit.
Also, a single digit cannot make combination with its own characters as already told that only one character can be typed through a digit.
"""


def letterCombinations(digits: str) -> List[str]:
    combs, comb = [],[]
    letters = {2:"abc",3:"def",4:"ghi",5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz"}  #the digit and letters representation in keypad
  
    def backtrack(i):
        if i == len(digits):  #here i represents the digit we are at in the number
            combs.append(''.join(comb))
            return 
        
        for letter in letters[int(digits[i])]:  #for that digit we are making combination for each of its possible letters with letters of other digit
            comb.append(letter)
            backtrack(i+1)  #going to another digit to make combination with its letters
            comb.pop()
          
    backtrack(0)
    return combs
        
