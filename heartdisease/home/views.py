import joblib
from django.shortcuts import render
import joblib

def index(request):
    return render(request, "index.html")
def result(request):
    cls = joblib.load('heartpredict.sav')

    lis = []

    lis.append(request.GET['age'])
    lis.append(request.GET['sex'])
    lis.append(request.GET['cp'])
    lis.append(request.GET['trestbps'])
    lis.append(request.GET['chol'])
    lis.append(request.GET['fbs'])
    lis.append(request.GET['restecg'])
    lis.append(request.GET['thalach'])
    lis.append(request.GET['exang'])
    lis.append(request.GET['oldpeak'])
    lis.append(request.GET['slope'])
    lis.append(request.GET['ca'])
    lis.append(request.GET['thal'])

    ans = cls.predict([lis])
    return render(request, 'result.html',{'ans':ans})


# Create your views here.
