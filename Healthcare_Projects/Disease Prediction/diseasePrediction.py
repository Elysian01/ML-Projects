from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import LabelEncoder
import numpy as np
import pandas as pd

df = pd.read_csv("Disease_Symptoms.csv")
disease = set(df.iloc[:, 0])
disease = list(disease)
disease.sort()

# Data Preprocessing

labelencoder_Y = LabelEncoder()
df.iloc[:, 0] = labelencoder_Y.fit_transform(df.iloc[:, 0].values)

with open("Coded.csv", "w") as f:
    df.to_csv(f, line_terminator="\n", encoding="ISO-8859-1")


# Split the dataset into independent (X) and dependent (Y)
X = df.iloc[:, 1:58].values
Y = df.iloc[:, 0].values

# Spliting Dataset into training and testing samples

# Split the dataset into 80% training and 20% testing

X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.20, random_state=0)


# Creating Models ( Decision Tree , Random Forest )

# Create a function for the models


def models(X_train, Y_train):

    # Decision Tree Classifier

    from sklearn.tree import DecisionTreeClassifier
    tree = DecisionTreeClassifier(criterion="entropy", random_state=0)
    tree.fit(X_train, Y_train)

    # Random Forest Classifier

    from sklearn.ensemble import RandomForestClassifier
    forest = RandomForestClassifier(
        n_estimators=10, criterion="entropy", random_state=0)
    forest.fit(X_train, Y_train)

    # Print the models accuracy on the training data

    print('[0] Decision Tree Classifier Training Accuracy : ',
          tree.score(X_train, Y_train))
    print('[1] Random Forest Classifier Training Accuracy : ',
          forest.score(X_train, Y_train))

    return tree, forest


# Getting all the models

model = models(X_train, Y_train)


# Testing Model Accuracy by Confusion Matrix


# Test model accuracy on test data on Confusion matrix


for i in range(len(model)):
    print("Model ", i)

    cm = confusion_matrix(Y_test, model[i].predict(X_test))
    # [[true_negative , false_postive] [false_negative,true_positive]]
    TP = cm[1][1]
    TN = cm[0][0]
    FP = cm[0][1]
    FN = cm[1][0]

    print(cm)
    print("Testing Accuracy =  ", (TP + TN)/(TP + TN + FN + FP))
    print()


def saveModel():
    import pickle
    with open("DiseasePrediction(Rand)", "wb") as f:
        pickle.dump(model[1], f)

# Testing the model against incoming input


header = ['bloody_stools', 'fecal_leakage', 'swelling', 'dizziness', 'confusion', 'fatigue', 'itching', 'vomiting', 'arm_pain',
          'cough', 'muscle_pain', 'depression', 'fever', 'painful_bowel_moments', 'urine_blood', 'sweating', 'nausea',
          'stiff_neck', 'decreased_appetite', 'weak', 'wheezing', 'bleeding', 'hives', 'bleed', 'headache', 'dry_mouth', 'sweat',
          'stomach_pain', 'stool_pressure', 'anxiety', 'shoulder_pain', 'anus_itching', 'vision_problem', 'abdominal_pain',
          'chest_pain', 'weight_loss', 'diarrhea', 'breath_problems', 'thirsty', 'anus_swelling', 'blood_o_tissue', 'constipation',
          'neck_pain', 'low_heartbeat', 'more_urine', 'low_breath', 'muscle_cramps', 'muscle_spasm', 'yawning', 'rash', 'back_pain',
          'anal_bleeding', 'lump_anus', 'cold', 'skin_rash', 'neck_stiff']

model_inputs = []
for x in range(0, len(header)):
    model_inputs.append(0)

inputs = [i.strip() for i in input("Enter Symptoms : ").split()]

print(inputs)

for element in range(0, len(header)):
    for symptoms in inputs:
        if symptoms == header[element]:
            model_inputs[element] = 1

prediction = model[0].predict([model_inputs])

print(disease[prediction[0]])

# with open("Models\DiseasePrediction(Dec)", "rb") as f:
#     decisionTreeModel = pickle.load(f)

# prediction = decisionTreeModel.predict([model_inputs])
# disease[prediction[0]]
