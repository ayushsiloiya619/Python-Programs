s=input("enter str")
str="aeiouAEIOU"
v,c=0,0
for i in s:
    if i in str:
       v+=1
    else:
        c+=1
print("vowels= ",v)
print("cons ",c)
