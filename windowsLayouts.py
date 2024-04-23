import PySimpleGUI as sg
from dataFunctions import *

sg.theme("dark")


patient_table_headings = [
    "First name",
    "Last name",
    "Gender",
    "Date of birth",
    "Height",
    "Weight",
    "Is taking medication",
    "Is allergic to meds",
    "Is blood donor",
    "Surgery done",
    "How many"
]

patient_table_values = convert_patients_to_table_data()


patients_window_layout = [
        [sg.Text("All patient Data"), sg.Button("Add new Patient")],
        [sg.Table(headings=patient_table_headings, values=patient_table_values, key="PATIENTS_TABLE", auto_size_columns=True, justification='center', vertical_scroll_only=False)]
        ]

patients_window = sg.Window('Patients List', patients_window_layout, size=(600, 200))


def create_patient_form_layout():
    return [
        [sg.Text("First Name", size=(10, 1)), sg.Input(key='FIRST_NAME')],
        [sg.Text("Last Name", size=(10, 1)), sg.Input(key='LAST_NAME')],
        [sg.Text("Gender"), sg.Radio("Male", group_id=1, key='GENDER'), sg.Radio("Female", group_id=1, key='GENDER')],
        [sg.Text("Date of birth", size=(10, 1)), sg.Input(key='DATE_OF_BIRTH'), sg.CalendarButton("Select Date", format='%Y/%m/%d')],
        [sg.Text("Height", size=(10, 1)), sg.Input(key='HEIGHT')],
        [sg.Text("Weight", size=(10, 1)), sg.Input(key='WEIGHT')],
        [sg.Text("Is taking medication?"), sg.Checkbox("Yes", key='IS_TAKING_MEDICATION')],
        [sg.Text("Is allergic to medication?"), sg.Checkbox("Yes", key='IS_ALLERGIC_TO_MEDICATION')],
        [sg.Text("Is blood donor?"), sg.Checkbox("Yes", key='IS_BLOOD_DONOR')],
        [sg.Text("Any surgery done?"), sg.Checkbox("Yes", key='ANY_SURGERY_DONE')],
        [sg.Text("How many?", size=(10, 1)), sg.Input(key='HOW_MANY')],
        [sg.Cancel(), sg.Button("Save")]
    ]

