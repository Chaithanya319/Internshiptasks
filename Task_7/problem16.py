# Problem 16: Caesar Cipher
# HackerRank Link: https://www.hackerrank.com/challenges/caesar-cipher-1/problem

def caesarCipher(s, k):
    result = []

    k = k % 26

    for char in s:
        if 'a' <= char <= 'z':
            new_char = chr((ord(char) - ord('a') + k) % 26 + ord('a'))
            result.append(new_char)

        elif 'A' <= char <= 'Z':
            new_char = chr((ord(char) - ord('A') + k) % 26 + ord('A'))
            result.append(new_char)

        else:
            result.append(char)

    return ''.join(result)


if __name__ == '__main__':
    n = int(input().strip())
    s = input().strip()
    k = int(input().strip())

    result = caesarCipher(s, k)
    print(result)
