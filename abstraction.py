from abc import ABC
class user(ABC):
      def __init__ (self,names,months):
          self.name = names
          self.month = months
      def display_user(self):
           print("%s subscripe for %d months" %(self.name,self.month))
      def process_fees(self):
          pass
class platinumuser(user):
    platinumpackege = 5000
    def process_fees(self):
        return self.month * platinumuser.platinumpackege
class golduser(user):
    goldpackege = 2000
    def process_fees(self):
        return self.month * golduser.goldpackege
md = platinumuser("Mani",11)
md.display_user()
nmd = md.process_fees()
print("Fees is ",nmd)
