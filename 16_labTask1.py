"""" Write a program that prompts the user to enter the length from the centre of a pentagon to a
 vertex and computes the area of the pentagon, as shown in the following figure"""
"""""
import math
r=input("Enter the length from the center to a vertex:")
r=float(r)
# Compute the area of the pentagon
s =(2*r)* math.sin(math.pi/5) # length of a side
s=float(s)

area=(3* 3**.5)/2 *s*s
area=float(area)
print("The area of pentagon is :",area)
"""""



# Question 2
"""2. Geometry: area of a regular polygon"""
"""""
import math
numberOfsides=input("Enter the number of Sides: ")
numberOfsides=float(numberOfsides)

side=input("Enter the side: ")
side=float(side)

# compute the area of regular pentagon
area=(numberOfsides * math.pow(side,2))/(4*math.tan(math.pi/numberOfsides))
area=float(area)
print("the area of polygon is: ",area)
"""""


# Question 3
""""" Write a program that prompts the user to enter integer and displays the number in reverse Also determines whether it is a palindrome number or not 
"""""
"""""
i=int(input("Enter Number: "))
temp=i
rev=0
while(i>0):
    rev=(rev*10)+i%10
    i=i//10
print("Reverse= ",rev)

if(temp==rev):
    print("The number is palindrom!")
else:
    print("Not a palindrom")
""""""
# Question 4

4. Write a program that prompts the user to enter the three points p1, p2, and p3 for a triangle. 
Display the area and three angles of triangle.
"""""
"""""
import math
x1,y1,x2,y2,x3,y3=eval(input("Enter three point of a triangle: "))
# Compute the area of triangle
side1=math.pow(math.pow(x2-x1,2)+math.pow(y2-y1,2),0.5)
side1=float(side1)
side2=math.pow(math.pow(x3-x2,2)+math.pow(y3-y2,2),0.5)
side2=float(side2)
side3=math.pow(math.pow(x1-x3,2)+math.pow(y1-y3,2),0.5)
side3=float(side2)

s=(side1+side2+side3)/2
s=float(s)

area=math.pow(s*(s-side1)*(s-side2)*(s-side3),0.5)
area=float(area)
print("The area of triangle is: ",area)
# three angles of triangle
a=eval(input("Enter first angle: "))
b=eval(input("Enter second angle: "))
c=180-(a+b)
c=float(c)
print("Third angle of the Triangle: ",c,"degree")
"""""

# Question 5
"""5. Body mass index (BMI)"""
"""Write a program that prompts the user to enter weight in pounds and height in inches and then display the BMI"""
"""""
import math
KilogramsPerPounds=0.45359237
MetersPerInch=0.0254

weight=eval(input("Enter weight in pounds: "))
height=eval(input("Enter height in inches: "))

weight=weight*KilogramsPerPounds
height=height*MetersPerInch

bodyMassIndex=weight/math.pow(height,2)
bodyMassIndex=float(bodyMassIndex)
print("BMI is: ",bodyMassIndex)
"""""

# Question 6
"""6. Write a program that prompts the user to enter a year and displays the given year is leap or not 
leap. A year is a leap year if it is divisible by 4 but not by 100 or if it is divisible by 400.
"""
"""""
year=eval(input("Enter year: "))

# leaf year if perfectly divisible by 400
if year % 400 == 0:
    print("is a leaf year:",year)
# not leaf year if divisible by 100
elif year % 100==0:
    print("Is not a leaf year:",year)
# leaf year if divisible by 4
elif year % 4==0:
    print("is a leaf year:",year)
else:
    # all other years is not a leaf year
    print("is not a leaf year")
"""""

# Question 7
"""7. Algebra: solve quadratic equations
"""
"""""
import cmath

a =eval(input("Enter a "))
b =eval(input("Enter b "))
c =eval(input("Enter c "))

# calculate the discriminant
d = (b**2) - (4*a*c)

if d==0:
    sol2 = (-b+cmath.sqrt(d))/(2*a)
    print("This equation has one root ",sol2)
elif d>0:
    sol1 = (-b - cmath.sqrt(d)) / (2 * a)
    sol2 = (-b + cmath.sqrt(d)) / (2 * a)
    print('The solution are {0} and {1}'.format(sol1, sol2))
else:
    print("The equation has not real root ")
"""""

""""8. Write a program that prompts the user to enter an integer for today’s day of the week (Sunday is 
0, Monday is 1, ..., and Saturday is 6). Also prompt the user to enter the number of days after 
today for a future day and display the future day of the week."""
"""""
todaysDate = eval(input("Enter an interger for today's day of the week from 0 - 6, Sunday is 0 and Saturday is 6."))
if todaysDate == 0:
    print("Today is Sunday")
elif todaysDate == 1:
    print("Today is Monday")
elif todaysDate == 2:
    print("Today is Tuesday")
elif todaysDate == 3:
    print("Today is Wednesday")
elif todaysDate == 4:
    print("Today is Thursday")
elif todaysDate == 5:
    print("Today is Friday")
elif todaysDate == 6:
    print("Today is Saturday")
daysElapsed = eval(input("Enter the number of days elapsed since today:"))

if daysElapsed == 1:
    print("Today is Sunday and the future day is Monday")
"""
"""""
9. Write a program that prompts the user to enter three integers and displays them in increasing 
order without using arrays, lists, sets. """""
"""""
user_data = [int(input("Enter First Number:")), int(input("Enter Second Number:")), int(input("Enter Third Number:"))]

for item in sorted(user_data):f
    print(item)
"""""
"""""
10. Day Of The Week """""
year=eval(input("Enter year: "))

q=eval(input("Enter the day of the month: "))

h=eval(input("Enter the day of the week: "))
m=eval(input("Enter the month: "))
j=eval(input("Enter the Century: "))
k=eval(input("Enter the year of the century: "))


h = ( q + 26* (m+1) // 10 + year%100 + year%100 // 4 + year// 100//4 + 5* year // 400 ) % 7
print("the name of the day of the week is: ",h)
