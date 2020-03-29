from flask import Flask, render_template, request
import pickle

app = Flask(__name__)


with open("Coronavirus_logistic", "rb") as f:
    logisticRegression = pickle.load(f)

model_inputs = [0, 0, 1, 1, 1, 0, 1, 0, 0, 3, 0, 0, 2]
model_inputs1 = [0, 1, 0, 0, 0, 1, 0, 0, 2, 3, 3, 3, 2]


prediction = logisticRegression.predict_proba([model_inputs])[0][1]


@app.route("/", methods=["POST", "GET"])
def hello_world():
    if request.method == "POST":
        # print(request.form)
        submitted_values = request.form
        temperature = float(submitted_values["temperature"].strip())
        age = int(submitted_values["age"])
        cough = int(submitted_values["cough"])
        cold = int(submitted_values["cold"])
        sore_throat = int(submitted_values["sore_throat"])
        body_pain = int(submitted_values["body_pain"])
        fatigue = int(submitted_values["fatigue"])
        headache = int(submitted_values["headache"])
        diarrhea = int(submitted_values["diarrhea"])
        difficult_breathing = int(submitted_values["difficult_breathing"])
        travelled14 = int(submitted_values["travelled14"])
        travel_covid = int(submitted_values["travel_covid"])
        covid_contact = int(submitted_values["covid_contact"])

        age = 2 if (age > 50 or age < 10) else 0
        temperature = 1 if temperature > 98 else 0
        difficult_breathing = 2 if difficult_breathing else 0
        travelled14 = 3 if travelled14 else 0
        travel_covid = 3 if travel_covid else 0
        covid_contact = 3 if covid_contact else 0

        model_inputs = [cough, cold, diarrhea,
                        sore_throat, body_pain, headache, temperature, difficult_breathing, fatigue, travelled14, travel_covid, covid_contact, age]
        prediction = logisticRegression.predict([model_inputs])[0]

        print(model_inputs)
        print("*******************          ", prediction)

        if prediction:
            return render_template("Infected.htm")
        else:
            return render_template("NonInfected.htm")

    return render_template("index.htm")
 # return "hello_world   " + str(format(float((str(prediction).replace(',', '.'))), ".3f")) + " %"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="14444", debug=True)
