import tkinter as tk
from tkinter import messagebox
from generate_password import Password
FILE_TO_SAVE = "day-29\\pass_vault.txt"

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

    if website == "" or username=="" or password=="":
        messagebox.showwarning(title="empty values",message="Please fill all boxes")
    else:
        confirmation = messagebox.askokcancel(title="Confirmation",message=f"Confirm details below:\nEmail:{username}\nPassword:{password}\n")

        if confirmation:
            with open(FILE_TO_SAVE,"a") as file:
                file.write(f"{website} | {username} | {password}\n")
                website_entry.delete(first=0,last=tk.END)
                password_entry.delete(first=0,last=tk.END)



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
website_entry = tk.Entry(width=52)
website_entry.focus()
website_entry.grid(row=1,column=1,columnspan=2)

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