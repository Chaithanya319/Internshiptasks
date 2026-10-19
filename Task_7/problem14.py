# Problem 14: Anagram
# HackerRank Link: https://www.hackerrank.com/challenges/anagram/problem

from collections import Counter

def anagram(s):
    n = len(s)

    if n % 2 != 0:
        return -1

    mid = n // 2
    first = Counter(s[:mid])
    second = Counter(s[mid:])

    changes = 0

    for char in first:
        if first[char] > second[char]:
            changes += first[char] - second[char]

    return changes


if __name__ == '__main__':
    q = int(input().strip())

    for _ in range(q):
        s = input().strip()
        result = anagram(s)
        print(result)
