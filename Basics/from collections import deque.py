from collections import deque
l=[10,20,30,40,50]
dq=deque(l)
dq.rotate(3)
l=list(dq)
print(l)