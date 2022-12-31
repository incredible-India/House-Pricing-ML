from django.shortcuts import render,HttpResponse
import json
from django.contrib import messages
from django.views import View
import pickle
import numpy as np
# Create your views here.

__MLmodel = None
locations = None
sqft =None
bath = None
bhk= None
#location from bengaluru test datsets
with open('./prediction/citilocation/columns.json') as cl:
    locations = json.loads(cl.read())

    #square foot info from test datsets
with open('./prediction/citilocation/sqft.json') as cs:
    sqft = json.loads(cs.read())
    #bathrooms info from test datsets
with open('./prediction/citilocation/bath.json') as ps:
    bath = json.loads(ps.read())
    #bedrooms info from test datsets
with open('./prediction/citilocation/bhk.json') as bs:
    bhk = json.loads(bs.read())

with open('./prediction/ML_Model_and_datasets/Mymodel.pickle','rb') as LM:
    __MLmodel = pickle.load(LM)





#using our trained model price prediction
#here we use our traine model is in ./House Pricing BNG\HousePricing\prediction\ML Model and datasets
#for more info u can check that directory and open DHouse Pricing BNG\HousePricing\prediction\ML_Model_and_datasets\.ipynb_checkpoints\Housing Pricing-checkpoint.ipynb with jupyter notebook
def CalculateEstimatePrice(location,sqft,bath,bhk):

    global locations
    global __MLmodel

    
    
    try:
        #checking the loacation as columns in my datsets
        loc_index = locations['data_columns'][3:].index(location)
    except:
        loc_index = -1
  
    xt = np.zeros(len(locations['data_columns']))
    xt[0] = sqft
    xt[1] = bath
    xt[2] = bhk
    if loc_index >= 0:
        xt[loc_index] = 1

    return __MLmodel.predict([xt])[0]


class index(View):

    def get(self, request):

        global location, sqft,bath,bhk

        return render(request, 'prediction/prediction.html',{
            'locations' : locations['data_columns'][3:],
            'sqft':sqft['data_columns'],
            'bath':bath['data_columns'],
            'bhk':bhk['data_columns'],
            })

    def post(self, request):

        userlocation = request.POST.get('location')
        usersqft = request.POST.get('sqft')
        userbath = request.POST.get('bath')
        userbhk = request.POST.get('bhk')


        #this is function which calculate the home price using our trained model ,and our trained model take argument as loaction,square fott,bath ,bhk (in order)
        estimatePrice = CalculateEstimatePrice(userlocation, usersqft,userbath, userbhk)

        finalPrice = round(estimatePrice,2)






        return render(request, 'prediction/finalresult.html',{

            'data' : finalPrice,
            'location' : userlocation,
            'sqft':usersqft,
            'bath' : userbath,
            'bhk' : userbhk
        })