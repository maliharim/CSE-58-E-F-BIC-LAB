k=input()
rev_k=k[::-1]
rev_c=""
for x in rev_k:
    if x== "A":
        rev_c +="T"
    elif x=="T":
        rev_c +="A"
    elif x== "C":
        rev_c +="G"
    elif x=="G":
        rev_c +="C"
        
  
print(rev_c)
