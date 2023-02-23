from uuid import uuid4

from firebase_admin import firestore
from db_init import *
import RPi.GPIO as GPIO
import time

servo_pin = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin, GPIO.OUT)
pwm = GPIO.PWM(servo_pin, 50)
pwm.start(7.5)

smartdoor_state = False
authorized = 1

for cnt in range(0, 1):
    if authorized == 1:

        smartdoor_state = True

        db = firestore.client()

        doc_ref = db.collection('person').document('Name')
        doc_ref.set({'Name': 'MJ'})

        doc_ref = db.collection('person').document('Face_image')
        doc_ref.set({'Person': 'picture'})

        doc_ref = db.collection('person').document('Door_state')
        doc_ref.set({'Time': '00:00', 'State': str(smartdoor_state)})

        doc_ref = db.collection('person').document('Camera_state')
        doc_ref.set({'State': 'off'})

        # blob = bucket.blob('Images/' + 'dd1.jpg')
        # blob.upload_from_filename(filename='./Images/' + 'dd1.jpg')
        # print(blob.public_url)

        pwm.ChangeDutyCycle(12.5)
        time.sleep(3.0)

    else:

        smartdoor_state = False

        db = firestore.client()

        doc_ref = db.collection('person').document('Name')
        doc_ref.set({'Name': 'MJ'})

        doc_ref = db.collection('person').document('Face_image')
        doc_ref.set({'Person': 'picture'})

        doc_ref = db.collection('person').document('Door_state')
        doc_ref.set({'Time': '00:00', 'State': str(smartdoor_state)})

        doc_ref = db.collection('person').document('Camera_state')
        doc_ref.set({'State': 'off'})

        # blob = bucket.blob('Images/' + 'dd2.jpg')
        # blob.upload_from_filename(filename='./Images/' + 'dd2.jpg')
        # print(blob.public_url)

        pwm.ChangeDutyCycle(7.5)
        time.sleep(1.0)

smartdoor_state = False
doc_ref = db.collection('person').document('Door_state')
doc_ref.set({'Time': '00:00', 'State': str(smartdoor_state)})
pwm.ChangeDutyCycle(7.5)
time.sleep(1.0)

pwm.stop()
GPIO.cleanup()

# from uuid import uuid4

# from firebase_admin import firestore
# from db_init import *

# db = firestore.client()

# doc_ref = db.collection('person').document('Name')
# doc_ref.set({'Name' : 'MJ'})

# doc_ref = db.collection('person').document('Face_image')
# doc_ref.set({'Person' : 'picture'})

# doc_ref = db.collection('person').document('Door_state')
# doc_ref.set({'Time' : '00:30', 'State' : 'off'})

# doc_ref = db.collection('person').document('Camera_state')
# doc_ref.set({'State' : 'off'})

# blob = bucket.blob('Images/' + 'dd.jpg')
# blob.upload_from_filename(filename='./Images/' + 'dd.jpg')
# print(blob.public_url)

# import json
#
# with open('bank4.json', 'r') as f:
#     data = json.load(f)
#
# # 트랜젝션
#
# transaction = db.transaction()
# doc_ref = db.collection('customer').document('c1')
#
#
# @firestore.transactional
# def update_in_transaction(transaction, doc_ref):
#     snapshot = doc_ref.get(transaction=transaction)
#     total_amount = snapshot.get('total_amount')
#     ntotal_amount = total_amount + 1000
#
#     transaction.update(doc_ref, {
#         'total_amount': ntotal_amount
#     })
#
#     return ntotal_amount
#
#
# result = update_in_transaction(transaction, doc_ref)
# result