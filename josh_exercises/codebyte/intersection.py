"""Find the intersection of two comma seperated strings of numbers. https://coderbyte.com/editor/Find%20Intersection:Python3
The two strings are given in an array.
Concepts: string manipulation. The split() function in str objects removes whitespace around a string by default, and removes a given
character at the beginning and end of the string. Results in a new string (does not mutate the string object)."""

def FindIntersection(strArr):
  str_1 = strArr[0]
  str_2 = strArr[1]
  list1 = list(str_1.split(", "))
  list2 = list(str_2.split(", "))
  result = ""
  no_intersection = True

  for string in list1:
    if string in list2:
      no_intersection = False
      result += string
      result += ","

  if no_intersection:
    return "false"
  
  return result.strip(",")