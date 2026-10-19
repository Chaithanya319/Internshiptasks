# Problem 20: Super Reduced String
# HackerRank Link: https://www.hackerrank.com/challenges/reduced-string/problem

def superReducedString(s):
    stack = []

    for char in s:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)

    result = ''.join(stack)

    if result:
        return result
    else:
        return "Empty String"


if __name__ == '__main__':
    s = input().strip()
    print(superReducedString(s))
