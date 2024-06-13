import datetime
model = datetime.datetime.now()
print("the time is:",model)


#loction base
import pytz
from datetime import datetime
fst = pytz.datetime("America/new_york")
da_ta = datetime.now(fst)
print("America/new_york :",da_ta.strftime("%d/%m/%y , %h/%m/%s , %p"))

