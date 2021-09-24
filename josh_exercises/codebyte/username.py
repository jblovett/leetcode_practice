""" Username Validation. Link: https://coderbyte.com/editor/Codeland%20Username%20Validation:Python3
The given string parameter must have the following conditions to be valid: 
1. The username is between 4 and 25 characters.
2. It must start with a letter.
3. It can only contain letters, numbers, and the underscore character.
4. It cannot end with an underscore character.
If all of these are true, return the string "true". If any of them are false, return the string "false".
Concepts: String manipulation, ascii tables. Note that conditional operators on chars return true or false based
on their ascii sequence. Str objects have .isalpha() and .isdigit() functions that return true if they consist entirely of 
letters or numbers respectively. """

def CodelandUsernameValidation(strParam) -> str:
  str_length: int = len(strParam)
  if str_length < 4 or str_length > 25:
    return "false"
  for index in range(str_length):
    char = strParam[index]
    if index == 0:
      if (char < "A") or (char > "Z" and char < "a") or (char > "z"):
        return "false"
    elif (char > "9" and char < "A") or (char < "_" and char > "Z") or (char == ",") or (char < "0") or (char > "z"):
      return "false"
    elif index == len(strParam) - 1 and char == "_":
      return "false"
  # code goes here
  return "true"

# keep this function call here 
print(CodelandUsernameValidation(input()))