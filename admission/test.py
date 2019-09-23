import pickle

f = open('DTR_model.pickle','rb')
model = pickle.load(f)

gre = int(input("Enter GRE   : "))
tof = int(input("Enter Toefl : "))
cgpa = int(input("Enter CGPA : "))

result = model.predict([[gre,tof,cgpa]])
print(result)
