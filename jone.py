book_list={"jone" : "https://drive.google.com/file/d/1E-Dntr8O7dkXoD0-j1QwJefxVFRfM-kf/view",
           "mani":"https://drive.google.com/file/d/1t3igWm4VcL6vFL34dwuU1Whk4REEYEVX/view",
           "arul":"https://drive.google.com/file/d/1Mge29TbJxLHSnpMWHujQjjyarObB9bnC/view",
           "gana":"https://drive.google.com/file/d/1Tc4jk81V7yX2kovTe1Ze_hLdByVR7e8x/view",
           "saravanan":"https://drive.google.com/file/d/14Ajdc5DpaFkCS7xOLQgM2R1ZvRMxATfO/view"}
def penalty():
    print("NOTE:!!!! ALL BOOKS MUST BE RETURNED WITHIN A SPAN OF 5 DAYS ELSE PENALTY WILL BE CHARGED 60 rs per day")

bn=str(input("Enter the name of the book"))
if bn in book_list:
    print("the book is available to purchase")
    decision=str(input("do you wish to borrow it"))
    if decision == "yes":
        x=book_list[bn]
        print(x)
        penalty()
    else:
        print("thank you")

else:
    print("the book is not available")


