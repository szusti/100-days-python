from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    label_checkmakrs.config(text="")
    label_timer.config(text="Timer",fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        label_timer.config(text="Break", fg=RED)
        count_down(long_break_sec)
    elif reps %2 == 0:
        label_timer.config(text="Break", fg=PINK)
        count_down(short_break_sec)
    else:

        label_timer.config(text="Work", fg=GREEN)
        count_down(work_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count /60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"
    
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000,count_down, count -1)
    else:
        start_timer()
        makrs = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            makrs += "✔"
        label_checkmakrs.config(text=makrs)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50,bg=YELLOW)

# if you have strange border around canvas, add highlightthickness=0)
canvas = Canvas(width=210,height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="day-28\\pomodoro-start\\tomato.png")
canvas.create_image(103,112,image=tomato_img)
timer_text = canvas.create_text(103,130,text="00:00", fill="white", font=(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=1)


start_button = Button(text="Start",command=start_timer, highlightthickness=0)
start_button.grid(column=0,row=2)
reset_button = Button(text="Reset",command=reset_timer, highlightthickness=0)
reset_button.grid(column=2,row=2)

label_timer = Label(text="Timer", bg=YELLOW,fg=GREEN,font=(FONT_NAME,50,"bold"))
label_timer.grid(row=0,column=1)
label_checkmakrs = Label(bg=YELLOW, fg=GREEN)
label_checkmakrs.grid(row=3,column=1)

window.mainloop()