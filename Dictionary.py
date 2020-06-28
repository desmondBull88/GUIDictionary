from tkinter import font
import tkinter as tk
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


def noResponse():
    word.delete(0, tk.END)
    label.config(text="")


canvas = tk.Canvas(root, height=600, width=700, bg='PaleTurquoise1')
canvas.pack()

frame = tk.Frame(root, bg='turquoise1', bd=5)
frame.place(relx=0.15, rely=0.1, relheight=0.1, relwidth=0.75)

word = tk.Entry(frame, font=40)
word.place(relwidth=0.6, relheight=1)

enter = tk.Button(frame, text='Find Definition',
                  command=lambda: definition(word.get()))
enter.place(relx=0.65, relheight=1, relwidth=0.35)

yes_button = tk.Button(canvas, text='Yes', padx=40,
                       pady=4, bd=5, state=tk.DISABLED, command=lambda: yesResponse(word.get()))
yes_button.place(relx=0.275, rely=0.915)

no_button = tk.Button(canvas, text='No', padx=40,
                      pady=4, bd=5, state=tk.DISABLED, command=noResponse)
no_button.place(relx=0.6, rely=0.915)

clear_button = tk.Button(canvas, text='Clear All',
                         padx=20, pady=4, bd=5, command=noResponse)
clear_button.place(relx=0.445, rely=0.915)

lower_frame = tk.Frame(root, bg='turquoise1', bd=5)
lower_frame.place(relx=0.15, rely=0.25, relheight=0.65, relwidth=0.75)

label = tk.Label(lower_frame, bg='azure', text='', font=(
    'Courier', 12), anchor='nw', justify='left', bd=3, wraplength=475)
label.place(relwidth=1, relheight=1)

root.mainloop()
