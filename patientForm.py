# Form to create and save a new patient
import dataFunctions
from windowsLayouts import *
from dataFunctions import *


def could_create_patient2(values):
    info = read_input_values(values).convert_values_to_strings()
    print("info in 'could_create_patient' method: ", info)
    validation = try_to_create_patient(values)
    print(validation)
    if validation:
        return True


# Reads the inputs and tries to create a patient with them
def read_input_values(values):
    id_patient = 0
    first_name = values["FIRST_NAME"]
    last_name = values["LAST_NAME"]
    
    gender = values["GENDER"]
    if gender == "True":
        gender = "Male"
    else:
        gender = "Female"
    
    date_of_birth = values["DATE_OF_BIRTH"]
    height = values["HEIGHT"]
    weight = values["WEIGHT"]
    is_taking_medication = values["IS_TAKING_MEDICATION"]
    is_allergic_to_medication = values["IS_ALLERGIC_TO_MEDICATION"]
    is_blood_donor = values["IS_BLOOD_DONOR"]
    any_surgery_done = values["ANY_SURGERY_DONE"]
    how_many = values["HOW_MANY"]
    if how_many == "":
        how_many = 0

    print("/n", first_name, last_name, gender, date_of_birth, height, weight, is_taking_medication, is_allergic_to_medication, is_blood_donor, any_surgery_done, how_many, "/n")

    new_patient = Patient(first_name, last_name, gender, date_of_birth, height, weight, is_taking_medication, is_allergic_to_medication, is_blood_donor, any_surgery_done, how_many)
    return new_patient


def could_create_patient(values):
    return dataFunctions.try_to_create_patient(
        0,
        values["FIRST_NAME"],
        values["LAST_NAME"],
        values["GENDER"],
        values["DATE_OF_BIRTH"],
        values["HEIGHT"],
        values["WEIGHT"],
        values["IS_TAKING_MEDICATION"],
        values["IS_ALLERGIC_TO_MEDICATION"],
        values["IS_BLOOD_DONOR"],
        values["ANY_SURGERY_DONE"],
        values["HOW_MANY"])


def display_form():
    patient_intake_layout = create_patient_form_layout()
    patient_form_window = sg.Window("New Patient Form", patient_intake_layout, size=(600, 400))

    # This variable prevents the loop from saving the Patient if the inputs are invalid
    was_save_successful = False

    while True:
        event, values = patient_form_window.read()
        if event == sg.WIN_CLOSED or event == "Cancel":
            break
        elif event == "Save":
            #was_save_successful = read_input_values(values)
            #new_patient = read_input_values(values)
            was_save_successful = could_create_patient(values)
            if was_save_successful:
                new_patient = read_input_values(values)
                print(new_patient)
                print("Patient saved")
                patient_post = create_patient_post(new_patient)
                print("info going to 'display_form' method: ", patient_post)
                insert_post_in_mongodb(patient_post)
                print("Patient Saved!")
                break
            else:
                print("Could not save patient, invalid input(s)")
    patient_form_window.close()
    return was_save_successful
