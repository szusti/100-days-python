import os
print(os.getcwd())

file = open("day-24\operations-on-file\my_file.txt")
contents = file.read()
print(contents)
file.close()

with open("day-24\operations-on-file\my_file.txt") as file_two:
    contents_two = file_two.read()
    print(contents_two)

# mode default is r - read. w - write (replace older text), a - append (add new text)
# w and a will create a new file if they don't exists.
with open("day-24\operations-on-file\my_file_2.txt", mode="a") as file_three:
    file_three.write("\nNew file here")


print("------------")
# C:\Users\xxxx\Desktop\VMShared\gitHub\python\100-Days-Python
print(os.getcwd())
# c:\Users\xxxx\Desktop\VMShared\gitHub\python\100-Days-Python\day-24\operations-on-file
print(os.path.dirname(__file__))

absolute_path = os.path.join(os.path.dirname(__file__), "my_file_3.txt")
print(absolute_path)
with open(absolute_path,mode="w") as file_four:
    file_four.write(f"absolute path, {absolute_path}")


