# Problem 4: Funny String
# HackerRank Link: https://www.hackerrank.com/challenges/funny-string/problem

def funnyString(s):
    n = len(s)

    for i in range(1, n):
        left = abs(ord(s[i]) - ord(s[i - 1]))
        right = abs(ord(s[n - i]) - ord(s[n - i - 1]))

        if left != right:
            return "Not Funny"

    return "Funny"


if __name__ == '__main__':
    t = int(input().strip())

    for _ in range(t):
        s = input().strip()
        result = funnyString(s)
        print(result)
