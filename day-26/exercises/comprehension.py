# ============================ LIST ===========================
# numbers = [1,2,3]
# new_list = []
# for n in numbers:
#     add_1 = n +1
# new_list.append(add_1)

# new_list = [new_item for item in list]
# numbers = [1,2,3]
# comprehension_list = [n+1 for n in numbers]

# name = "Michale"
# new_list = [letter for letter in name]

# new_list = [new_item for item in list if test]
# names = ["Alex", "Beth", "Caroline", "Dave", "Elenor", "Freddie"]
# new_list = [name.upper() for name in names if len(name) < 5]
# -------------------------------------------------------------
#==========================DICT=============================
# new_dict = {new_key:new_value for item in list}
# new_dict = {new_ley:new_value for (key,value) in dict.items()}
# new_dict = {new_ley:new_value for (key,value) in dict.items() if test}
# ========================PANDA=============================
import pandas
student_dict = {
    "student":["ANgela", "James", "Lily"],
    "score": [56,76,78]
}
for (key,value) in student_dict.items():
    print(value)

student_data_frame = pandas.DataFrame(student_dict)
for (key,value) in student_dict.items():
    print(value)

for (index,row) in student_data_frame.iterrows():
    # print(index,row)
    print(row.student)
