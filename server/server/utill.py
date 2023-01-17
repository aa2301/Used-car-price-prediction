import pickle
import numpy as np
__model=None
def get_estimated_price(brand_name,car_name,Kilometers_Driven,Mileage,Year,Fuel,Transmission_given):
    feactures=[]
    return __model.predict([feactures])
def load_artifacts():
    global __model
    with open("D:\My\projects\sp ml\UCPP\server\artifacts\Used_car_price_prediction",'rb') as f:
        __model=pickle.load(f)