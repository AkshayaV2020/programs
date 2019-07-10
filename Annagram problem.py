m=input("Enter the string")
n=input("Enter tyhe second string")
l=[]
l1=[]
if len(m)==len(n):
    for i in range(0,len(m)):
        l.append(m.count(m[i]))
        l1.append(m.count(n[i]))
    if l==l1:
        print("Anagram")
    else:
        print("Not an anagram")
else:
        print("Not an anagram")

