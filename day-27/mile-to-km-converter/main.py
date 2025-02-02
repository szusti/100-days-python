import tkinter

window = tkinter.Tk()
window.title("Miles to Km converter")
window.minsize(200,100)
window.config(padx=10,pady=10)

# First Row
entry_box = tkinter.Entry()
entry_box.insert(0,0)
entry_box.config(width=10)
entry_box.grid(row=0,column=1)

label_miles = tkinter.Label(text="Miles")
label_miles.grid(row=0,column=3)

# Second Row
label_equal_to = tkinter.Label(text="is equal to")
label_equal_to.grid(row=1,column=0)

label_converted = tkinter.Label(text=0)
label_converted.grid(row=1,column=1)

label_km = tkinter.Label(text="Km")
label_km.grid(row=1,column=3)

# Third row
def convert():
    mil_number = round(1.60934 * float(entry_box.get()),3)
    label_converted.config(text=f"{mil_number}")


button = tkinter.Button(text="Convert",command=convert, pady=10)
button.grid(row=2,column=1)





window.mainloop()

