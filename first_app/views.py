from django.shortcuts import render
import datetime
# Create your views here.
def home(request):
    d={'author ' : 'Tanvir','age':3, 'list':['python','is','fun'],
       'birthday':datetime.datetime.now(),'courses':
       [ 
           {
               'name' : 'python',
               'id':1,
               'fee' :10000,
           },
           {
               'name' : 'django',
               'id':2,
               'fee' :50000,
           },
           {
               'name' : 'java',
               'id':3,
               'fee' :1000,
           },
           


       ]}
    return render(request,'home.html',d)