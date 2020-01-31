from django.shortcuts import render
from django.http import HttpResponse

from django.http import JsonResponse

from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
import io

from .models import Activity
from .serializers import ActivitySerializer
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


def index(request):
    return HttpResponse("Bonjour la street")

def predict_activity(data):
    from sklearn.externals import joblib

    colonnes = ["respiration","ECG","ACC_c_x","ACC_c_y","ACC_c_z","ACC_w_x","ACC_w_y","ACC_w_z","temperature","EDA","BVP","WEIGHT","Gender","AGE","SKIN","HEIGHT","SPORT","label"]
    path_to_model = "./ipynb/model.sav"
    model = joblib.load(path_to_model)
    data = [[data[colonne] for colonne in colonnes]]
    medv = model.predict(data)

    return medv

@csrf_exempt
def predict(request):
    print(request)
    if request.method == 'GET':
        return JsonResponse("ERROR",status=400)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ActivitySerializer(data=data)
        if serializer.is_valid():
            data["activity"] = predict_activity(data)
            serializer = ActivitySerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data , status=201)
        return JsonResponse(serializer.errors,status=400)

