# Problem 7: Alphabet Rangoli
# HackerRank Link: https://www.hackerrank.com/challenges/alphabet-rangoli/problem

def print_rangoli(size):
    import string

    alphabet = string.ascii_lowercase
    width = 4 * size - 3
    lines = []

    for i in range(size):
        left = alphabet[size - 1:size - i - 1:-1]
        right = alphabet[size - i - 1:size]
        row = "-".join(left + right)
        lines.append(row.center(width, "-"))

    for i in range(size - 2, -1, -1):
        lines.append(lines[i])

    print("\n".join(lines))


if __name__ == "__main__":
    n = int(input())
    print_rangoli(n)
