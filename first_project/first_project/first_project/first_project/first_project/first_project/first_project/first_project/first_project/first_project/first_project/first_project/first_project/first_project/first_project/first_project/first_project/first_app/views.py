from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
import random
# from flask import Flask
# app = Flask(__name__)
# Create your views here.
# @app.route('/abc')
# def index(request):
#     my_dict = {'insert_me':"Software development internship exercise"}
#     return render(request,'first_app/index.html',context=my_dict)

def index1(request):

    cityNames = ["Boston", "New York", "Paris", "Rome", "Cambridge", "London", "Amsterdam", "Manhattan", "Denvers", "Brighton", "Quincy", "Braintree", "Somerville", "New Delhi", "Mumbai"];
    name = (random.choice(cityNames))
    # print(" Random City Name -->  " + name)
        # return render(request,'first_app/index.html',context=name)
        # name = HttpResponse('')
    return HttpResponse(name)
