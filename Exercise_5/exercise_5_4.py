print("Please enter the name of 5 cities one by one.")
cities = []

for i in range(5):
    c = input("Enter a name of a city: ")
    cities.append(c)

for city in cities:
    print(city)