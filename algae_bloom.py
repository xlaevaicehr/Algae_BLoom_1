import tkinter as tk

ph_level = 0

root = tk.Tk()
root.geometry("300x400")
sum = 0

root.config(bg="darkgreen")

root.title("Algae Blooms")

label = tk.Label(root, text=ph_level, font=('Georama', 100))
label.pack(padx=50, pady=20)

yes = tk.Label(root, text=' ', font=('Georama', 100))

buttonframe = tk.Frame(root)
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)

def add_one():
    global ph_level
    ph_level += 1
    label.config(text=ph_level)

def add_two():
    global ph_level
    ph_level += 2
    label.config(text=ph_level)

def add_three():
    global ph_level
    ph_level += 3
    label.config(text=ph_level)

def add_four():
    global ph_level
    ph_level += 4
    label.config(text=ph_level)

def add_five():
    global ph_level
    ph_level += 5
    label.config(text=ph_level)

def add_six():
    global ph_level
    ph_level += 6
    label.config(text=ph_level)

def add_seven():
    global ph_level
    ph_level += 7
    label.config(text=ph_level)

def add_eight():
    global ph_level
    ph_level += 8
    label.config(text=ph_level)

def add_nine():
    global ph_level
    ph_level += 9
    label.config(text=ph_level)


def clear():
    global ph_level
    ph_level = 0
    label.config(text=ph_level)

def enter():
    if ph_level <= 9:
        yes.config(text='AN algae bloom is not likely for you', font=('Georama', 50))
    elif ph_level >= 12:
        yes.config(text='An algae bloom is not likely for you', font=('Georama', 50))
    elif ph_level >= 9 and ph_level <= 12:
        yes.config(text='An algae bloom is likely for you', font=('Georama', 50))


btn1 = tk.Button(buttonframe, text='1', font=('Georama', 50), command=add_one)
btn1.grid(row=0, column=0, sticky=tk.W + tk.E)

btn2 = tk.Button(buttonframe, text='2', font=('Georama', 50), command=add_two)
btn2.grid(row=0, column=1, sticky=tk.W + tk.E)

btn3 = tk.Button(buttonframe, text='3', font=('Georama', 50), command=add_three)
btn3.grid(row=0, column=2, sticky=tk.W + tk.E)

btn4 = tk.Button(buttonframe, text='4', font=('Georama', 50), command=add_four)
btn4.grid(row=1, column=0, sticky=tk.W + tk.E)

btn5 = tk.Button(buttonframe, text='5', font=('Georama', 50), command=add_five)
btn5.grid(row=1, column=1, sticky=tk.W + tk.E)

btn6 = tk.Button(buttonframe, text='6', font=('Georama', 50), command=add_six)
btn6.grid(row=1, column=2, sticky=tk.W + tk.E)

btn7 = tk.Button(buttonframe, text='7', font=('Georama', 50), command=add_seven)
btn7.grid(row=2, column=0, sticky=tk.W + tk.E)

btn8 = tk.Button(buttonframe, text='8', font=('Georama', 50), command=add_eight)
btn8.grid(row=2, column=1, sticky=tk.W + tk.E)

clear = tk.Button(root, text='clear', font=('Georama', 50), command=clear)

btn9 = tk.Button(buttonframe, text=9, font=('Georama', 50), command=add_nine)
btn9.grid(row=2, column=2, sticky=tk.W + tk.E)


clear.pack()

buttonframe.pack()

enter = tk.Button(root, text='Enter', font=('Georama', 50), command=enter)
enter.pack(padx=0, pady=0)

yes.pack()

root.mainloop()