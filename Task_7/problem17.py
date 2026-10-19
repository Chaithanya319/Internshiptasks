# Problem 17: Separate the Numbers
# HackerRank Link: https://www.hackerrank.com/challenges/separate-the-numbers/problem

def separateNumbers(s):
    n = len(s)

    for i in range(1, n // 2 + 1):
        first = s[:i]

        if first[0] == '0':
            continue

        num = int(first)
        result = ""

        while len(result) < n:
            result += str(num)
            num += 1

        if result == s:
            print("YES", first)
            return

    print("NO")


if __name__ == '__main__':
    q = int(input().strip())

    for _ in range(q):
        s = input().strip()
        separateNumbers(s)
