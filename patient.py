class Patient:

    def __init__(self, patient_id, name, age, gender, affected_knee):
        self.__patient_id = patient_id
        self.__name = name
        self.__age = age
        self.__gender = gender
        self.__affected_knee = affected_knee

    def get_patient_details(self):
        return {
            "Patient ID": self.__patient_id,
            "Name": self.__name,
            "Age": self.__age,
            "Gender": self.__gender,
            "Affected Knee": self.__affected_knee
        }