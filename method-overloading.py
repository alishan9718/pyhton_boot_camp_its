#method overloading
#polymorphism

class Add:
      def add(a,b):

       return ( a+b)
def add(a,b,c):

       return ( a+b,c)


obj=Add
sum=Add.add(10,10)
print(sum)