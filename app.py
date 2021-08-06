import itertools

# import admin as admin
# from idlelib import tooltip
from tempfile import mkdtemp

import firebase_admin
import pyrebase
import schedule as schedule
from flask import render_template, Flask, redirect
from firebase_admin import credentials, firestore
from flask import *
from flask import Flask, render_template, session, request, redirect, flash, get_template_attribute, url_for
import random
import string
import folium
from datetime import datetime
import time




# ---------------------------firestore Database---------------------

cred = credentials.Certificate("serviceAccountkey.json")
firebase_admin.initialize_app(cred)
fdb = firestore.client()  # this connects to our Firestore database
# collection = db.collection('newslot')
# doc = collection.document('EvhfUH2TdOhurpYfq5h0qgIO27c2')
# res = doc.get().to_dict()
# print(res)


# val=[]
# docss = fdb.collection('newslot').document('6u87X3fFLdTRvAwLaGsxwbD6sK22')
# docs=docss.get()
# print(docs.to_dict())
# print(docs.to_dict().keys())
# print(docs.to_dict().values())
# for i in docs.to_dict():
#     val=i
# print("quwyetu",val)
#






# if 'parking details' in docs.to_dict().keys():
#     print('found')
# else:
#     print('Not found')


# do=docs.to_dict()
# key_list = list(do.keys())
# val_list = list(do.values())
# position = key_list.index('sample')
# print(val_list[position])

# x = fdb.collection("newslot")
# query = x.order_by("uid").limit_to_last(2)
# results = query.get()
# print(results)


# val=[]
# fieldValue = admin.firestore.FieldValue
# docss = fdb.collection('newslot').document('details')
# print(docss.to_dict())
# remov = docss.update({ 'sample': fieldValue.delete() });
# print(docss.to_dict())





# collection = fdb.collection('newslot').document('6u87X3fFLdTRvAwLaGsxwbD6sK22')  # opens 'places' collection
# result = collection.get(field_paths={'uid'}).to_dict()
# print(str(list(result.values())))






# result=list(itertools.chain(city,contact))
# print(result)
# zi = list(zip(a))
# print("zzzzzzzzzzzzzzzzzz", zi)
# for i in zi:
#     print(i)
# print(list(itertools.chain.from_iterable(a)))
# print(z)
    # val.append(i)
    # for j in i:
    #     print(j)
# print(val)



val = []
def rentalval(value):
    val.clear()
    docss = fdb.collection('newslot').document(value)
    # d = docss.get().to_dict()
    # print(d)
    city = docss.get(field_paths={'city'}).to_dict()
    contact = docss.get(field_paths={'contact'}).to_dict()
    latitude = docss.get(field_paths={'latitude'}).to_dict()
    longitude = docss.get(field_paths={'longitude'}).to_dict()
    price = docss.get(field_paths={'price'}).to_dict()
    spots = docss.get(field_paths={'spots'}).to_dict()
    title = docss.get(field_paths={'title'}).to_dict()
    uid = docss.get(field_paths={'uid'}).to_dict()
    city = (str(list(city.values())))
    contact = (str(list(contact.values())))
    latitude = (str(list(latitude.values())))
    longitude = (str(list(longitude.values())))
    price = (str(list(price.values())))
    spots = (str(list(spots.values())))
    title = (str(list(title.values())))
    uid = (str(list(uid.values())))
    print(city, contact, latitude, longitude, price, spots, title, uid)

    le = len(city)
    city = city[2:le - 2]
    print(city)
    val.append(city)

    le = len(contact)
    contact = contact[2:le - 2]
    print(contact)
    val.append(contact)

    le = len(latitude)
    latitude = latitude[1:le - 1]
    print(latitude)
    val.append(latitude)

    le = len(longitude)
    longitude = longitude[1:le - 1]
    print(longitude)
    val.append(longitude)

    le = len(spots)
    spots = spots[1:le - 1]
    print(spots)
    val.append(spots)

    le = len(price)
    print(price)
    price = price[2:le - 2]
    print(price)
    val.append(price)

    le = len(title)
    title = title[2:le - 2]
    print(title)
    val.append(title)

    le = len(uid)
    uid = uid[2:le - 2]
    print(uid)
    val.append(uid)

    return city,contact,latitude,longitude,spots,price,title,uid


