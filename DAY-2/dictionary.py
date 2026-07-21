records = {
    "name" : "Deepak Verma",
    "course" : "B-Tech",
    "cgpa" : 9.4,
    "subjects" : ["UHV", "DAA", "DBMS"]
}

records["percentage"] = 87

#--------------Methods--------------#
print(records.popitem())
del records["cgpa"]
new_dict = records.copy()
print(new_dict)