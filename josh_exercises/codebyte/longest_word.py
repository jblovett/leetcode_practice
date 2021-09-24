"""Web link: https://coderbyte.com/editor/Longest%20Word:Python3
Goal is to return the longest word in a given string while excluding punctuation.
Concepts: for loops, string manipulation, and lists.
Notes: The split() function converts a string into a list of strings, each an individual word.
        Characters a thru z can be differentiated with operators. b > a.
Big O: O(n) for space and time. Loop through the string's characters once"""

def LongestWord1(sen: str): # note web solution doesn't have : str. Just sen
  #double_quote: str = '''"'''

  longest_word: str = "" # holds the longest word so far
  # excluded_characters = ["&", "!", "?", ".", ",", "'", "\"", double_quote] # better way to exclude puntuation?
  word: str = "" # holds the current word being built
  
  for character in sen:
    # if character in excluded_characters:
    #   continue
    if ((character < 'a' and character > 'z') or (character < 'A' or character > 'Z')):
        continue
    
    elif character == " ": #if reached a space, the word is complete. Time to compare length.
      
      
      if len(word) > len(longest_word):
        longest_word = word
      
      word = "" #current word set back to empty. Must hold the next word

    else:
      word += character

    
  if len(word) > len(longest_word): # quick fix for final word being excluded from the for loop. Check a string terminator instead?
        longest_word = word

  return longest_word

