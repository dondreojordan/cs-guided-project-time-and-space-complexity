"""
You have a string. 
Split it into the minimum possible number of increasing substrings. 
A substring is considered to be increasing when the next symbol in the substring is also next 
in the English alphabet. 
This is case sensitive, i.e. 'b' is next for 'a' but 'C' is not next for 'b'. 
Return an array of these substrings.

Example

For s = "ABCDEFFDEfghCBA", the output should be
increasingSubstrings(s) = ["ABCDEF", "F", "DE", "fgh", "C", "B", "A"].
"""

# def increasingSubstrings(string):
#     # input: a string containing lowercase/uppercase letters in any alphebetical order
#     def alphabetical(word):
#         return list(word) == sorted(word)

#     # Parse the string into letters to variable 'parsed_string'
#     # if letter in parsed_string.isupper() :
#         # 
#     # else:
#     # return: an array of strings in alphebetical order together as lowercase or uppercase
#     return

def alphabetical(word):
    return list(word) == sorted(word)



if __name__=='__main':
    string = "ABCDEFFDEfghCBA"
    print(alphabetical("ABCDEFFDEfghCBA"))
    # print(increasingSubstrings(string))