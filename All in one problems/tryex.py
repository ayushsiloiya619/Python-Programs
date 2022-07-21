try: 
    x=int(input("x = "))
    y=int(input("y = "))
    res=x/y 
except ValueError:
    print("Bad input number!")
except ZeroDivisionError:
    print("Division by zero!")
else:
    print("The result is ",res)
finally:
    print("The program finished!")