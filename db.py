from firebase_admin import firestore

db = firestore.client()

doc_ref = db.collection('i2e2').document('Authorization')
doc_ref.set({

})