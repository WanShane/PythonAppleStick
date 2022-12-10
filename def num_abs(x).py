def num_abs(x):
    if x < 0:
        return(-x)
    else:
        return(x)
a = input("input your number:")
x = int(a)
print("the abs is:",num_abs(x))