# Problem 3: Mars Exploration
# HackerRank Link: https://www.hackerrank.com/challenges/mars-exploration/problem

def marsExploration(s):
    count = 0

    for i in range(len(s)):
        if s[i] != "SOS"[i % 3]:
            count += 1

    return count


if __name__ == '__main__':
    s = input().strip()
    result = marsExploration(s)
    print(result)
