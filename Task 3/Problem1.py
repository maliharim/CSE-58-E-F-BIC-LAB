
from itertools import product

text = input()
k,d = map(int,input().split())

def mm(a,b):
    c = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            c += 1
    return c

patterns = {}

for i in product('ACGT', repeat=k):
    pattern = ''.join(i)
    c = 0

    for j in range(len(text)-k+1):
        if mm(pattern, text[j:j+k]) <= d:
            c += 1

    patterns[pattern] = c

max_count = max(patterns.values())

for pattern in patterns:
    if patterns[pattern]==max_count:
        print(pattern,end='  ')
