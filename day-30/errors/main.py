# something that might cause an exception
# try:
# do this if there was an exception
# except:
# do this if there were no exception
# else:
# do this no matter what happens
# finally:

# ==========================================================
# try:
#     file = open("day-30\\errors\\a_file.txt")
#     a_dictionary = {"key":"value"}
#     print(a_dictionary["xxx"])
# except FileNotFoundError:
#     print("There was an error with opening a file, creating a new one")
#     # file = open("day-30\\errors\\a_file.txt", "w")
# #NOTE second except won't be executed if first one will be. TO resolve this, you need either create separate try: except:, or nest it.
# except KeyError as error_message:
#     print(f"Key {error_message} does not exists")
# else:
#     content = file.read()
# finally:
#     raise KeyError("Test of your own message")
#     file.close()
#     print("File was closed")

# ===========================================================

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Are you godzilla or something? Too high value, so definitely you are not human")

bmi = weight / height ** 2
print(bmi)