import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import storage

PROJECT_ID = "i2e2-7fb0d"
cred = credentials.Certificate("i2e2-7fb0d-firebase-adminsdk-oy0oa-8500a3725e.json")

default_app = firebase_admin.initialize_app(cred, {
    'storageBucket': f"{PROJECT_ID}.appspot.com"
})

bucket = storage.bucket()

print("firebase initialized...", default_app)
