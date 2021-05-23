import firebase_admin
from firebase_admin import credentials
from firebase_admin import initialize_app
from firebase_admin import db

cred = credentials.Certificate('jamhacks-7c86a-firebase-adminsdk-74i1n-54d674b4bd.json')
app = initialize_app(cred, {
	'databaseURL':'https://jamhacks-7c86a-default-rtdb.firebaseio.com/'
	})

ref = db.reference("/Users")

def reference():
    return ref