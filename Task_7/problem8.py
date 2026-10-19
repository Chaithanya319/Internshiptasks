# Problem 8: Gemstones
# HackerRank Link: https://www.hackerrank.com/challenges/gem-stones/problem

def gemstones(arr):
    common_elements = set(arr[0])

    for rock in arr[1:]:
        common_elements = common_elements.intersection(set(rock))

    return len(common_elements)


if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(input().strip())

    result = gemstones(arr)
    print(result)
