import tkinter as tk
from tkinter import messagebox
from generate_password import Password
import json
#NOTE
# for json, dump() writes, load() read, update() updated
    
FILE_TO_SAVE = "day-30\\errors\\pass_manager\\pass_vault.json"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_random_pass():
    password = Password()
    password_entry.delete(0,tk.END)
    password_entry.insert(0,password.password)
    window.clipboard_clear()
    window.clipboard_append(password.password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_file():
    website = website_entry.get()
    username = email_user_entry.get()
    password = password_entry.get()

    new_data = {
        website:{
            "email": username,
            "password": password
        }
    }

    if website == "" or password=="":
        messagebox.showwarning(title="empty values",message="Please fill all boxes")
    else:
        try:
            with open(FILE_TO_SAVE,"r") as file:
                # reading old data
                json_data:dict = json.load(file)
                # update old data with new one
        except FileNotFoundError:
            with open(FILE_TO_SAVE,"w") as file:
                json.dump(new_data, file, indent=4)
        else:
            # updating old data with new data
            json_data.update(new_data)

            with open(FILE_TO_SAVE,"w") as file:
                # save updated datafi
                json.dump(json_data, file, indent=4)
        finally:
            website_entry.delete(first=0,last=tk.END)
            password_entry.delete(first=0,last=tk.END)
# -------------------------- FIND PASSWORD -------------------------#

def find_password():
    website = website_entry.get()
    try:
        with open(FILE_TO_SAVE,"r") as file:
            json_data:dict = json.load(file)
            if website in json_data:
                messagebox.showinfo(title="Password Info", message=f"For {website}\nEmail/Username: {json_data[website]['email']}\nPassword: {json_data[website]['password']}" )
            else:
                messagebox.showwarning(title="Not found", message=f"I could not find account for: {website}")
    except FileNotFoundError:
        messagebox.showerror(title="File not found", message=f"Could not find file with passwords\n{FILE_TO_SAVE}")

# ---------------------------- UI SETUP ------------------------------- #


window = tk.Tk()
window.config(width=220, height=220,padx=20,pady=20)
window.title("Password Manager")

# Row 0 - Pic
canvas = tk.Canvas(width=200,height=200)
image_lock = tk.PhotoImage(file="day-29\\logo.png")
canvas.create_image(100,100,image=image_lock)
canvas.grid(row=0,column=1)

# Row 1 - Website
website_label = tk.Label(text="Website:")
website_label.grid(row=1,column=0)
website_entry = tk.Entry(width=33)
website_entry.focus()
website_entry.grid(row=1,column=1)
search_button = tk.Button(text="Search",command=find_password, width=14)
search_button.grid(row=1,column=2)

# Row 2 - Email/Username
email_user_label = tk.Label(text="Email/Username:")
email_user_label.grid(row=2,column=0)
email_user_entry = tk.Entry(width=52)
email_user_entry.insert(0,"example@email.com")
email_user_entry.grid(row=2,column=1,columnspan=2)

# Row 3 - Password
password_label = tk.Label(text="Password:")
password_label.grid(row=3,column=0)
password_entry = tk.Entry(width=33)
password_entry.grid(row=3,column=1)
password_button = tk.Button(text="Generate Password",command=generate_random_pass)
password_button.grid(row=3,column=2)

#Row 4 - add button
add_button = tk.Button(text="Add",width=44, command=save_file)
add_button.grid(row=4,column=1, columnspan=2)

window.mainloop()