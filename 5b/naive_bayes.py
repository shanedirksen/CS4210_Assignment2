# -------------------------------------------------------------------------
# AUTHOR: Shane Dirksen
# FILENAME: naive_bayes.py
# SPECIFICATION: A simple python program that outputs the prediction and confidence of a naive bayes model
# FOR: CS 4210- Assignment #2
# TIME SPENT: 2 hours
# -----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard
# dictionaries, lists, and arrays

#importing some Python libraries
from sklearn.naive_bayes import GaussianNB
import csv

#reading the training data in a csv file
db = []
X = []
Y = []

# reading the data in a csv file
with open('weather_training.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for i, row in enumerate(reader):
        if i > 0:  # skipping the header
            db.append(row)

#transform the original training features to numbers and add them to the 4D array X.
#For instance Sunny = 1, Overcast = 2, Rain = 3, so X = [[3, 1, 1, 2], [1, 3, 2, 2], ...]]
for entry in db:
    updated_instance = []
    class_labels = []
    for i, value in enumerate(entry):
        if i == 1:
            if value == 'Sunny':
                updated_instance.append(1)
            elif value == 'Overcast':
                updated_instance.append(2)
            elif value == 'Rain':
                updated_instance.append(3)
        elif i == 2:
            if value == 'Cool':
                updated_instance.append(1)
            elif value == 'Mild':
                updated_instance.append(2)
            elif value == 'Hot':
                updated_instance.append(3)
        elif i == 3:
            if value == 'Normal':
                updated_instance.append(1)
            elif value == 'High':
                updated_instance.append(2)
        elif i == 4:
            if value == 'Weak':
                updated_instance.append(1)
            elif value == 'Strong':
                updated_instance.append(2)
        elif i == 5:
            if value == 'No':
                Y.append(1)
            elif value == 'Yes':
                Y.append(2)
    X.append(updated_instance)
# X =

#transform the original training classes to numbers and add them to the vector Y.
#For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
#--> add your Python code here
# Y =

#fitting the naive bayes to the data
clf = GaussianNB()
clf.fit(X, Y)

#reading the test data in a csv file
test = []
X2 = []
Y = []

# reading the data in a csv file
with open('weather_test.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for i, row in enumerate(reader):
        if i > 0:  # skipping the header
            test.append(row)
for entry in test:
    updated_instance = []
    for i, value in enumerate(entry):
        if i == 1:
            if value == 'Sunny':
                updated_instance.append(1)
            elif value == 'Overcast':
                updated_instance.append(2)
            elif value == 'Rain':
                updated_instance.append(3)
        elif i == 2:
            if value == 'Cool':
                updated_instance.append(1)
            elif value == 'Mild':
                updated_instance.append(2)
            elif value == 'Hot':
                updated_instance.append(3)
        elif i == 3:
            if value == 'Normal':
                updated_instance.append(1)
            elif value == 'High':
                updated_instance.append(2)
        elif i == 4:
            if value == 'Weak':
                updated_instance.append(1)
            elif value == 'Strong':
                updated_instance.append(2)
    X2.append(updated_instance)
#printing the header os the solution
# print("X2", X2)
prediction = []
for i in range(len(X2)):
    ans = clf.predict_proba([X2[i]])[0]
    # print("ans", ans)
    Y.append(ans)
    # print(ans[0])
    # print("i", i)
    if ans[0] > ans[1]:
        prediction.append("No")
    else:
        prediction.append("yes")
# print("Y", Y)
print ("Day".ljust(15) + "Outlook".ljust(15) + "Temperature".ljust(15) + "Humidity".ljust(15) + "Wind".ljust(15) + "PlayTennis".ljust(15) + "Confidence".ljust(15))
for i, entry in enumerate(test):
    # print("max", max(Y[i]))
    if max(Y[i]) < .75:
        continue
    else:
        print(entry[0].ljust(15) + entry[1].ljust(15) + entry[2].ljust(15) + entry[3].ljust(15) + entry[4].ljust(15) + prediction[i].ljust(15) + str(max(Y[i]))[0:4])

#use your test samples to make probabilistic predictions. For instance: clf.predict_proba([[3, 1, 2, 1]])[0]
#--> add your Python code here
