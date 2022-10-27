import pickle
import json
import pandas as pd
import numpy as np
import config


class MedicalInsurance() :
    def __init__ (self, age, sex, bmi, children, smoker, region):
        self.age = age
        self.sex = sex
        self.bmi = bmi
        self.children = children
        self.smoker = smoker
        self.region = "region_" + region

    
    def load_model (self) :
        with open (config.Medical_MODEL_FILE_PATH, "rb") as f :
            self.model = pickle.load(f)
        with open (config.Medical_JSON_FILE_PATH,"r") as f :
            self.json_data = json.load(f)


    def get_predicted_charges(self):

        self.load_model()

        region_index = self.json_data["columns"].index(self.region)

        array = np.zeros(len(self.json_data["columns"]))

        array[0] = self.age
        array[1] = self.json_data["sex"][self.sex]
        array[2] = self.bmi
        array[3] = self.children
        array[4] = self.json_data["smoker"][self.smoker]
        array[region_index] = 1

        print ("Test Array :",array)

        predicted_charges = self.model.predict([array])[0]
        print ("Medical Insurance Premium Charges :",predicted_charges)
        return np.around(predicted_charges,2)


if __name__ == "__main__" :
    age = 48
    sex = "female"
    bmi = 30.800
    children = 3
    smoker = "no"
    region = "northwest"

    medical_ins = MedicalInsurance(age, sex, bmi, children, smoker, region)
    charges = medical_ins.get_predicted_charges()
    print ()
    print (f"Medical Insurance Premium Charges will be {charges}/- Rs Only")