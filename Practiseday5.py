#1 
names = ["sakina", "sakshi", "sejal", "sneha", "sameer"]
with open("names.txt", "w") as f:
    for name in names:
        f.write(name + "\n")

with open("names.txt", "r") as f:
    for line in f.readlines():
        print(line, end="")

#2
with open("log.txt", "a") as f:
    f.write("Program run successfully" + "\n")

with open("log.txt", "r") as f:
    data = f.read()
    print(data)

#3 
num = [5, 10, 15, 20, 25]
lst = [i for i in num if i>15]
print(lst)

#4
import json
cities = {
    "Mumbai": 12442373,
    "Delhi": 16787941,
    "Bengaluru": 8443675
}

with open("cities.json", "w") as f:
    json.dump(cities, f)

with open("cities.json", "r") as f:
    cities = json.load(f)
    
for city, population in cities.items():
    print(city, ":", population)

new_city = input("Enter city: ")
new_population = int(input("Enter population: "))

cities[new_city] = new_population

with open("cities.json", "w") as f:
    json.dump(cities, f)

#5
try:
    with open("data.txt", "r") as f:
        data = f.read()

except FileNotFoundError:
    with open("data.txt", "w+") as f:
        f.write("") 
        f.seek(0)
        data = f.read()

finally:
    print(data)
