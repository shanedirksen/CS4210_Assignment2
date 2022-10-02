# -------------------------------------------------------------------------
# AUTHOR: Shane Dirksen
# FILENAME: knn.py
# SPECIFICATION: A simple python program that calculates the error rate of the 1NN LOO-CV method using a binary points input file
# FOR: CS 4210- Assignment #2
# TIME SPENT: 3 hours
# -----------------------------------------------------------*/

# IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard
# dictionaries, lists, and arrays

# importing some Python libraries
from sklearn.neighbors import KNeighborsClassifier
import csv

db = []

# reading the data in a csv file
with open('binary_points.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for i, row in enumerate(reader):
        if i > 0:  # skipping the header
            db.append(row)

# loop your data to allow each instance to be your test set
incorrect = 0

for i, instance in enumerate(db):
    # print(db)
    # add the training features to the 2D array X and remove the instance that will be used for testing in this
    # iteration. For instance, X = [[1, 3], [2, 1,], ...]]. Convert values to float to avoid warning messages
    # transform the original training classes to numbers and add them to the vector Y. Do not forget to remove the
    # instance that will be used for testing in this iteration. For instance, Y = [1, 2, ,...]. Convert values to
    # float to avoid warning messages

    # --> add your Python code here
    X = db[:i] + db[i + 1:]
    Y = []
    for j in X:
        j[0] = float(j[0])
        j[1] = float(j[1])
        Y.append(j[2])

    X = [k[:2] for k in X]

    for l, m in enumerate(Y):
        if m == '-':
            Y[l] = 0
        else:
            Y[l] = 1
    testSample = db[i]
    x = int(testSample[0])
    y = int(testSample[1])
    truth = testSample[2]
    if truth == '-':
        truth = 0
    else:
        truth = 1
    # fitting the knn to the data
    clf = KNeighborsClassifier(n_neighbors=1, p=2)
    clf = clf.fit(X, Y)

    # use your test sample in this iteration to make the class prediction. For instance:
    class_predicted = clf.predict([[x, y]])[0]
    # --> add your Python code here
    print("Predicted class: ", class_predicted)
    # compare the prediction with the true label of the test instance to start calculating the error rate.
    # --> add your Python code here
    if class_predicted != truth:
        incorrect = incorrect+1

# print the error rate
# --> add your Python code here
print("Error rate: ", incorrect / len(db))
