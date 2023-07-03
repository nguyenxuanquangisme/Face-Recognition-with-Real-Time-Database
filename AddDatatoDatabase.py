import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://face-recognition-real-ti-30341-default-rtdb.firebaseio.com/"

})

ref = db.reference('Student')
data = {
    "170099":
        {
            "name": "Nguyen Xuan Quang",
            "major": "AI",
            "starting_year":2021,
            "total_attendance":6,
            "standing":"G",
            "year":3,
            "last_attendance_time": "2023-07-03 20:09:34"
        },
    "321654":
        {
            "name": "Murtaza Hassan",
            "major": "Robotics",
            "starting_year": 2020,
            "total_attendance": 8,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2023-07-03 20:09:34"
        },
    "852741":
        {
            "name": "Emly Blunt",
            "major": "Economics",
            "starting_year": 2019,
            "total_attendance": 10,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2023-07-03 20:09:34"
        },
    "963852":
        {
            "name": "Elon Musk",
            "major": "Physics",
            "starting_year": 2014,
            "total_attendance": 3,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2023-07-03 20:09:34"
        }
}


for key,value in data.items():
    ref.child(key).set(value)