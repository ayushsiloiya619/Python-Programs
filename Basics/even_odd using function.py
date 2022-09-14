def even_odd(l):
    even=[]
    odd=[]
    for x in l:
        if x%2==0:
            even.append(x)
        else:
            odd.append(x)
    return even,odd
l=[10,21,30,41,50]
even,odd=even_odd(l)
print("even =",even)
print("odd =",odd)