rfidval = []

def rfid_val(value):
    rfidval.clear()
    docs = fdb.collection('newvehicle').document(value)
    # d = docss.get().to_dict()
    # print(d)
    email = docs.get(field_paths={'email'}).to_dict()
    city = docs.get(field_paths={'city'}).to_dict()
    brand = docs.get(field_paths={'brand'}).to_dict()
    regNumber = docs.get(field_paths={'regNumber'}).to_dict()
    category = docs.get(field_paths={'category'}).to_dict()
    contact = docs.get(field_paths={'contact'}).to_dict()
    pincode = docs.get(field_paths={'pincode'}).to_dict()
    uid = docs.get(field_paths={'uid'}).to_dict()
    email = (str(list(email.values())))
    city = (str(list(city.values())))
    brand = (str(list(brand.values())))
    regNumber = (str(list(regNumber.values())))
    category = (str(list(category.values())))
    contact = (str(list(contact.values())))
    pincode = (str(list(pincode.values())))
    uid = (str(list(uid.values())))
    print(email, city, brand, regNumber, category, contact, pincode, uid)
    res = ''.join(random.choices(string.ascii_uppercase + string.digits, k=2)) + ' ' + ''.join(
        random.choices(string.ascii_uppercase + string.digits, k=2)) + ' ' + ''.join(
        random.choices(string.ascii_uppercase + string.digits, k=2)) + ' ' + ''.join(
        random.choices(string.ascii_uppercase + string.digits, k=2))

    le = len(email)
    email = email[2:le - 2]
    print(email)
    rfidval.append(email)

    le = len(city)
    city = city[2:le - 2]
    print(city)
    rfidval.append(city)

    le = len(brand)
    brand = brand[2:le - 2]
    print(brand)
    rfidval.append(brand)

    le = len(regNumber)
    regNumber = regNumber[2:le - 2]
    print(regNumber)
    rfidval.append(regNumber)

    le = len(category)
    category = category[2:le - 2]
    print(category)
    rfidval.append(category)

    le = len(contact)
    contact = contact[2:le - 2]
    print(contact)
    rfidval.append(contact)

    le = len(pincode)
    pincode = pincode[2:le - 2]
    print(pincode)
    rfidval.append(pincode)



    le = len(uid)
    uid = uid[2:le - 2]
    print(uid)
    rfidval.append(uid)
    rfidval.append(res)

    return email, city, brand, regNumber, category, contact, pincode, uid , res



# ------------------------------Realtime Database-----------------------------
config = {
    'apiKey': "AIzaSyB7VFg9QRuxubO-bVB-AbYKERASTUbJWW8",
    'authDomain': "intellipark-89631.firebaseapp.com",
    'databaseURL': "https://intellipark-89631-default-rtdb.firebaseio.com",
    'projectId': "intellipark-89631",
    'storageBucket': "intellipark-89631.appspot.com",
    'messagingSenderId': "1019669593876",
    'appId': "1:1019669593876:web:e9b896b954ec249b290c01"
};

firebase= pyrebase.initialize_app(config)
rdb = firebase.database()
# -------------------------------------------------------------------

# db.child("names").push({"names":"Suraj"})
# db.child("names").child("name").update({"name":"Suraj"})

# users= db.child("names").child("name").get()
# print(users.val())
data =  { 'Name': 'Au space',
          'From':"  9:00 AM ",
          'To':"  11:00 PM ",
          'Priority':"1",

          }

# slots=db.child("Slots2").child("1001").child("101").child("1").update(data)
# print(slots)

# --------------------------------------------------------------------------------------
# extract all parking space name and locaction
# title_list = []
# lat_list=[]
# lon_list=[]
# parking = fdb.collection('parking').stream()
# for doc in parking:
#     docs = fdb.collection('parking').document(doc.id)
#     title = docs.get(field_paths={'title'}).to_dict()
#     latitude = docs.get(field_paths={'coordinate.latitude'}).to_dict()
#     longitude = docs.get(field_paths={'coordinate.longitude'}).to_dict()
#     lat = (str(list(latitude.values())))
#     lon = (str(list(longitude.values())))
#     title = (str(list(title.values())))
#     lenlat =  len(lat)
#     lenlon = len(lon)
#     lentitle = len(title)
#     lat = lat[13:lenlat - 2]
#     lon = lon[14:lenlon - 2]
#     title = title[2:lentitle-2]
#     title_list.append(title)
#     lat_list.append(lat)
#     lon_list.append(lon)








    # le = len(coordinate)
    # lat = coordinate[14:le - 26]
    # lon = coordinate[37:le - 2]
    #
    # print("lot",lat)
    # print("LONG",lon)


