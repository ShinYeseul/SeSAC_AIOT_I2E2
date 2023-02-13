import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("i2e2-7fb0d-firebase-adminsdk-oy0oa-8500a3725e.json")

app = firebase_admin.initialize_app(cred)
db = firestore.client()
print("firebase initialized...", db)
