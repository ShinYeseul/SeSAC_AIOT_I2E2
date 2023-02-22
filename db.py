from uuid import uuid4

from firebase_admin import firestore
from db_init import *

db = firestore.client()

doc_ref = db.collection('person').document('Name')
doc_ref.set({'Name' : 'MJ'})

doc_ref = db.collection('person').document('Face_image')
doc_ref.set({'Person' : 'picture'})

doc_ref = db.collection('person').document('Door_state')
doc_ref.set({'Time' : '00:00', 'State' : 'off'})

doc_ref = db.collection('person').document('Camera_state')
doc_ref.set({'State' : 'off'})

blob = bucket.blob('Images/' + 'dd.jpg')
blob.upload_from_filename(filename='./Images/' + 'dd.jpg')
print(blob.public_url)

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