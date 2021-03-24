class Solution:
    """A class which returns the longest possible palindrome in a string."""

    def plaindrome_dict(self, word: str) -> int:
        """Calculates a hashmap of char frequencies in a given string.
         Calls biggest palindrome to return the longest possible."""
        letter_counts = {}
        for char in word:
            if (letter_counts.get(char) == None):
                letter_counts.setdefault(char, 1)
            else:
                letter_counts[char] = (letter_counts[char] + 1)
        return int(self.biggest_palindrome(letter_counts))

    def biggest_palindrome(self, letter_counts: dict) -> int:
        """Calculates the length of the longest possible palindrome. A palindrome must consist of at least one pair, 
        with the odd numbers in the middle if they exist. This function detects if that case is present."""
        pairs = 0
        is_odd = False
        for key in letter_counts:
            count = int(letter_counts[key])
            if (count % 2 == 0):
                pairs = (pairs + (count / 2))
            else:            
                is_odd = True
        if (is_odd and pairs > 0):
            return ((pairs * 2) + 1)
        else:
            return (pairs * 2)
