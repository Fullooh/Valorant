import os
from dotenv import load_dotenv
import firebase_admin
from firebase_admin import credentials

# Load environment variables from the .env file
load_dotenv()

# Get the path to the service account key file from the environment variable
service_account_path = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')

# Initialize Firebase using the credentials
cred = credentials.Certificate(service_account_path)
firebase_admin.initialize_app(cred)
