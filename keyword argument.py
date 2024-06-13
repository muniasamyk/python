"""def person(name,age,gender,address,pincode):
    print(                "the person details"              )
    print("NAME:",name)
    print("AGE:", age)
    print("GENDER:", gender)
    print("ADDRESS:", address)
    print("PINCODE:", pincode)
person("mani",21,"male","chennai",606002)
"""
#key word using
#person(name="mani",age=21,pincode=606622,address="chennai",gender="male")
#positional arguments(*args)
#lenth keyword  arguments(**kwargs)

def Details(**kwargs):
    print("datas:",kwargs)
    print("data type:",type(kwargs))
    for key,value in kwargs.items():
        print("{}:{}",format(key,value))
Details(name="mani",address="chennai",age=21)









