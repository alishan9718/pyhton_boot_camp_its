   
#function in python

def multiply(a , b):
    z = a*b
    print("the value is:",z)

x=int(input("enter 1 num "))
y=int(input("enter 2 num "))
multiply(x,y)



#home work




def calculate_age(birthdate):
    today = datetime.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

birthdate_input = input("Enter your birthdate (YYYY-MM-DD): ")
birthdate = datetime.strptime(birthdate_input, "%Y-%m-%d")
age = calculate_age(birthdate)

print(f"You are {age} years old.")