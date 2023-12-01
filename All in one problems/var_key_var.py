def check_args(*args):
    total_min=sum(args)
    if total_min<60:
        return f"Total time to launch {total_min} minutes."
    else:
        return f"Total time to launch is {total_min/60} seconds."
print(check_args(4,14,18))
    

def args_check(*args):
    print(args)
args_check("12")

def var_args(**args):
    print(args)
var_args(tanks=1,day="Mon",time=90)