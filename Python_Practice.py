import random
import csv
import datetime
print("Hello World!")
ballot = 1, 245
print(type(ballot))
print(type(18.31))
print(type(""))
help("keywords")
print(5+2*3)

countries = ["Arapahoe", "Denver", "Jefferson"]
print(countries)
countries[0] = "El Paso"
print(countries)

countries.insert(1, "burak")
print(countries)
countries.pop(1)

counties_dict = {}

counties_dict["Denver"] = 463353
counties_dict["Jefferson"] = 432438
print(len(counties_dict))
print(counties_dict.values())

voting_data = []
voting_data.append({"burak": 111, "burcu": 0000, "melek": 2222})
print(voting_data)

x = 6
while x <= 7:
    print(x)
    x += 1


now = datetime.datetime.now()

print(f"now is { now}")
print(dir(csv))


print(dir(counties_dict))

##
print(dir(random))
