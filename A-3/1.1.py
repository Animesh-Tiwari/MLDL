def myreduce(func,lst):
    return a
def func(a,b):
    return a+b
lst = [1,2,3,4,5]
a = lst[0]
for i in range(1,len(lst)):
    b = lst[i]
    a = func(a,b)
print(myreduce(func,lst))
