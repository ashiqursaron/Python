# dictionary = {"Saron": 22,"Shithel": 30, "Tanim": 35}
# new_dictionary = {key : value for key,value in dictionary.items() if value >=30}
# print(dictionary)
# print(new_dictionary)

people = {
    "Saron" : {
        "Id" : "22-48697-3",
        "Department" : "CSE",
        "CGPA" : 2.5
    },
    "Shithel" : {
        "Id" : "22-48698-3",
        "Department" : "CSE",
        "CGPA" : 2.6
    },
    "Tanim" : {
        "Id" : "22-48699-3",
        "Department" : "CSE",
        "CGPA" : 2.7
    }
}
for person, details in people.items():
    print(person+":")
    for id,info in details.items():
        print(id + " " + str(info))