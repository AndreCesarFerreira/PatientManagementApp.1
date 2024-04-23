from pymongo import MongoClient
from patientInfo import *
import datetime

uri = "mongodb+srv://JackWarlenstein:cOb70cc5QV@cluster0.vmy7zgj.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri)

db = client["MedicalApp"]
patient_list = db["Patients"]
doctor_list = client["Doctors"]


# Send a ping to confirm a successful connection
def connect_to_mongodb():
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)

# Methode to convert the date into an apropriate formate
def convert_date(date):
    return datetime.datetime.strftime(date, '%Y/%m/%d')  # YYYY/MM/DD


def insert_post_in_mongodb(post):
    patient_list.insert_one(post)


def retrieve_last_id_mongodb():
    return patient_list.find().sort('_id', -1).limit(1)[0]['_id']


def retrieve_info_mongodb():
    info = patient_list.find({})
    list_info = []
    for x in info:
        list_info.append(x)
    return list_info


def create_patient_post(patient_info):
    patient_date_of_birth = patient_info.date_of_birth
    new_id = int(retrieve_last_id_mongodb()) + 1
    post = {"_id": new_id,
            "First Name": patient_info.first_name,
            "Last Name": patient_info.last_name,
            "Gender": patient_info.gender,
            "Date of Birth": patient_date_of_birth,
            #"Age": patient_info.age,
            "Height": patient_info.height,
            "Weight": patient_info.weight,
            "Is taking medication?": patient_info.is_taking_medication,
            "Is allergic to meds?": patient_info.is_allergic_to_meds,
            "Is blood donor?": patient_info.is_blood_donor,
            "Surgery done?":  patient_info.surgery_done,
            "How many?": patient_info.how_many}
    return post
