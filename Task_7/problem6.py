# Problem 6: Pangrams
# HackerRank Link: https://www.hackerrank.com/challenges/pangrams/problem

def pangrams(s):
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    letters = set(s.lower())

    if alphabet.issubset(letters):
        return "pangram"
    else:
        return "not pangram"


if __name__ == '__main__':
    s = input()
    result = pangrams(s)
    print(result)
