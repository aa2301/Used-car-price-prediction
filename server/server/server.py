from flask import Flask, request, jsonify
import pickle
import numpy as np
__model=None
app=Flask(__name__)
def load_artifacts():
    global __model
    with open("D:\My\projects\sp ml\UCPP\server\artifacts\Used_car_price_prediction",'rb') as f:
        __model=pickle.load(f)
@app.route('/get_estimated_price',methods=['POST','GET'])
def get_estimated_price():
    brand_name=str(request.form[''])
    feactures=[]
    return __model.predict([feactures])

if __name__=="__main__":
    app.run()