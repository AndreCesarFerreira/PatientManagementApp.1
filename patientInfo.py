from dateutil.relativedelta import relativedelta
from datetime import datetime


# Patient class with the class constructor and necessary methods
class Patient:

    # Initialize the Patient and set the values for the fields
    def __init__(self, first_name, last_name, gender, date_of_birth, height, weight, is_taking_medication, is_allergic_to_meds, is_blood_donor, surgery_done, how_many):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.date_of_birth = date_of_birth
        #self.age = self.calculate_age(date_of_birth)
        #self.age = age
        self.height = height
        self.weight = weight
        self.is_taking_medication = is_taking_medication
        self.is_allergic_to_meds = is_allergic_to_meds
        self.is_blood_donor = is_blood_donor
        self.surgery_done = surgery_done
        self.how_many = how_many

    # Method to calculate the age of the Patient only using the birthdate and the current date.
    def calculate_age(self, date):
        today = datetime.today()
        age = relativedelta(today, self.date_of_birth)
        return age.years

    # Convert each of the fields to a string, bundle them into a list, and return the list
    def convert_values_to_strings(self):
        first_name = str(self.first_name)
        last_name = str(self.last_name)
        gender = str(self.gender)
        #date_of_birth = datetime.strftime(self.date_of_birth, '%Y/%m/%d')  # YYYY/MM/DD
        date_of_birth = str(self.date_of_birth)
        #age = str(self.age)
        height = str(self.height)
        weight = str(self.weight)
        is_taking_medication = str(self.is_taking_medication)
        is_allergic_to_meds = str(self.is_allergic_to_meds)
        is_blood_donor = str(self.is_blood_donor)
        surgery_done = str(self.surgery_done)
        how_many = str(self.how_many)

        string_prep = first_name, last_name, gender, date_of_birth, height, weight, is_taking_medication, is_allergic_to_meds, is_blood_donor, surgery_done, how_many
        return string_prep
