import boto3
from django.core.files.storage import FileSystemStorage
import os
from django.conf import settings
from keras.models import load_model 

def load_model_from_s3(bucket_name, file_key):
    local_file_path = os.path.join(settings.BASE_DIR, 'xception_v4_large_08_0.894.h5')  # Path to store the downloaded model file locally
    file_exists = os.path.exists(local_file_path)
    if(file_exists == False):
        local_file_path = os.path.join(settings.BASE_DIR, 'xception_v4_large_08_0.894.h5')  # Path to store the downloaded model file locally
        val = s3.head_object(Bucket=bucket_name, Key=file_key)
        print("Rushil", val)
        # Download the model file from S3
        s3.download_file(bucket_name, file_key, 'xception_v4_large_08_0.894.h5' )
        fs = FileSystemStorage()
        file_name = 'xception_v4_large_08_0.894.h5'



        # Load the model from the local file
    model = load_model(local_file_path)  # or the appropriate method to load your model
    
    return model
