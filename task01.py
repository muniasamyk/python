#multilevel inheritance

class markets:
    def items1(self):
        self.name1= input("Enter the fruits:")
        self.name2= int(input("How much KG:"))
class items1(markets):
    def items2(self):
        self.name3 = input("Enter the vachitables:")
        self.name4 = int(input("How much KG:"))
class items(items1):
    def items3(self):
        self.name5= input("Enter the juice:")
        self.name6= int(input("How many :"))
        self.name7= input("Enter the items :")
class details(items):
    def getdatails(self):
        print("-------------WEL COME-------------")
        print("Name of the fruits :",self.name1)
        print("Amound of fruits:",self.name2)
        print("Name of the vachitables :",self.name3)
        print("Amound of vachhitables:",self.name4)
        print("Name of the juice:",self.name5)
        print("Juice  :", self.name6)
        print("Name of the items:", self.name7)
        print("--------THANK YOU---------")
abc = details()
abc.items1()
abc.items2()
abc.items3()
abc.getdatails()
'''

#hybride inheritance
class onlinecourse:
    def search(self):
        print("course name     :python")
        print("duration        :2 to 3 months")
class detail(onlinecourse):
    def identify(self):
        print("your select method :",str(input("PAID or UNPAId  :")))
        print("your session is :",str(input("what session you need(Forenoon or Afternoon) :")))
class timing(onlinecourse):
    def time(self):
        print("your class timing is :",str(input("Your available timing:")))

        print("---subscribe now---")
class details(detail,timing):
    def getdetails(self):
        print("--------------welcome to our dutorial-------------")
cmd = details()
cmd.getdetails()
cmd.search()
cmd.identify()
cmd.time()

'''























