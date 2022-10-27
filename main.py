from distutils.command.config import config
import config
from flask import Flask,render_template,jsonify,request
from Model.utils import MedicalInsurance

app = Flask(__name__)

@app.route("/")
def home_api() :
    print ("Welcome to Medical Insurance Charges Prediction")
    return render_template("index.html")


@app.route("/predict_charges",methods = ["POST","GET"])
def predict_charges () :

    if request.method == "GET" :
        print ("We are using GET Method")

        age = int(request.args.get("age"))
        sex = request.args.get("sex")
        bmi = float(request.args.get("bmi"))
        children = int(request.args.get("children"))
        smoker = request.args.get("smoker")
        region = request.args.get("region")

        print ("age, sex, bmi, children, smoker, region :\n",age, sex, bmi, children, smoker, region)

        medical_charges = MedicalInsurance(age, sex, bmi, children, smoker, region)
        charges = medical_charges.get_predicted_charges()
        return render_template("index.html",prediction = charges)

    else :
        print ("We are using POST Method")

        age = int(request.form.get("age"))
        sex = request.form.get("sex")
        bmi = float(request.form.get("bmi"))
        children = int(request.form.get("children"))
        smoker = request.form.get("smoker")
        region = request.form.get("region")

        print ("age, sex, bmi, children, smoker, region :\n",age, sex, bmi, children, smoker, region)

        medical_charges = MedicalInsurance(age, sex, bmi, children, smoker, region)
        charges = medical_charges.get_predicted_charges()
        return render_template("index.html",prediction = charges)

if __name__ == "__main__" :
    app.run (host = "0.0.0.0", port = config.PORT_NUMBER, debug = True)