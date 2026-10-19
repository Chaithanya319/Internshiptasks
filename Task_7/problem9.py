# Problem 9: Beautiful Binary String
# HackerRank Link: https://www.hackerrank.com/challenges/beautiful-binary-string/problem

def beautifulBinaryString(b):
    return b.count("010")


if __name__ == '__main__':
    n = int(input().strip())
    b = input().strip()

    result = beautifulBinaryString(b)
    print(result)
