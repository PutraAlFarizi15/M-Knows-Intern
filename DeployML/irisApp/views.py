from django.shortcuts import render
from joblib import load

model = load('./saveModels/model.joblib')

# Create your views here.
def predictor(request):
    return render(request, 'main.html')

def formInfo(request):
    sepal_length = request.GET['sepal_length']
    sepal_width = request.GET['sepal_width']
    petal_length = request.GET['petal_length']
    petal_width = request.GET['petal_width']
    y_pred = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])
    if y_pred[0] == 0:
        y_pred = 'Setosa'
    elif y_pred[0] == 1:
        y_pred = 'Verscicolor'
    else:
        y_pred = 'Virginica'
    
    return render(request, 'result.html', {'result' : y_pred})