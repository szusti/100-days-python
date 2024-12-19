# SImpe code with return string + docstring

def format_name(f_name, l_name):
    """Take a first and last name and format it to return to the tittle case version of the name"""
    if f_name=="" or l_name== "":
        return "Invalid output"
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    # this kind of return result in one string that can take variables from the function
    return f"{formated_f_name} { formated_l_name}"


print(format_name(input("What is your first name"), input("What is your surname")))