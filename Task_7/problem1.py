
# Problem 1: Set .symmetric_difference() Operation
# HackerRank: https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem

n = int(input())
set_a = set(map(int, input().split()))

m = int(input())
set_b = set(map(int, input().split()))

result = set_a.symmetric_difference(set_b)

for num in sorted(result):
    print(num)

