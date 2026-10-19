# Problem 12: Making Anagrams
# HackerRank Link: https://www.hackerrank.com/challenges/making-anagrams/problem

from collections import Counter

def makeAnagram(a, b):
    count_a = Counter(a)
    count_b = Counter(b)

    deletions = 0

    for char in set(a) | set(b):
        deletions += abs(count_a[char] - count_b[char])

    return deletions


if __name__ == '__main__':
    a = input().strip()
    b = input().strip()

    result = makeAnagram(a, b)
    print(result)