# ------------------------------------------------------------------------------------------



app = Flask(__name__)

@app.route('/',methods=["GET","POSt"])
def login():
    if request.method=="POST":
        username=request.form.get("username")
        password = request.form.get("password")
        if username == "hirespacz" and password == "hirespacz":
            return redirect("/dashboard")
        return redirect('/')
    return render_template("login.html")

@app.route('/dashboard')
def home():
    userdoc = fdb.collection('users').stream()
    parkingdoc = fdb.collection('parking').stream()
    emails = []
    spacename=[]
    for users in userdoc:
        email = fdb.collection('users').document(users.id)
        email = email.get(field_paths={'email'}).to_dict()
        email = (str(list(email.values())))
        le = len(email)
        email = email[2:le - 2]
        emails.append(email)
        print(emails)
    count = len(emails)


    for space in parkingdoc:
        space = fdb.collection('parking').document(space.id)
        space = space.get(field_paths={'title'}).to_dict()
        space = (str(list(space.values())))
        le = len(space)
        space = space[2:le - 2]
        spacename.append(email)
        print(spacename)
    spacecount = len(spacename)




    return render_template("dashboard.html",count=count,spacecount=spacecount)

@app.route('/map')
def map():
    title_list = []
    lat_list = []
    lon_list = []
    parking = fdb.collection('parking').stream()
    for doc in parking:
        docs = fdb.collection('parking').document(doc.id)
        title = docs.get(field_paths={'title'}).to_dict()
        latitude = docs.get(field_paths={'coordinate.latitude'}).to_dict()
        longitude = docs.get(field_paths={'coordinate.longitude'}).to_dict()
        lat = (str(list(latitude.values())))
        lon = (str(list(longitude.values())))
        title = (str(list(title.values())))
        lenlat = len(lat)
        lenlon = len(lon)
        lentitle = len(title)
        lat = lat[13:lenlat - 2]
        lon = lon[14:lenlon - 2]
        title = title[2:lentitle - 2]
        print(title,lat,lon)
        title_list.append(title)
        lat_list.append(lat)
        lon_list.append(lon)
        map = folium.Map(location=[lat, lon], zoom_start=11)
        feature_group = folium.FeatureGroup("Locations")
        for lat,lon,title in zip(lat_list,lon_list,title_list):
            feature_group.add_child(folium.Marker(location=[lat, lon], popup=title))
            map.add_child(feature_group)
            map.save(outfile="templates/mmap.html")


    return render_template('map.html')


@app.route('/rental')
def rental():
    documents = fdb.collection(u'newslot').stream()
    docs = []
    emailval=[]

    for doc in documents:
        print(f'{doc.id}')
        docs.append(doc.id)
        docss = fdb.collection('users').document(doc.id)
        print('uiwqie',docss.get().to_dict())
        email = docss.get(field_paths={'email'}).to_dict()
        email = (str(list(email.values())))
        email=email[2:len(email)-2]
        emailval.append(email)


    print(emailval)
    print(docs)


    return render_template("rental.html",docs=docs,email=emailval)




@app.route('/request_rental/<value>')
def request_rental(value):
    print("request route: ",value)
    rentalval(value)
    print(val)
    return render_template("request.html",val=val)


@app.route('/delete_rental_space/<value>')
def deleterentalspace(value):
    fdb.collection('newslot').document(value).delete()
    return redirect('/rental')



@app.route('/submit_rental_space', methods=["POST"])
def submitrentalspace():

    city = request.form.get("city")
    contact = request.form.get("contact")
    latitude = request.form.get("latitude")
    longitude = request.form.get("longitude")
    price = request.form.get("price")
    spots = request.form.get("spots")
    slotdata={
        'city': city,
        'contact': contact,
        'price': price,
        'spots': spots,
        'title': val[6],
        'description': '',
        'etime': '',
        'dtime': '',
        'itime': firestore.SERVER_TIMESTAMP,
        'rating': '',
        'status': True,
        'coordinate':{
            'latitude': latitude,
            'longitude': longitude,

        }
    }


    fdb.collection('parking').document(val[7]).set(slotdata)


    fdb.collection('newslot').document(val[7]).delete()



    return redirect('/rental')


