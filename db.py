from uuid import uuid4

from firebase_admin import firestore
from db_init import *

db = firestore.client()

doc_ref = db.collection('i2e2').document('Authorized')
doc_ref.set({
    'Number':'1',
    'Time_stamp':'2022',
    'Door_Status':'o',
    'Face_Image':'dfd',
    'Name':'name',
    'Monitoring_Camera':'df'
})

doc_ref = db.collection('i2e2').document('Unauthorized')
doc_ref.set({
    'Number':'1',
    'Time_stamp':'2022',
    'Door_Status':'o',
    'Face_Image':'dfd',
    'Unknown':'name',
    'Monitoring_Camera':'df'
})

blob = bucket.blob('Images/' + 'dd.jpg')
blob.upload_from_filename(filename='./Images/' + 'dd.jpg')
print(blob.public_url)