"""If the number of teams are even, half will move on to the next round after matching. If the number of teams are odd, a random team
will move on while rest match, so that half the teams plus one move on. Find the number of matches until one winner remains!
https://leetcode.com/problems/count-of-matches-in-tournament/
Data structures needed: nothing fancy! While loops, if statements, and arithmetic."""

def numberofMatches(n: int) -> int:
    matches: int = 0
    while n > 1:
        if n % 2 == 0:
           # print("n was even")
           # print(n)
            matches = matches + (n / 2)
            n = n / 2
            
        else:
           # print("n was odd")
           # print(n)
            matches = matches + (n - 1) / 2
            n = (n - 1) / 2 + 1
            
    return int(matches)


def main():
    print(numberofMatches(14))



if __name__ == "__main__":
    main()