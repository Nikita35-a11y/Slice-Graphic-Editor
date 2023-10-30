import tkinter as tk
from tkinter import SUNKEN
from tkinter import colorchooser
from tkinter import HORIZONTAL


def onChoose():
    color = colorchooser.askcolor()[1]
    print(color)
    frame.config(bg=color)


def paint(event):
    get = int(entry_width.get())

    x1, y1 = (event.x - 1), (event.y - 1)
    x2, y2 = (event.x + 1), (event.y + 1)
    canvas.create_oval(x1, y1, x2, y2, fill="black", width=get)


def erase(event):
    get = int(entry_width.get())

    x1, y1 = (event.x - 1), (event.y - 1)
    x2, y2 = (event.x + 1), (event.y + 1)
    canvas.create_oval(x1, y1, x2, y2, fill="white", outline="white", width=get)


root = tk.Tk()
root.title("Drawing Canvas")

canvas = tk.Canvas(root, bg="white", width=750, height=500)
canvas.pack(side="top", fill="x")

canvas.bind("<B1-Motion>", paint)
canvas.bind("<B3-Motion>", erase)

button_color = tk.Button(text="Цвет Кисти", width=10, command=onChoose)
button_color.pack(side="bottom", anchor="center", pady=5)

label_width = tk.Label(text="Размер кисти")
label_width.pack(side="bottom", anchor="center")

entry_width = tk.Scale(root, orient=HORIZONTAL, length=200, from_=1.0, to=1000)
entry_width.pack(side="bottom", anchor="center")

frame = tk.Frame(root, border=1, relief=SUNKEN, width=100, height=100)
frame.pack(side="bottom", anchor="center", pady=2)

if __name__ == '__main__':
    root.geometry("1000x700")
    root.configure(background="#262626")
    root.mainloop()
