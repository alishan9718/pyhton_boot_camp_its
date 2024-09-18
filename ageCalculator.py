import datetime

#Age calculator using class and functions

class Agecalculator:
    
    def ageFinder():
        currentYear= datetime.date.today().year
        dateOfBirth=int(input("enter your date of birth"))
        age= currentYear-dateOfBirth

        print(age)  


   
x=Agecalculator
x.ageFinder()