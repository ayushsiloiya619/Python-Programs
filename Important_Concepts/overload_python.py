class A:
    def test(self , x=None , y=None):
        if x!=None and y!=None:
            return x*y 
        elif x!=None:
            return x*x 
        else:
            return 0
obj=A()
print(obj.test(2,3))
print(obj.test(2))
print(obj.test())