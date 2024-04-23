import patientForm
from windowsLayouts import *
from dataFunctions import *


# Add new patient when the button is pressed, display patient form
def press_add_patient_button(patients_window):
    print("Button Pressed")
    was_save_successful = patientForm.display_form()
    print(was_save_successful)
    if was_save_successful:
        #patient_table_values = convert_patients_to_table_data()
        patients_window["PATIENTS_TABLE"].update(values=patient_table_values)


if __name__ == '__main__':
    connect_to_mongodb()
    while True:
        
        event, values = patients_window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == "Add new Patient":
            press_add_patient_button(patients_window)