"""


Step1: Import package/Module
Step2: Store plotting points
Step3: Plot graph

"""

import matplotlib.pyplot as py

x = [5,4]
y = [8,30]

py.plot(x,y)
py.xlabel("Money in INR")
py.ylabel("Working no of hrs")
#py.bar(x,y)
py.pie(x)
py.show()


