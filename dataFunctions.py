# Data and data manipulation functions
from time import strptime

import PySimpleGUI as sg
from patientInfo import Patient
from datetime import datetime
from mongoDB import *

# List of patients for our initial table data
"""patients = [
    Patient("André", "César", "Male", datetime(1994, 7, 30), 1.75, 95, True, False, True, False, 0),
    Patient("Robert", "Patt", "Male", datetime(1972, 5, 22), 1.65, 65, True, False, True, True, 2),
    Patient("Julian", "Lion", "Male", datetime(1985, 3, 16), 1.82, 120, False, True, False, False, 0),
    Patient("Alim", "Mar", "Female", datetime(1995, 2, 22), 1.60, 180, False, True, False, True, 10)
]"""

patients = retrieve_info_mongodb()
# print("Values retrieve from mongoDB:\n", patients)


""" (Original method before MongoDB) Returns a list with all patients' info
def convert_patients_to_table_data():
    patients_data = []
    for patient in patients:
        strings = patient.convert_values_to_strings()
        patients_data.append(strings)
        #patients_data.append(patient)
    return patients_data
"""

# Method to convert the info retrieve from MongoDB into usable data by the program
def convert_mongodb_info_to_patient():
    list_of_patients = []
    for patient in patients:
        first_name = patient['First Name']
        last_name = patient['Last Name']
        gender = patient['Gender']
        date_of_birth = patient['Date of Birth']
        height = patient['Height']
        weight = patient['Weight']
        is_taking_meds = patient['Is taking medication?']
        is_allergic_to_meds = patient['Is allergic to meds?']
        is_blood_donor = patient['Is blood donor?']
        surgery_done = patient['Surgery done?']
        how_many = patient['How many?']
        new_patient = Patient(first_name, last_name, gender, date_of_birth, height, weight, is_taking_meds, is_allergic_to_meds, is_blood_donor, surgery_done, how_many)
        list_of_patients.append(new_patient)
    return list_of_patients

# Method to convert the patients to table data
def convert_patients_to_table_data():
    patient_list = convert_mongodb_info_to_patient()
    patients_data = []
    for patient in patient_list:
        strings = patient.convert_values_to_strings()
        patients_data.append(strings)
        #patients_data.append(patient)
    return patients_data


# Validates the input and attemts to create a patient, returns True if patient created successfully and False otherwise
def try_to_create_patient(id_patient, first_name, last_name, gender, date_of_birth, height, weight, is_taking_medication, is_allergic_to_medication, is_blood_donor, any_surgery_done, how_many):

   validation_result = validate(first_name, last_name, date_of_birth, height, weight)
   if validation_result[0]:
       if gender == "True":
           gender = "Male"
       else:
           gender = "Female"

       date_of_birth = strptime(date_of_birth, '%Y/%m/%d')
       height = float(height)
       weight = float(weight)
       if how_many == '':
           how_many = 0
       else:
            how_many = int(how_many)
       patient = Patient(first_name, last_name, gender, date_of_birth, height, weight, is_taking_medication, is_allergic_to_medication, is_blood_donor, any_surgery_done, how_many)
       """
       Bit of code to check if the information being passed to the Patient is all correct and there to be inserted.
       print(patient.convert_values_to_strings())
       """
       patients.append(patient)
       return True
   else:
       error_message = generate_error_message(validation_result[1])
       sg.popup(error_message)

# Methode to validate the value of first_name, last_name, date_of_birth, height and weight.
def validate(first_name, last_name, date_of_birth, height, weight):
    is_valid = True
    values_invalid = []

    if len(first_name) == 0:
        values_invalid.append('First Name')
        is_valid = False

    if len(last_name) == 0:
        values_invalid.append('Last Name')
        is_valid = False

    #date_of_birth = datetime.strptime(date_of_birth, '%Y/%m/%d')
    #date_now = datetime.now()
    #date_now = datetime.strptime(date_now, '%Y/%m/%d')
    """if date_of_birth > datetime.strftime(datetime.now(), '%Y/%m/%d'):
        values_invalid.append('Date of Birth')
        is_valid = False
    el"""
    if date_of_birth == '':
        values_invalid.append('Date of Birth')
        is_valid = False

    if height == '':
        values_invalid.append('Height')
        is_valid = False

    if weight == '':
        values_invalid.append('Weight')
        is_valid = False

    result = [is_valid, values_invalid]
    return result

# Method to generate an error message in case something is missing in the Patient form
def generate_error_message(values_invalid):
    error_message = "Invalid Inputs:"
    for value_invalid in values_invalid:
        error_message += ("\n" + value_invalid)
    return error_message
