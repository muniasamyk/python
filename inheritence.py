#sinlge class
'''
class cars:
    firstcarname = "BMW"
    seccarname = "toyota"
    thirdcarname = "tata"
class details(cars):
    version = "M serius"
    version1 ="Fornuter"
    version2 ="Tata i5"
ob = details()
print(ob.firstcarname,"is a version of",ob.version)
print(ob.seccarname,"is a version of",ob.version1)
print(ob.thirdcarname,"is a version of",ob.version2)
'''

#multilevel

class personal:
    def getpersonaldetail(self):
        self.name = input("enter the name :")
        self.mail = input("enter the mail id :")
class educational(personal):
    def geteducationaldetail(self):
        self.collegename = input("enter the college of name :")
        self.department = input("enter the department name :")
class professional(educational):
    def getprofessionaldetails(self):
        self.companyname = input("enter company name :")
        self.designation = input("enter the designation :")
class details(professional):
    def getdetails(self):
        print("------------records---------------")
        print("Name       :",self.name)
        print("Mail       :",self.mail)
        print("college name :",self.collegename)
        print("department   :",self.department)
        print("company name :",self.companyname)
        print("designation   :",self.designation)
        print("-----------thank you-----------")
obj = details()
obj.getpersonaldetail()
obj.geteducationaldetail()
obj.getprofessionaldetails()
obj.getdetails()