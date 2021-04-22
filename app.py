import firebase_admin
from firebase_admin import credentials, firestore
import flask
from flask import abort,jsonify,request,redirect
import json
import requests

app=flask.Flask(__name__)

cred = credentials.Certificate("zoggy-9b28a-firebase-adminsdk-o2rhr-9f811023eb.json")
firebase_admin.initialize_app(cred)
store=firestore.client()

@app.route('/addRESTAURANT',methods=['POST'])
def addRestaurant():
    data = request.get_json(force=True)

    dit={}
    dit["name"]=data.get("name")
    dit["mobile"]=data.get("mobile")
    dit["address"]=data.get("address")
    dit["location"]={"lat":data.get("lat"),"lng":data.get("lng")}
    dit["type"]=data.get("typ")
    dit["Rest_id"]=data.get("rest_id")
    dit["imageurl"]=data.get("imageurl")
    dit["createdAt"]=firestore.SERVER_TIMESTAMP

    store.collection("Restaurant").add(dit)
    return jsonify({"Response":200, })


if __name__=='__main__':
    app.run(host='0.0.0.0',port=5001,debug=False)