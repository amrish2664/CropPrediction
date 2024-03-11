from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
import pickle
import os
import pickle
import numpy as np
def predict_crop(request):
    if request.method == 'POST':
        n = float(request.POST['n'])
        p = float(request.POST['p'])
        k = float(request.POST['k'])
        temperature = float(request.POST['temperature'])
        humidity = float(request.POST['humidity'])
        ph = float(request.POST['ph'])
        r = float(request.POST['r'])
        current_directory= os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        file_path = os.path.join(current_directory, 'model.pkl')       
        model = pickle.load(open(file_path, 'rb'))
        prediction = model.predict(np.array([[n, p, k, temperature, humidity, ph,r]]))
        return render(request, 'index.html', {'prediction': prediction[0]})
    return render(request, 'index.html')