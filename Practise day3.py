#1
string = input("enter the string = ")
if(string==string[::-1]):
    print("string is palindrome")
else:
    print("string is not palindrome")

#2
num = [1, 2, 3, 4, 5, 6]
sum = 0
for i in num:
    sum += i
print(f"avg = {sum/len(num)}")

#3
list1 = [1, 2, 7] 
list2 = [2, 4, 5]

list1 = set(list1)
list2 = set(list2)
result = list(list1.union(list2))
print(result)

#4
tup = (1, 2, 3, 4, 5, 6)
even_tup = []
odd_tup  = []

for i in tup:
    if(i%2==0):
        even_tup.append(i)
    else:
        odd_tup.append(i)

even_tup = tuple(even_tup)
odd_tup = tuple(odd_tup)
print(even_tup, odd_tup)

5

students = {}
while True:
    print("\n===== MENU =====")
    print("A - Add a student")
    print("B - Update marks")
    print("C - Search for a student")
    print("D - Display all students and marks")
    print("E - Exit")

    choice = input("Enter your choice: ").upper()

    match choice:

        case "A":
            name = input("enter the name")
            marks = int(input("enter the marks"))
            students[name]=marks
        case "B":
            name = input("enter the name")
            if name in students:
                marks = int(input("enter the marks"))
                students[name] = marks
            else:
                print("please print valid name")

        case "C":
            name = input("enter the name")
            if name in students:
                print(f"Student found = {name} and marks = {students[name]}")
            else:
                print("Name not found")

        case "D":
            if len(students) == 0:
                print("Dictionary is empty.")
            else:
                print("\nStudents and Marks:")
                for name, marks in students.items():
                    print(name, ":", marks)

        case "E":
            print("Program Ended.")
            break

        case _:
            print("Invalid Choice.")

#6
words = ["apple","banana","kiwi","cherry","mango"]
dict = {}
for i in words:
    dict[i]=len(i)
print(dict)

#7
string = input("enter the string with spaces = ")
count=0
for i in string:
    if(i==" "):
        count+=1
print(f"Number of count of spaces = {count}")

#8
def common_element(list1, list2):
    list1 = set(list1)
    list2 = set(list2)

    common = list1.intersection(list2)

    if common:
        print(f"Shared common element = {common}")
    else:
        print("Shared no common element")


list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]

list3 = [1, 2, 3]
list4 = [3, 4]

common_element(list1, list2)
common_element(list3, list4)

#9
def find_duplicates(lst):
    seen = set()
    duplicate = set()

    for i in lst:
        if i in seen:
            duplicate.add(i)
        else:
            seen.add(i)

    if duplicate:
        print("Duplicate elements:", duplicate)
    else:
        print("No duplicate elements")


lst = [1, 2, 3, 4, 2, 5, 3, 6, 7, 2]

find_duplicates(lst)

#10
def find_duplicates(str):
    seen = set()
    duplicate = set()

    for i in str:
        if i in seen:
            duplicate.add(i)
        else:
            seen.add(i)

    if seen:
        print("Unique:", seen)
    else:
        print("No unique element")


string = "sakina"

find_duplicates(string)
