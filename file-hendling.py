
#file handling

#create file
f=open("ali.c","w")
f.write('#include<stdio.h>int main(){printf("hello");return 0;}')
f.close()

     


name=input("enter your name")
college=input ("enter your college name")
email=input("enter your enamil address")
f=open("ali.txt","w")
ali=name+college+email
f.write(ali)
f.close()



# self practice of  file hendling


name=input("enter your name")
college=input ("enter your college name")
email=input("enter your enamil address")
ali=[name,college,email]
f=open("ali.txt","w")
for i in ali:
    f.write(str(i))
   
    f.write("\n")

f.close()




ali=('{"persnalDetail":{"name":"ali","class":"mca","rollNo":"3,"}}')
f=open("ali.json","w")

f.write(ali)
   
f.write("\n")

f.close()





name=input("enter your name")
college=input ("enter your college name")
email=input("enter your enamil address")
ali=[name,college,email]
f=open("ali.xlsm","w")
for i in ali:
    f.write(str(i))
   
    f.write("\n")

f.close()
