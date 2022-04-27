def myfilter(func,lst):
    x = []
    for i in lst:
        if func(i)==True:
            x.append(i)
        else:
            pass
    return x

def myfunc(x):
    if x%2==0:
        return True
    else:
        return False

num = [1,2,3,4,5,6,7,8]

combs = myfilter(myfunc,ages)

print(combs)
