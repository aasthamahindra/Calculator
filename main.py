from tkinter import *

#structure
calc = Tk()
calc.title("Calculator")
calc.geometry("312x324")
calc.resizable(0,0)

io_frame = Frame(calc, width = 312, height = 50, bd = 0)
io_frame.pack(side = TOP)

text = StringVar()

#frame for input/output result
io_field = Entry(io_frame, font = ('Arial', 18, 'bold'), textvariable = text, width = 50, bg = "grey", bd = 0, justify = RIGHT)
io_field.pack(ipady = 30)

#frame for buttons
btn_frame = Frame(calc, width = 312, height = 273, bg = "black")
btn_frame.pack()

#run calculator
calc.mainloop()