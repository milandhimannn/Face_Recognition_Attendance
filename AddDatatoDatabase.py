import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL': ""
})

ref =db.reference('Students')

data = {
    "1504":
        {
            "Name": "Akash Kashyap",
            "Course": "Btech-IT",
            "Starting_Year": 2020,
            "total_attendance":5,
            "year": 6,
            "last_attendance_time": "01-05-2023  17:00:30",
        },
    "1522":
        {
            "Name":"Milan Dhiman",
            "Course": "Btech-IT",
            "Starting_Year": 2020,
            "year": 6,
            "total_attendance": 5,
            "last_attendance_time": "01-05-2023  17:00:30",

        },
    "1560":
        {
            "Name":"Gagandeep Singh",
            "Course": "Btech-IT",
            "Starting_Year": 2020,
            "year":6,
            "total_attendance": 5,
            "last_attendance_time": "01-05-2023  17:00:30",

        }
}

for key, value in data.items():
    ref.child(key).set(value)
