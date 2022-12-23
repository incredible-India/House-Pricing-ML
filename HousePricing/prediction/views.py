from django.shortcuts import render,HttpResponse
import json
import os
# Create your views here.
def index(request):

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
        
    
    return render(request, 'prediction/prediction.html',{
        'locations' : locations['data_columns'][3:],
        'sqft':sqft['data_columns'],
        'bath':bath['data_columns'],
        'bhk':bhk['data_columns'],
    })