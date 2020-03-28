from app.calculation.forms import CalculateForm
from enum import Enum

class Gender(Enum):
    Male = 0
    Female = 1

class Framingham:

    def __age_converter(self, age):
        if 20 <= age <= 34:
            return (0, 2)
        if 35 <= age <= 39:
            return (5, 6)
        if 40 <= age <= 44:
            return (9, 9)  
        if 45 <= age <= 49:
            return (12, 12)  
        if 50 <= age <= 54:
            return (15, 15)  
        if 55 <= age <= 59:
            return (16, 16)  
        if 60 <= age <= 64:
            return (19, 19)         
        if 65 <= age <= 69:
            return (20, 21)   
        if 70 <= age <= 74:
            return (21, 23)  
        if 75 <= age <= 79:
            return (22, 25) 

    def __total_cholesterol_converter(self, age, total_cholesterol):
        if 20 <= age <= 39:
            if total_cholesterol < 160.0:
                return (0, 0)
            if 160.0 <= total_cholesterol <= 199.0:
                return (4, 4)
            if 200.0 <= total_cholesterol <= 239.0:
                return (7, 8)
            if 240.0 <= total_cholesterol <= 279.0:
                return (9, 11)
            if total_cholesterol > 290.0:
                return (11, 13)
        if 40 <= age <= 49:
            if total_cholesterol < 160.0:
                return (0, 0)
            if 160.0 <= total_cholesterol <= 199.0:
                return (3, 3)
            if 200.0 <= total_cholesterol <= 239.0:
                return (5, 6)
            if 240.0 <= total_cholesterol <= 279.0:
                return (6, 8)
            if total_cholesterol > 290.0:
                return (8, 10)
        if 50 <= age <= 59:
            if total_cholesterol < 160.0:
                return (0, 0)
            if 160.0 <= total_cholesterol <= 199.0:
                return (2, 2)
            if 200.0 <= total_cholesterol <= 239.0:
                return (3, 4)
            if 240.0 <= total_cholesterol <= 279.0:
                return (4, 5)
            if total_cholesterol > 290.0:
                return (5, 7)
        if 60 <= age <= 69:
            if total_cholesterol < 160.0:
                return (0, 0)
            if 160.0 <= total_cholesterol <= 199.0:
                return (1, 1)
            if 200.0 <= total_cholesterol <= 239.0:
                return (1, 2)
            if 240.0 <= total_cholesterol <= 279.0:
                return (2, 3)
            if total_cholesterol > 290.0:
                return (3, 4)
        if 70 <= age <= 79:
            if total_cholesterol < 160.0:
                return (0, 0)
            if 160.0 <= total_cholesterol <= 199.0:
                return (0, 1)
            if 200.0 <= total_cholesterol <= 239.0:
                return (0, 1)
            if 240.0 <= total_cholesterol <= 279.0:
                return (1, 2)
            if total_cholesterol > 290.0:
                return (1, 2) 

    def __smoker_converter(self, age):
        if 20 <= age <= 39:
            return (8, 9)
        if 40 <= age <= 49:
            return (5, 7)
        if 50 <= age <= 59:
            return (3, 4)  
        if 60 <= age <= 69:
            return (1, 2)  
        if 70 <= age <= 79:
            return (1, 1)  

    def __hdl_cholesterol_converter(self, hdl_cholesterol):
        if hdl_cholesterol >= 60.0:
            return (0, 0)
        if 50.0 <= hdl_cholesterol <= 59.0:
            return (1, 1)
        if 40.0 <= hdl_cholesterol <= 49.0:
            return (2, 2)
        if hdl_cholesterol < 40.0:
            return (3, 3)
        
    def __systolic_blood_pressure_converter(self, systolic_blood_pressure):
        if systolic_blood_pressure < 120.0:
            return (0, 0)
        if 120.0 <= systolic_blood_pressure <= 129.0:
            return (0, 1)
        if 130.0 <= systolic_blood_pressure <= 139.0:
            return (1, 2)
        if 140.0 <= systolic_blood_pressure <= 159.0:
            return (1, 3)            
        if systolic_blood_pressure > 160.0:
            return (2, 4)

    def __score_converter(self, form, gender):
        age = form.age.data
        age_score = self.__age_converter(age)[gender]
        total_cholesterol_score = self.__total_cholesterol_converter(age, form.total_cholesterol.data)[gender]
        smoker_score = 0
        if form.smoker.data == 'yes':
            smoker_score = self.__smoker_converter(age)[gender]
        hdl_cholesterol_score = self.__hdl_cholesterol_converter(form.hdl_cholesterol.data)[gender]
        systolic_blood_pressure_score = self.__systolic_blood_pressure_converter(form.systolic_blood_pressure.data)[gender]
        return [age_score, total_cholesterol_score, smoker_score, hdl_cholesterol_score, systolic_blood_pressure_score]

    def convert_values_to_score(self, form):
        if form.gender.data == 'male':
            return self.__score_converter(form, Gender.Male.value)
        else:
            return self.__score_converter(form, Gender.Female.value)
    
    def convert_score_to_risk(self, form, score):
        if form.gender.data == 'male':
            if 9 <= score <= 13:
                return 1
            if 13 <= score <= 15:
                return 2
            if score == 16:
                return 3
            if score == 17:
                return 4
            if score == 18:
                return 5
            if score == 19:
                return 6
            if score == 20:
                return 8
            if score == 21:
                return 10
            if score == 22:
                return 12
            if score == 23:
                return 16
            if score == 24:
                return 20   
            if score == 25:
                return 25
            if score > 26:
                return 30
        else:
            if 9 <= score <= 21:
                return 1
            if 22 <= score <= 23:
                return 2
            if score == 24:
                return 3
            if score == 25:
                return 4
            if score == 26:
                return 5
            if score == 27:
                return 6
            if score == 28:
                return 8
            if score == 29:
                return 11
            if score == 30:
                return 14
            if score == 31:
                return 17  
            if score == 32:
                return 22
            if score == 33:
                return 27
            if score > 34:
                return 30