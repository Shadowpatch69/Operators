# this is for single line comment ctrl slash
""" This is for mutiline comment shift option A """
name="Aarav Tamang"
age = 20 
address = "Baneshwor"
# concate method
print(" My name is " + name + " My age is "+str(age) + " Address is " + address)
# f-string method
print(f"My name is {name} and My age is {age} and address is {address}")
# fomat old version method
print("My name is %s and age is %d and address is %s " % (name,age,address))
#  format new version method
print("My name is {0} and age is {1} and address is {2} .format(name,age,address)")
# type of the data hold by variable
print(type(name))

# assigning variables
name= input ("Enter your name")
age = int( input ("Enter the age"))
address = input ("Enter the location")
# concate method
print(" My name is " + name + " My age is "+str(age) + " Address is " + address)
# f-string method
print(f"My name is {name} and My age is {age} and address is {address}")
# fomat old version method
print("My name is %s and age is %d and address is %s " % (name,age,address))
#  format new version method
print("My name is {0} and age is {1} and address is {2} .format(name,age,address)")


num1= input("enter any number")
num2= input("enter any number")

num3= int (input("enter any number"))
num4= int (input("enter any number"))

sum1= num1 + num2
sum2= num3 + num4

print (f"first sumis {sum1} and second sum is {sum2}")
print (type(sum1))
print (type(sum2))

# True and False value
# if and is used then it return first false if both true then last value
# if or is used then it return first true if both false then last value
print (6 and 7)
print ( 6 or 7)

# membership and identity 
a = [ 1,2,3]
b = [ 1,2,3]
c = a

# false
print (a is b) 
# true 
print (a == b)
# true
print (a is c )
print (id (a))
print (id(b))
print (id(c))