#oops
# class and object
import datetime

class Myclass:
    age=20
    print("you are in a class")
    
# object creation and pass properties
    
x =Myclass()
print(x.age)



class Agecalculator:
    
    def ageFinder():
        currentYear= datetime.date.today().year
        dateOfBirth=int(input("enter your date of birth"))
        age= currentYear-dateOfBirth

        print(age)  


   
x=Agecalculator
x.ageFinder()