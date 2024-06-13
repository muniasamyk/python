

try:
    firstname = str(input("Enter the name :"))
    lastname = str(input("Enter the name :"))
    fullname = firstname + lastname
except Exception as g :
    print(g)
    print("THE NAME IS MAIN OUR LIFE")
else:
    print(fullname)


finally:
    print("Thank you")





