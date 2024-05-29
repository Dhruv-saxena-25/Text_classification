from flask import Flask,request,render_template
import numpy as np
import pandas as pd
from flask_cors import CORS, cross_origin
from sklearn.preprocessing import StandardScaler
from hate.pipeline.prediction_pipeline import PredictionPipeline
from hate.constants import *

application=Flask(__name__)
CORS(application)
app=application

## Route for a home page

# @app.route('/')
# def index():
#     return render_template('home.html') 

@app.route("/", methods=['GET'])
@cross_origin()

def home():
    
    return render_template('home.html')



@app.route('/predict',methods=['POST'])
def predictRoute():
    if request.method == 'POST':
            # Extract the text input from the form
            input_text = request.form['text']
            obj = PredictionPipeline()
            result = obj.run_pipeline(input_text)
            return render_template('result.html', results=result)
    

if __name__=="__main__":
    app.run(host=APP_HOST, port= APP_PORT, debug= True)     