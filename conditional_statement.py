
#voting eligiblity cheak 


age =input("Enter your age  ")
if(int(age)>=18):  print("you are eligble") 
else: print("you are not eligble")  

age = input("enter your age")
gender = input("enter your gender")
if(int(age)>17 and gender == "male") :print("male are eligble for privet job")
    
elif (int(age)>17 and gender == "female"):print("female are eligble for govermennt job")
    
else:print ("you are under age no job for you ")


a=int(input("enter first num1"))
b=int(input("enter first num2"))
c=int(input("enter first num3"))

if(a<b and b>c):
    print(b,"b is greater")
elif(b<a and a>c):
    print(a,"a is greater")

else:
    print(c,"c is greater")