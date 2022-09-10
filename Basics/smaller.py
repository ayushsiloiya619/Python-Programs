def smaller(l,x):
    res=[]
    for e in l:
        if e<x:
            res.append(e)
    return res 
l=[10,20,2,3,4,5]
x=10
print(smaller(l,x))