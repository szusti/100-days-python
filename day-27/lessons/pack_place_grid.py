# Layoutts for tkinter
# pack, place, grid

# --------------------------------------------------
# NOTE !!!!!!!!!!!!!!
# YOU CAN"T MIX GRID AND PACK
# ---------------------------------------------------


from tkinter import *

window = Tk()
window.minsize(width=500,height=200)

# padding

window.config(padx=10,pady=10)



# ========= pack ==============
# hard to sprecision
# label = Label(text="This is old text")
# label.config(text="This is new text")
# label.pack(side="left")

# button = Button(text="Click Me")
# button.pack(side="left")

# entry = Entry(width=30)
# entry.insert(END, string="Some text to begin with.")
# entry.pack(side="left")

# ========= place ==============
# for precision

# label = Label(text="This is old text")
# label.config(text="This is new text")
# label.place(x=0,y=0)

# button = Button(text="Click Me")
# button.place(x=0,y=50)

# entry = Entry(width=30)
# entry.insert(END, string="Some text to begin with.")
# entry.place(x=100,y=150)
# ========== Grid ==========
# as the name suggest use rows and columns.

label = Label(text="This is old text")
label.config(text="This is new text")
label.grid(column=0,row=0)
label.config(padx=50,pady=50)

button = Button(text="Click Me")
button.grid(column=1,row=1)

buton_2 = Button(text="Goodbye")
buton_2.grid(column=3,row=0)

entry = Entry(width=30)
entry.insert(END, string="Some text to begin with.")
entry.grid(column=3,row=3)

window.mainloop()




