import tkinter as tk
from tkinter.filedialog import askopenfilename
from DocumentParser import DocumentParser


def get_file_name():
    f = askopenfilename()
    file_entry.delete(0, tk.END)
    file_entry.insert(tk.END, f)


def execute():
    options = {
        'style_choice': style_choice.get(),
        'dot': dot_choice.get(),
        'space': space_choice.get(),
        'q_roll_start': question_no.get() - 1
    }
    DocumentParser(file_entry.get(), options)


window = tk.Tk()
window.title('Question formatter - MUA')
window.geometry("800x600")

# Title group
title = tk.Label(master=window, text="Question Formatter", font=("Arial", 28))
title.grid()

# File Entry
file_entry = tk.Entry(master=window, width=60)
file_entry.grid()

choose_file = tk.Button(master=window, text="Choose file...", command=get_file_name)
choose_file.grid()

# Q_number
tk.Label(master=window, text="Question number to start with").grid()
question_no = tk.Scale(master=window, from_=1, to=100, orient=tk.HORIZONTAL)
question_no.grid()

# Radio group - Style
tk.Label(master=window, text="Select a style for the options").grid()
style_choice = tk.IntVar()
option1 = tk.Radiobutton(master=window, text="(A)", variable=style_choice, value=1)
option2 = tk.Radiobutton(master=window, text="A)", variable=style_choice, value=2)
style_choice.set(1)

option1.grid()
option2.grid()

# Radio group - Dot
tk.Label(master=window, text="Should there be a dot").grid()
dot_choice = tk.BooleanVar()
option3 = tk.Radiobutton(master=window, text="(A)", variable=dot_choice, value=False)
option4 = tk.Radiobutton(master=window, text="(A).", variable=dot_choice, value=True)
dot_choice.set(False)

option3.grid()
option4.grid()

# Radio group - Space
tk.Label(master=window, text="Should there be a space").grid()
space_choice = tk.BooleanVar()
option5 = tk.Radiobutton(master=window, text="(A)Option", variable=space_choice, value=False)
option6 = tk.Radiobutton(master=window, text="(A) Option", variable=space_choice, value=True)
space_choice.set(False)

option5.grid()
option6.grid()

execute = tk.Button(text="Start", command=execute)
execute.grid()

window.mainloop()
