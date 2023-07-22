from django.apps import AppConfig
from fashionImageClassificationService.model_loading_views import load_model_from_s3  # Replace with the actual function to load your model
import boto3
import environ



class FashionimageclassificationserviceConfig(AppConfig):
    # default_auto_field = 'django.db.models.BigAutoField'

    env = environ.Env()
    environ.Env.read_env()
    name = 'fashionImageClassificationService'
    s3 = boto3.client('s3',
    aws_access_key_id=env('AWS_ACCESSKEY_ID'),
    aws_secret_access_key=env('AWS_SECRET_ACCESS_KEY'))
    print('Preloading the ML model...')
    model = load_model_from_s3('image-classification-model', 'xception_v4_large_08_0.894.h5')  # Load your model here
    print('ML model preloaded successfully!', model)
