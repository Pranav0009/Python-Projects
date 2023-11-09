import tkinter as tk
from PIL import Image, ImageTk
import random 

window = tk.Tk()
window.title("Dice Roll")
window.geometry("500x360")

dice = ["dice1.png","dice2.png","dice3.png","dice4.png","dice5.png","dice6.png"]

image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
image2 = ImageTk.PhotoImage(Image.open(random.choice(dice)))

label1 = tk.Label(window,image=image1)
label2 = tk.Label(window,image=image2)

label1.place(x = 60 , y = 100)
label2.place(x = 300 , y = 100)

def roll():
    image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    label1.configure(image=image1)
    label1.image = image1

    image2 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    label2.configure(image=image2)
    label2.image = image2

button = tk.Button(window,text="ROLL", bg="green", height = 3, width=7,fg="white",command=roll)
button.place(x = 220 , y = 20)


window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")

window.mainloop()