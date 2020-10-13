import os

basedir = os.path.abspath(os.path.dirname(__file__))
# SQLALCHEMY_DATABASE_URI = 'sqlite' + os.path.join(basedir, app.db)


API_URL = "https://www.googleapis.com/geolocation/v1/geolocate?key="
API_KEY = "AIzaSyC42UqAekJzZurXayShCHcHKG6WZXVuvBk"
API_CALLBACK = "myMap"