#   <a target="_blank" href="https://icons8.com/icon/86112/lock">Padlock</a>
#   icon by <a target="_blank" href="https://icons8.com">Icons8</a>

import random
import string
import tkinter as tk
import ttkbootstrap as ttk
import pyperclip

themes = ["darkly", "darkly", "vapor", "minty", "lumen"]


def theme_change(*args):
    selected_theme = set_theme.get()
    master.style.theme_use(selected_theme)


master = ttk.Window(themename="darkly",
                    iconphoto="icon.png")
master.title('Locksmith')
master.geometry("420x300")
master.resizable(False, False)

set_theme = ttk.StringVar()

set_theme.trace_add("write", theme_change)
set_theme.set("darkly")

top_frame = ttk.Frame(master)
top_frame.pack(fill='x')

theme = ttk.OptionMenu(top_frame, set_theme, *themes)
theme.pack(anchor="nw", side="left")


def length_value(value):
    slider_value.set("Length: " + str(value))
    generate(value)


def generate(value):
    value = int(value)
    generated_password = string.ascii_letters + string.digits + string.punctuation + string.hexdigits
    password = ''.join(random.choice(generated_password) for i in range(value))
    # max value: 128

    if 64 > len(password) > 32:
        output_string.set(password[:32] + '\n' + password[32:])
    elif 96 > len(password) >= 64:
        output_string.set(password[:32] + '\n' + password[32:64] + '\n' + password[64:])
    elif len(password) >= 96:
        output_string.set(password[:32] + '\n' + password[32:64] + '\n' + password[64:96] + '\n' + password[96:64])
    else:
        output_string.set(password)


def copy_to_clipboard():
    password = output_string.get()
    password = password.replace('\n', '')
    copy.config(text=" Password \n   copied")
    pyperclip.copy(password)
    master.after(1250, reset_copy)


def reset_copy():
    copy.config(text="     Copy\n  password")


title = ttk.Label(master, text="LOCKSMITH", font="Consolas 20 bold")
title.pack(anchor="center")

input_frame = ttk.Frame(master)
input_frame.pack()

#   used to be a button to generate password
gen = ttk.Button(input_frame, text="  Generate\n  password", command=generate)
gen.pack(side="right", padx=50)

copy = ttk.Button(input_frame, text="     Copy\n  password", command=copy_to_clipboard)
copy.pack(side="left", padx=50)
event = copy.config(text="     Copy\n  password")

output_string = tk.StringVar()
output_label = ttk.Label(master, text="OUTPUT", font="Consolas 14", textvariable=output_string)
output_label.pack(side="top", pady=5)

slider_value = tk.StringVar()
length_slider = tk.Scale(master, from_=8, to=128, length=256, orient="horizontal", command=length_value)
length_slider.set(12)
length_slider.pack(side="bottom", pady=25)
length_text = tk.Label(master, textvariable=slider_value)
length_text.pack(side="bottom")

length_value(length_slider.get())

master.mainloop()
