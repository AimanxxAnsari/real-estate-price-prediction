import json
import pickle
import numpy as np
 

__location = None
__data_columns = None
__model = None

def estimated_price(location, sqft, bhk, bath):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk

    if loc_index >= 0:
        x[loc_index] = 1

    return round(__model.predict([x])[0], 2)

def get_location():
    return __location

def load_saved():
    print('loading saved info..')
    global __data_columns
    global __location 
    global __model

    with open('../model/columns.json', 'r') as file:
        __data_columns = json.load(file)['data_columns']
        __location = __data_columns[3:]

    with open('../model/blr-price-model.pickle', 'rb') as file:
        __model = pickle.load(file)

    print('saving info completed..')

if __name__  == '__main__':
    load_saved()
    print(get_location())
    print(estimated_price('1st Phase JP Nagar', 1000, 3, 2))
    print(estimated_price('1st Phase JP Nagar', 1000, 2, 2))
    print(estimated_price('abbigere', 1200, 3, 3))