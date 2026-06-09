exam = input()
m = int(input())    

count={}
for i in range(len(exam)- m+1):
    s = exam[i:i+m]
    if s in count:
        count[s] += 1
    else:
        count[s] = 1
max_count = max(count.values())

for s in count:
    if count[s]==max_count:
       print(s)
