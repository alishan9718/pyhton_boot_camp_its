#user can input only sting input

from pickle import TRUE


def inputAlphabetOnly(name):
     while True:
          user_Input=input(name)
          if user_Input.isalpha:
                                return user_Input
     else:
          print("invalid input , please enter Alphabets only")

name=inputAlphabetOnly("enter your name:")
print("hello",name)                            
