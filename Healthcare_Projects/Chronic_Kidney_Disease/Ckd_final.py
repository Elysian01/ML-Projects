import pickle
import numpy as np

with open("CKD", "rb") as f:
    deepLearningModel = pickle.load(f)

print("Working")

model_inputs = [0.75, 0.2, 0.033898, 0.836735, 0.717949, 1.0]
model_inputs1 = [1.020, 0.0, 1.2, 14.8, 30, 0]
model_inputs2 = [1.020, 0.0, 0.8, 14.1, 29, 0]

print()

temp_array = np.array(model_inputs2).reshape(1, 6)
pred = deepLearningModel.predict(temp_array)
pred = [1 if y >= 0.5 else 0 for y in pred][0]
print(pred)