@app.route('/rfid')
def rfid():
    # documents = fdb.collection(u'newvehicle').stream()
    docs = []
    emailval = []

    parking = fdb.collection('newvehicle').stream()
    for doc in parking:
        docss = fdb.collection('newvehicle').document(doc.id)
        docs.append(doc.id)
        email = docss.get(field_paths={'email'}).to_dict()
        email = (str(list(email.values())))
        email = email[2:len(email) - 2]
        emailval.append(email)


    return render_template("rfid.html", docs=docs, email=emailval)




@app.route('/submit_rfid',methods=["POST"])
def submit_rfid():
    email = request.form.get("email")
    region = request.form.get("region")
    regnumber = request.form.get("regnumber")
    rfidno = request.form.get("rfidno")
    brand = request.form.get("brand")
    category = request.form.get("category")
    pincode= request.form.get("pincode")
    contact = request.form.get("contact")
    uid= request.form.get("uid")

    print(email,regnumber,"rfid",rfidno,region,brand,category,pincode,contact,uid)

    rfid_data = {
        'email': email,
        'region': region,
        'rfidno': rfidno,
        'brand': brand,
        'category': category,
        'pincode':pincode,
        'contact':contact,
        'regnumber':regnumber,
        'accepted_time': firestore.SERVER_TIMESTAMP,
        'uid':uid,

    }
    fdb.collection('myvehicle').document(uid).set(rfid_data)
    fdb.collection('newvehicle').document(uid).delete()

    return redirect('/rfid')

@app.route('/delete_rfid/<delrfid>')
def delete_rfid(delrfid):
    fdb.collection('newvehicle').document(delrfid).delete()
    return redirect('/rfid')

@app.route('/rfid_details/<rfidnum>',methods=["GET","POST"])
def rfid_details(rfidnum):
    print("request route::::: ", rfidnum)

    rfid_val(rfidnum)
    print(rfidval)

    return render_template("rfid_details.html", val=rfidval)

@app.route('/table')
def table():
    parkingdoc = fdb.collection('parking').stream()
    spacedocs=[]
    emaillist = []
    titlelist = []
    pricelist = []
    ratinglist = []
    for doc in parkingdoc:
        spacedocs.append(doc.id)
        docss = fdb.collection('users').document(doc.id)
        useremail = docss.get(field_paths={'email'}).to_dict()
        useremail = (str(list(useremail.values())))
        useremail = useremail[2:len(useremail) - 2]
        # --------------------------------------------------
        parkdetails = fdb.collection('parking').document(doc.id)
        title = parkdetails.get(field_paths={'title'}).to_dict()
        title = (str(list(title.values())))
        title = title[2:len(title) - 2]

        price = parkdetails.get(field_paths={'price'}).to_dict()
        price = (str(list(price.values())))
        price = price[2:len(price) - 2]

        rating = parkdetails.get(field_paths={'rating'}).to_dict()
        rating= (str(list(rating.values())))
        rating  = rating [1:len(rating) - 1]


        emaillist.append(useremail)
        titlelist.append(title)
        pricelist.append(price)
        ratinglist.append(rating)



    return render_template("tables.html",emaillist=emaillist,titlelist=titlelist,pricelist=pricelist,ratinglist=ratinglist)

@app.route('/user')
def user():

    userdoc = fdb.collection('users').stream()
    emails = []
    for users in userdoc:
        emaill = fdb.collection('users').document(users.id)

        email = emaill.get(field_paths={'email'}).to_dict()

        email = (str(list(email.values())))

        le = len(email)
        email = email[2:le - 2]
        emails.append(email)
        print(emails)



    return render_template("user.html",emails=emails)


@app.route('/userprofile')
def userprofile():
    return render_template("userprofile.html")




@app.route('/privacy')
def privacy():
    return render_template("privacy.html")

@app.route('/tnc')
def tnc():
    return render_template("tnm.html")




if __name__ == '__main__':

    app.run()
