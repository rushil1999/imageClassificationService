# preload_model.py

from django.core.management.base import BaseCommand
from fashionImageClassificationService.model_loading_views import load_model_from_s3  # Replace with the actual function to load your model
import boto3
class Command(BaseCommand):
    help = 'Preloads the ML model into memory'

    def handle(self, *args, **options):
        s3 = boto3.client('s3',
        aws_access_key_id="AKIAVQATD7RUYQL26THE",
        aws_secret_access_key="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")
        self.stdout.write('Preloading the ML model...')
        model = load_model_from_s3('image-classification-model', 'xception_v4_large_08_0.894.h5')  # Load your model here
        self.stdout.write('ML model preloaded successfully!')
        setattr(Command, 'model', model)  # Save the model as an attribute of the Command class
