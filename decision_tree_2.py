# -------------------------------------------------------------------------
# AUTHOR: Shane Dirksen
# FILENAME: decision_tree_2.py
# SPECIFICATION: A simple python program that creates decision trees using different datasets and runs 10 times, finds the lowest accuracy, and reports as the performance.
# FOR: CS 4210- Assignment #2
# TIME SPENT: 2 hours
# -----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard
# dictionaries, lists, and arrays

#importing some Python libraries
from sklearn import tree
import csv

dataSets = ['contact_lens_training_1.csv', 'contact_lens_training_2.csv', 'contact_lens_training_3.csv']
performance = []
for ds in dataSets:

    dbTraining = []
    X = []
    Y = []

    #reading the training data in a csv file
    with open(ds, 'r') as csvfile:
         reader = csv.reader(csvfile)
         for i, row in enumerate(reader):
             if i > 0: #skipping the header
                dbTraining.append (row)
    #transform the original categorical training features to numbers and add to the 4D array X. For instance Young = 1, Prepresbyopic = 2, Presbyopic = 3
    for entry in dbTraining:

        updated_instance = []
        for i, value in enumerate(entry):
            if i == 0:
                if value == 'Young':
                    updated_instance.append(1)
                elif value == 'Prepresbyopic':
                    updated_instance.append(2)
                elif value == 'Presbyopic':
                    updated_instance.append(3)
            elif i == 1:
                if value == 'Myope':
                    updated_instance.append(1)
                elif value == 'Hypermetrope':
                    updated_instance.append(2)
            elif i == 2:
                if value == 'No':
                    updated_instance.append(1)
                elif value == 'Yes':
                    updated_instance.append(2)
            elif i == 3:
                if value == 'Reduced':
                    updated_instance.append(1)
                elif value == 'Normal':
                    updated_instance.append(2)
        X.append(updated_instance)

    #transform the original categorical training classes to numbers and add to the vector Y. For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
    #--> addd your Python code here
    # Y =
    for entry in dbTraining:
        if entry[-1] == 'Yes':
            Y.append(1)
        elif entry[-1] == 'No':
            Y.append(2)
    # print("X", X)
    # print("Y", Y)
    accuracy = []
    #loop your training and test tasks 10 times here
    for i in range (10):

        #fitting the decision tree to the data setting max_depth=3
        clf = tree.DecisionTreeClassifier(criterion = 'entropy', max_depth=3)
        clf = clf.fit(X, Y)

       #read the test data and add this data to dbTest
       #--> add your Python code here
        dbTest = []
        dataSet = 'contact_lens_test.csv'
        with open(dataSet, 'r') as csvfile:
            reader = csv.reader(csvfile)
            for i, row in enumerate(reader):
                if i > 0:  # skipping the header
                    dbTest.append(row)
        # print(dbTest)


        X2 = []
        Y2 = []
        incorrect = 0
        for n, data in enumerate(dbTest):
            #transform the features of the test instances to numbers following the same strategy done during training,
            #and then use the decision tree to make the class prediction. For instance: class_predicted = clf.predict([[3, 1, 2, 1]])[0]
            #where [0] is used to get an integer as the predicted class label so that you can compare it with the true label
            #--> add your Python code here
            # print("data", data)
            updated_instance = []
            for i, value in enumerate(data):
                if i == 0:
                    if value == 'Young':
                        updated_instance.append(1)
                    elif value == 'Prepresbyopic':
                        updated_instance.append(2)
                    elif value == 'Presbyopic':
                        updated_instance.append(3)
                elif i == 1:
                    if value == 'Myope':
                        updated_instance.append(1)
                    elif value == 'Hypermetrope':
                        updated_instance.append(2)
                elif i == 2:
                    if value == 'No':
                        updated_instance.append(1)
                    elif value == 'Yes':
                        updated_instance.append(2)
                elif i == 3:
                    if value == 'Reduced':
                        updated_instance.append(1)
                    elif value == 'Normal':
                        updated_instance.append(2)
            X2.append(updated_instance)

            # transform the original categorical training classes to numbers and add to the vector Y. For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
            # --> addd your Python code here
            # Y =
            for entry in dbTest:
                if entry[-1] == 'Yes':
                    Y2.append(1)
                elif entry[-1] == 'No':
                    Y2.append(2)
            # print("y2", Y2)

            # print("n", n)
            class_predicted = clf.predict([X2[n]])[0]
            if class_predicted != Y2[n]:
                incorrect = incorrect + 1

            # print("Prediction: ", class_predicted)
            # print("Ground truth: ", Y2[n])
            # print("Dataset: ", ds)
        accuracy_1 = 1 - (incorrect / len(dbTest))
        accuracy.append(accuracy_1)
    print("accuracy", accuracy)
    performance.append(min(accuracy))
print("Worst performance of each model", performance)
            #compare the prediction with the true label (located at data[4]) of the test instance to start calculating the accuracy.
            #--> add your Python code here

        #find the lowest accuracy of this model during the 10 runs (training and test set)
        #--> add your Python code here

    #print the lowest accuracy of this model during the 10 runs (training and test set).
    #your output should be something like that: final accuracy when training on contact_lens_training_1.csv: 0.2
    #--> add your Python code here




