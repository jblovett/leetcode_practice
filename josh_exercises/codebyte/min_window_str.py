""" link: https://coderbyte.com/editor/Min%20Window%20Substring:Python3
Given two strings in a list of strings, where index 0 is string N, and index 1 is string
K, find the shortest substring of N that contains all the characters in K.
concepts: str manipulation, list, range, nested for loops, string to a list of characters function."""

def MinWindowSubstring(strArr):
  add_the_rest: bool = False
  search_in = strArr[0] #string N
  
  res = "" #The resulting subarray
  shortest = strArr[0] # The shortest subarray. Default length is string N

  for i in range(len(search_in)): # Start the character search beginning at each character in N, sequentially
    search_for = list(strArr[1]) # Remake a list of characters of K for each i iteration
    for j in range(len(search_in) - i): # Iterate through the rest of the characters in N, starting at the index specified in the outter for loop
      char = search_in[i + j] # current character
      if len(search_for) == 0: # if every character in K has been included in the substring, break the loop.
        break
      elif add_the_rest: # The first time we find a character in K, we know that each character following will be in the substring.
        res += char
        if char in search_for: 
          search_for.remove(char) # Remove characters in K if they've been included.
      elif char in search_for:
        res += char
        search_for.remove(char)
        add_the_rest = True
      else:
        continue
    if len(search_for) == 0 and len(res) < len(shortest):
      shortest = res
    res = ""
  return shortest