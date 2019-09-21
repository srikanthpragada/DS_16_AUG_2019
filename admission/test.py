import pandas as pd

model = pd.read_pickle('DTR_model.pickle')

gre = int(input("Enter GRE   : "))
tof = int(input("Enter Toefl : "))
cgpa = int(input("Enter CGPA : "))

result = model.predict([[gre,tof,cgpa]])
print(result)
