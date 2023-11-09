import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()
root.title("Temperature Converter")
root.geometry("900x510")


PRIMARY_COLOR = "Black"
SECONDARY_COLOR = "yellow"
PRIME_SHADE = "#303030"
SECONDARY_SHADE = "#136C38"

def getFont(size = 9, bold = False):
    return ("TkDefaultFont", size, "bold" if bold else "normal")

def validate(P):
    empty = P ==""
    digit = empty or P[-1].isdigit()
    minus = P == "-" and len(P) == 1
    decimal = P.count(".") == 1
    out = empty or digit or minus or decimal
    return out

calFunc = {
    "cf": lambda x: (x * 9/5) + 32,
    "fc": lambda x: (x - 32) * 5/9,
    "ck": lambda x: x + 273.15,
    "kc": lambda x: x - 273.15
}

calFunc["fk"] = lambda x: calFunc["ck"](calFunc["fc"](x))
calFunc["kf"] = lambda x: calFunc["cf"](calFunc["kc"](x))

def convert(fromInpt, fromUnitVar, toUnitVar, resultVar):
    fromU = fromUnitVar.get().lower()
    toU = toUnitVar.get()[0].lower()

    try:
        val = float(fromInpt.get())
    except ValueError:
        resultVar.set("Error !!")
        return
    
    if fromU == toU:
        res = val 
    else:
        res = calFunc[fromU + toU](val)

    resultVar.set(f"{res:.2f}")  # Format the result to 2 decimal places

reg = root.register(validate)

borderFrame = tk.Frame(root, bg = SECONDARY_COLOR, width=450, height=510)
borderFrame.place(x=0, y=0)

leftFrame = tk.Frame(borderFrame, bg = PRIMARY_COLOR, width = 440, height = 500)
leftFrame.place(x=5, y=5)

enterLabel = tk.Label(leftFrame, text="Enter Temperature", bg=PRIMARY_COLOR, fg=SECONDARY_COLOR, font = getFont(16, True))
enterLabel.place(x=30, y=30)

degLabel = tk.Label(leftFrame, text = "Degree", bg=PRIMARY_COLOR, fg=SECONDARY_COLOR, font = getFont(9))
degLabel.place(x = 30, y = 120)

inputEntry = tk.Entry(leftFrame, bg = PRIME_SHADE,fg = "#ffffff", insertbackground ="#ffffff", borderwidth = 5, relief = "flat", validatecommand=(reg, "%P"), validate = "key")
inputEntry.place(x = 30, y = 160, width = 265, height = 42)

unitVar = tk.StringVar(root)
unitVar.set("C")

convertVar = tk.StringVar(root)
convertVar.set("Fahrenheit")

s = ttk.Style()
s.configure("unit.TMenuButton", background = SECONDARY_COLOR)
s.configure("unit.TMenuButton", relief = "flat")

s.configure("covertTo.TMenuButton", relief = "flat")
s.configure("covertTo.TMenuButton", background = PRIME_SHADE)
s.configure("covertTo.TMenuButton", foreground = "#ffffff")
s.configure("covertTo.TMenuButton", width = 320)

unitMenu = ttk.OptionMenu(leftFrame, unitVar, "C","C","F","K")
unitMenu.place(x=300, y=160, width=110, height=42)

convertLabel = tk.Label(leftFrame, text = "Convert To", bg = PRIMARY_COLOR , fg = SECONDARY_COLOR, font = getFont(9))
convertLabel.place(x=30, y=280)

convertMenu = ttk.OptionMenu(leftFrame, convertVar, "Fahrenheit", "Celsius", "Kelvin" )
convertMenu.place(x=30, y=320, width=380, height=42)

convertButton = tk.Button(leftFrame, text="Convert", bg=SECONDARY_COLOR, fg=PRIMARY_COLOR, font=getFont(12), relief="flat", activebackground=SECONDARY_SHADE , bd=0)
convertButton.place(x=150, y=420, width=140, height=40)

rightFrame = tk.Frame(root, bg=SECONDARY_COLOR,width=450,height=510)
rightFrame.place(x=450, y=0)

resultVar = tk.StringVar(root)
resultVar.set("")

resultLabel = tk.Label(rightFrame, textvariable=resultVar, bg=SECONDARY_COLOR, fg=PRIMARY_COLOR, font=getFont(64, True))
resultLabel.place(relx=0.5, rely=0.4901, anchor= tk.CENTER)

convertButton.configure(command= lambda:convert(inputEntry, unitVar,convertVar,resultVar))

root.mainloop()