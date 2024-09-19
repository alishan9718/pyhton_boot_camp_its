#exception Hendling using try and except
'''
num1=10/0
try:
   print(num1)
   
except ZeroDivisionError:
        print("not define")

except:
     print("somthing went wrong")
'''

num2=input("enter number1")
string =input("enter string")


num2=int(num2)

     
     
try:
    print(num2+string)

except TypeError:
     print("error")
        
