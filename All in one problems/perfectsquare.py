import math
number=int(input())
root=math.sqrt(number)
if int(root+0.5)**2==number:
    print("Perfect Square")
else:
    print("Not Perfect Square")