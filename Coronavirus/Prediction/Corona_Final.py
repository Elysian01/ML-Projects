import pickle
from termcolor import colored

# accuracy ==> 100%

with open("Coronavirus_logistic", "rb") as f:
    logisticRegression = pickle.load(f)

model_inputs = [0, 0, 1, 1, 1, 0, 1, 0, 0, 3, 0, 0, 2]
model_inputs1 = [0, 1, 0, 0, 0, 1, 0, 0, 2, 3, 3, 3, 2]


prediction = logisticRegression.predict([model_inputs])

print()

if prediction:
    print(colored("You may be suffering , Please visit nearest hospital for test", "red"))
else:
    print(colored("You are safe :) ", "green"))
