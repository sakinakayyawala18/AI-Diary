1

salary = int(input("enter the inital salary salary = "))

if(salary < 30,000):
    salary = salary + salary * 5/100
    print(f"Your new salary  = {salary}")
elif(salary>30_000 and  salary<70_000):
    salary = salary + salary * 15/100
    print(f"Your new salary  = {salary}")
else:
    salary = salary + salary * 25/100
    print(f"Your new salary  = {salary}")

#2
num1  = int(input("enter the number 1 = "))
num2  = int(input("enter the number 2 = "))

for i in range(num1,num2):
    if(i%2==0):
        print(i)

#3 
n  = int(input("enter the number = "))

while n>0:
    print(n%10)
    n=n//10

#4
n  = int(input("enter the number = "))

count=0
while n>0:
    count+=1
    n=n//10
print(count)

#5
n  = int(input("enter the number = "))

sum=0
while n>0:
    digit  = n%10
    sum += digit
    n=n//10
print(sum)

#7
while True:
    a = input("Enter the number (or Quit to exit): ")

    if a == "Quit":
        break
    a = int(a)
    if a > 0:
        print("Positive")
    elif a == 0:
        print("Zero")
    else:
        print("Negative")

#8
def calculator(a, b, operation):
    if(operation=="+"):
        print(a+b)
    elif(operation=="-"):
        print(a-b)
    elif(operation=="*"):
        print(a*b)
    else:
        print(a/b)

calculator(2, 3, "+")

#9
def is_prime(n):
    if n==1 or n==0:
        return True
    else:
        for i in range(2,n):
            if n%i==0:
                return False
                break
        return True

print(is_prime(10))

#10
target = 5

while True:
    num = int(input("enter the guess number = "))
    if(num>target):
        print("Too High")
    elif(num<target):
        print("Too low")
    else:
        print(f"Got it, it is {num}")
        break


