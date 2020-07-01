from tkinter import font
from PIL import ImageTk, Image
import tkinter as tk
from tkinter import ttk
import json
from difflib import get_close_matches

root = tk.Tk()
root.title('Dictionary')


data = json.load(open('data.json'))


def definition(word):
    word = word.lower()
    label_output = ''
    if word in data:
        meaning1 = data[word]
        for item in meaning1:
            label_output = label_output + '\n\n' + item
        label.config(text=label_output)
    elif len(get_close_matches(word, data.keys(), n=2, cutoff=0.8)) > 0:
        output = get_close_matches(word, data.keys())[0]
        label_output = 'Did you mean ' + output + ' instead?'
        label.config(text=label_output)
        yes_button.config(state=tk.NORMAL)
        no_button.config(state=tk.NORMAL)
    else:
        label_output = 'That word does not exist, try again!'
        label.config(text=label_output)
        return 'That word does not exist, try again!'


def yesResponse(word):
    output = get_close_matches(word, data.keys(), n=2, cutoff=0.8)[0]
    meaning = data[output]
    label_output2 = ''
    for item in meaning:
        label_output2 = label_output2 + '\n\n' + item
    label.config(text=label_output2)
    yes_button.config(state=tk.DISABLED)
    no_button.config(state=tk.DISABLED)


def noResponse():
    word.delete(0, tk.END)
    label.config(text="")
    yes_button.config(state=tk.DISABLED)
    no_button.config(state=tk.DISABLED)


canvas = tk.Canvas(root, height=600, width=700, bg='PaleTurquoise1')
canvas.pack()

image1 = tk.PhotoImage(file="background5.jpg")
icon = tk.PhotoImage(file="icon3.png")
background = tk.Label(root, image=image1)
background.place(relwidth=1, relheight=1)


frame = tk.Frame(root, bg='gray25', bd=5)
frame.place(relx=0.15, rely=0.125, relheight=0.1, relwidth=0.7)

word = ttk.Entry(frame, font=40)
word.place(relwidth=0.825, relheight=1)

enter = ttk.Button(frame, text='Find Definition', image=icon,
                   command=lambda: definition(word.get()))
enter.place(relx=0.85, relheight=1, relwidth=0.15)

yes_button = ttk.Button(root, text='Yes',
                        state=tk.DISABLED, command=lambda: yesResponse(word.get()))
yes_button.place(relx=0.25, rely=0.915)

no_button = ttk.Button(root, text='No',
                       state=tk.DISABLED, command=noResponse)
no_button.place(relx=0.65, rely=0.915)

clear_button = ttk.Button(root, text='Clear All',
                          command=noResponse)
clear_button.place(relx=0.45, rely=0.915)

lower_frame = tk.Frame(root, bg='gray25', bd=5)
lower_frame.place(relx=0.15, rely=0.25, relheight=0.65, relwidth=0.7)

label = tk.Label(lower_frame, bg='azure', text='', font=(
    'Courier', 12), anchor='nw', justify='left', bd=3, wraplength=475)
label.place(relwidth=1, relheight=1)

upper_frame = tk.Frame(root, bg='gray30', bd=5)
upper_frame.place(relx=0.165, rely=0.01)
label2 = tk.Label(upper_frame, text='Welcome to the English Dictionary', fg='gray25', bg='azure', bd=5,
                  font=('Helvetica', 20, 'bold'))
label2.pack()

label3 = tk.Label(root, )

root.mainloop()
