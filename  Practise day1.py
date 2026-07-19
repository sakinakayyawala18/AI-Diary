#1
name = input("enter your name =  ")
age = int(input("enter your age = "))
print(f"Hello {name}, you are {age} years old!")

#2
num1 = int(input("enter your num1 = "))
num2 = int(input("enter your num2 = "))

sum = num1 + num2
product = num1 * num2
quotient = num1/num2
difference = num1 - num2

print(sum, difference, product, quotient)

#3
num1 = int(input("enter your num1 = "))
num2 = int(input("enter your num2 = "))
num3 = float(input("enter your num3 = "))

avg = (num1 + num2 + num3)/3
print(avg)

#4
a = "45"
print(int(a))
print(float(a))
print(str(a))

#5
x = 10 + 3 * 2 ** 2
print(x)

#6
num1 = int(input("enter your num1 = "))
num2 = int(input("enter your num2 = "))
temp1 = num1
num1 = num2
num2 = temp1

print(num1)
print(num2)

#7
CelsiusT = float(input("enter your T = "))
FahrenheitTemp= (CelsiusT * (9/5)) + 32
print(f"FahrenheitTemp = {FahrenheitTemp}")

#8
r = float(input("enter your radius= "))
Area = (r*r) * π
print(Area)

#9
P = float(input("enter your Principle= "))
R = float(input("enter your radius= "))
T = float(input("enter your Time= "))
SI = (P * R * T )/100
print(f"Simple Intrest = {SI}")

#10
num = 45.78
inti = int(num)
print(f"interger part  = {inti}")
print(f"fraction part  = {num - inti}")