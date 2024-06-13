#syntax
"""
function.reduce(function,iterabla,initializer)
here initializer is optional
"""
""""
from functools import reduce
def add(x,y):
    return x+y
numbers=[1,2,5,4,2,3,2,11]
print("result:",reduce(add,numbers))"""


from functools import reduce
list1=[11,10,9,8,7,6,5,12,13,14,2,15,16]
def least(x,y):
     if x<y:
        return x
     else:
        return y

result= reduce(least,list1)
print("the least value:",result)
