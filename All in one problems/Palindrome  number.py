i=int(input())
org=i
rev=0
while (i>0):
    rev=rev*10+i%10
    i=i//10
if rev==org:
    print('palindrome')
else:
    print('not palindrome')