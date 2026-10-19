# Problem 13: Sherlock and the Valid String
# HackerRank Link: https://www.hackerrank.com/challenges/sherlock-and-the-valid-string/problem

from collections import Counter

def isValid(s):
    freq = Counter(Counter(s).values())

    if len(freq) == 1:
        return "YES"

    if len(freq) != 2:
        return "NO"

    (f1, c1), (f2, c2) = freq.items()

    if (f1 == 1 and c1 == 1) or (f2 == 1 and c2 == 1):
        return "YES"

    if (abs(f1 - f2) == 1) and (c1 == 1 or c2 == 1):
        return "YES"

    return "NO"


if __name__ == '__main__':
    s = input().strip()
    result = isValid(s)
    print(result)
