import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("livbus-ae064-firebase-adminsdk-519sl-6254005930.json")
firebase_admin.initialize_app(cred,{
    'databaseURL' : "https://livbus-ae064-default-rtdb.firebaseio.com/"
    })

i=0
while True:
    ref = db.reference('/{0}'.format(i))
    data = {
        "name" : "Hari-{0}".format(i+1),
        "id" : "100{0}".format(i+1)
    }
    ref.set(data)
    i+=1
    if i==5:
        break