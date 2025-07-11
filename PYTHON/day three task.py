#>>>>>>>>>>>>>DAY THREE TASKS<<<<<<<<<<<<<<<<<<

#FIND THE LARGEST NUMBER   
a=int(input("Enter 1st number"))
b=int(input("Enter 2nd number"))

if a>b:
    print("this is largest number",a)

else:
    print("this is largest number", b)
    
    #CHECKING EVEN OR ODD

num=int(input("Enter a number:"))
 
if num % 2==0:
    print("this is even number")
else:
    print("this is odd number")

    #LEAP YEAR CHECKER

year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("It is a Leap Year")
else:
    print("It is Not a Leap Year")

    #GRADING MARKS 
marks = int(input("Enter your marks: "))


if(marks >=90 and marks<100):
   
   grade="A"

elif(marks >= 80 and marks <90):
    grade="B"
elif(marks>=70 and marks <80):
    grade="C"
else:
    grade="D"

print("garade of the student->", grade)

#Find Largest of Three Numbers

a=int(input("Enter 1st number:"))
b=int(input("enter 2nd number:"))
c=int(input("enter 3rd number:"))

if a>=b and a>=c:
     largest= a
     print("the greatest number is", a)
elif b>=a and b>=c:
    largest= b
    print("the greatest number is", b)
else :
    largest=c

    print("the greatest number is", c)

#TAFFIC LIGHT
    

color = input("Enter traffic light color (red, yellow, green): ")

if color == "red":
    print("Stop")
elif color == "yellow":
    print("Wait")
elif color == "green":
    print("Go")
else:
    print("Invalid color! Please enter red, yellow, or green.")





