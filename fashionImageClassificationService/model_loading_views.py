import boto3
from django.core.files.storage import FileSystemStorage
import os
from django.conf import settings
from keras.models import load_model 
import environ
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

def load_model_from_s3(bucket_name, file_key):
    local_file_path = os.path.join(settings.BASE_DIR, 'xception_v4_large_08_0.894.h5')  # Path to store the downloaded model file locally
    file_exists = os.path.exists(local_file_path)
    env = environ.Env()
    environ.Env.read_env()
    if(file_exists == False):
        s3 = boto3.client('s3',
            aws_access_key_id=env('AWS_ACCESSKEY_ID'),
            aws_secret_access_key=env('AWS_SECRET_ACCESS_KEY'))
        local_file_path = os.path.join(settings.BASE_DIR, 'xception_v4_large_08_0.894.h5')  # Path to store the downloaded model file locally
        # Download the model file from S3
        s3.download_file(bucket_name, file_key, 'xception_v4_large_08_0.894.h5' )
        fs = FileSystemStorage()
        file_name = 'xception_v4_large_08_0.894.h5'



        # Load the model from the local file
    model = load_model(local_file_path)  # or the appropriate method to load your model
    
    return model
