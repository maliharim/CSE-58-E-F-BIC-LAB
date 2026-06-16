p = input()
text = input()

d = int(input())

length = len(p)

for i in range(len(text)-length+1):
    mismatch = 0

    for j in range(length):
        if(p[j] != text[i+j]):
            mismatch += 1

    if mismatch <=d:
        print(i,end='  ')
