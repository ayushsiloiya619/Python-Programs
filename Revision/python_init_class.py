class calculator:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def add(self):
        return self.num1+self.num2

cal=calculator(5,3)
result=cal.add()
print(result)