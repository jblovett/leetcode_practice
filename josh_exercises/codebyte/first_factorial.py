"""Link: https://coderbyte.com/editor/First%20Factorial:Python3
return the factorial of a given int.
concepts: while loop, operators
Big O: O(n) for both time and space I think. All depends on the input"""


def FirstFactorial(num):
  multiplier = num - 1
 
  while multiplier > 0:
    num *= multiplier
    multiplier -= 1
    

  
  return num