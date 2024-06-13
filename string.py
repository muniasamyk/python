'''
a = "python is a high level language"
output = a.capitalize()
print(output)
'''
"""
print("the upper case :",a.upper())
print("the lower case :",a.lower())
print("the split case :",a.split())
print("the title case :",a.title())"""

"""
b = a.split()
print("the join case :", b.join())
"""

'''
print ("the index values:", a.index("level"))
print ("the find values:", a.find("ab"))
'''
"""
b = "!!!hi helow!!!"
print("strip is:", b.strip())
print("lstrip:", b.lstrip("!!!"))
print("rstrip:", b.rstrip("!!!"))
"""
'''
c = "welcome to our department"
print(c.count("e"))
print(c.startswith("w"))
print(c.endswith("h"))
print(c.encode())

"""type casting"""
a = "hi"
print(type(a))
b = int(10)
print(type(b))'''

"""slicing"""
'''t = "hellowworld"[::2]
print(t)
print(t[0:5:1])
print(t[0:10:2])'''
'''
for i in range(10):
 print(i)
 print("hi")
'''


'''
x =  1
def funvction():
       global x
       x =x+1
funvction()
print(x)
'''




def revers_string(input_str):
    reversed_str = ""
    index = len(input_str) - 1

    while index >= 0:
        reversed_str += input_str[index]
        index -= 1
        print("Reversed str:", reversed_str)

str = input("Enter a str:")
print("original str:", str)

revers_string(str)

