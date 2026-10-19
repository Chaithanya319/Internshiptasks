# Problem 10: CamelCase
# HackerRank Link: https://www.hackerrank.com/challenges/camelcase/problem

def camelcase(s):
    count = 1

    for char in s:
        if char.isupper():
            count += 1

    return count


if __name__ == '__main__':
    s = input().strip()
    result = camelcase(s)
    print(result)
