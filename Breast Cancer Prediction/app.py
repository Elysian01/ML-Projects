from flask import Flask, render_template, request, url_for, send_file, flash, redirect, make_response
import pickle
import numpy as np
import os

import termcolor
import smtplib

# import warnings
import CancerModel
import PdfConverter
from PdfConverter import PDFPageCountError

app = Flask(__name__)
app.config['SECRET_KEY'] = '73a4b6ca8cb647a20b71423e31492452'


@app.route("/infected")
def Infected():
    return render_template("Infected.htm", disease="Nothing")


@app.route("/noninfected")
def NonInfected():
    return render_template("NonInfected.htm")


@app.route("/download")
def Download():
    file = "static/Example.docx"
    return send_file(file, as_attachment=True)


@app.route("/BreastCancer", methods=["POST", "GET"])
def BreastCancer():
    if request.method == "POST":
        f = request.files['inputFile']

        name, extension = os.path.splitext(f.filename)
        print(extension)
        try:
            if extension == ".png" or extension == ".jpg" or extension == ".jpeg" or extension == ".pdf":
                location = os.path.join("Received_Files", f.filename)
                f.save(location)
                print("File Saved !")
                if extension == ".pdf":
                    PdfConverter.Convert(f.filename)
                    image = name + ".png"
                    prediction = CancerModel.Predict(
                        os.path.join("Received_Files", image))
                else:
                    prediction = CancerModel.Predict(
                        os.path.join("Received_Files", f.filename))
                print(prediction)
                if prediction:
                    return render_template("Infected.htm", disease="Breast Cancer ")
                else:
                    return render_template("NonInfected.htm")

            else:
                flash(
                    "Please upload files with extension 'png', 'pdf' , 'jpg' or 'jpeg'")

        except ValueError:
            flash("Please Upload Only Valid Files ")
        except PDFPageCountError:
            flash("Please Upload Only Valid Files , or try again later")
    return render_template("BreastCancer.html", title="Breast Cancer", navTitle="Breast Cancer", headText="Breast Cancer Probability Detector", ImagePath="/static/BreastCancer.jpg")


if __name__ == '__main__':
    app.run(threaded=True, debug=True, host="0.0.0.0", port=5000)
