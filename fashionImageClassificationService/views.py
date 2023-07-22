from django.shortcuts import render

# Create your views here.
from keras.models import load_model 
from keras.preprocessing import image 
from keras.preprocessing.image import img_to_array, load_img 
from django.http import JsonResponse
import numpy as np 
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from keras.preprocessing.image import load_img
from keras.applications.xception import preprocess_input
import boto3
from django.core.files.storage import FileSystemStorage
import os
from fashionImageClassificationService.apps import FashionimageclassificationserviceConfig

""" ... 
    def index(): 
    You can download the entire code from this repository
    ...
""" 


labels = {
    0: 'dress',
    1: 'hat',
    2: 'longsleeve',
    3: 'outwear',
    4: 'pants',
    5: 'shirt',
    6: 'shoes',
    7: 'shorts',
    8: 'skirt',
    9: 't-shirt'
}
image_size = (299, 299)

@csrf_exempt
def predImg(request):
    if request.method == 'POST': 
        context = {} 
        uploaded_file= request.FILES['img'] 
        fs = FileSystemStorage() 
        name = fs.save(uploaded_file.name, uploaded_file) 
        context["url"] = fs.url(name) 
        testimage = '.'+context["url"] 
        img = image.load_img(testimage,  target_size=image_size) 
        x = np.array(img)
        X = np.array([x])
        X = preprocess_input(X)
        print(FashionimageclassificationserviceConfig.name)
        print(FashionimageclassificationserviceConfig)
        model = FashionimageclassificationserviceConfig.model
        print(model)
        if(model != None):
            pred = model.predict(X)
            
            context['predictedClass'] = labels[np.argmax(pred[0])] 
            context['probability'] = "{:.2f}".format(round(np.max(pred), 2)*100)
        else:
            return JsonResponse({'error': "Model didn't load Properly"})

        print("Delete file after execution", uploaded_file.name)
        fs.delete(uploaded_file.name)
        
    return JsonResponse({'predictClass': labels[np.argmax(pred[0])] })