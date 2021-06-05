from tkinter import *

#structure
calc = Tk()
calc.title("Calculator")
calc.geometry("312x324")
calc.resizable(0,0)

io_frame = Frame(calc, width = 312, height = 50, bd = 0)
io_frame.pack(side = TOP)

text = StringVar()
expression = ""

#frame for input/output result
io_field = Entry(io_frame, textvariable = text, width = 52, bg = "grey", bd = 0, justify= RIGHT)
io_field.pack(ipady = 25)

#frame for buttons
btn_frame = Frame(calc, width = 312, height = 273, bg = "black")
btn_frame.pack()

#defining buttons
def click(item):
    global expression
    expression = expression + str(item)
    text.set(expression)

def clear():
    global expression
    expression = ""
    text.set(expression)

def equal(item):
    global expression
    result = str(eval(expression))
    text.set(result)

#placing buttons
#Row-0
clr = Button(btn_frame, text = "C", fg = "white", width = 22, height = 3, bd = 0, bg = "black", cursor = "hand2", command = lambda: clear()).grid(row = 0, column = 0, columnspan = 2)
percent = Button(btn_frame, text="%", fg = "white", width = 10, height = 3, bd = 0, bg="black", cursor = "hand2", command = lambda: click("%")).grid(row = 0, column = 2)
divide = Button(btn_frame, text = "/", fg = "white", width = 10, height = 3, bd = 0, bg = "black", cursor = "hand2", command = lambda: click("/")).grid(row = 0, column = 3)

#Row-1
seven = Button(btn_frame, text = "7", fg = "white", width = 10, height = 3, bd = 0, bg = "black", cursor = "hand2", command = lambda: click(7)).grid(row = 1, column = 0)
eight = Button(btn_frame, text = "8", fg = "white", width = 10, height = 3, bd = 0, bg = "black", cursor = "hand2", command = lambda: click(8)).grid(row = 1, column = 1)
nine = Button(btn_frame, text = "9", fg = "white", width = 10, height = 3, bd = 0, bg = "black", cursor = "hand2", command = lambda: click(9)).grid(row = 1, column = 2)
multiply = Button(btn_frame, text = "*", fg = "white", width = 10, height = 3, bd = 0, bg = "black", cursor = "hand2", command = lambda: click("*")).grid(row = 1, column = 3)

#Row-2
four = Button(btn_frame, text = "4", fg = "white", width = 10, height = 3, bd = 0, bg = "black", cursor = "hand2", command = lambda: click(4)).grid(row = 2, column = 0)
five = Button(btn_frame, text = "5", fg = "white", width = 10, height = 3, bd = 0, bg = "black", cursor = "hand2", command = lambda: click(5)).grid(row = 2, column = 1)
six = Button(btn_frame, text = "6", fg = "white", width = 10, height = 3, bd = 0, bg = "black", cursor = "hand2", command = lambda: click(6)).grid(row = 2, column = 2)
subtract = Button(btn_frame, text = "-", fg = "white", width = 10, height = 3, bd = 0, bg = "black", cursor = "hand2", command = lambda: click("-")).grid(row = 2, column = 3)

#Row-3
one = Button(btn_frame, text = "1", fg = "white", width = 10, height = 3, bd = 0, bg = "black", cursor = "hand2", command = lambda: click(1)).grid(row = 3, column = 0)
two = Button(btn_frame, text = "2", fg = "white", width = 10, height = 3, bd = 0, bg = "black", cursor = "hand2", command = lambda: click(2)).grid(row = 3, column = 1)
three = Button(btn_frame, text = "3", fg = "white", width = 10, height = 3, bd = 0, bg = "black", cursor = "hand2", command = lambda: click(3)).grid(row = 3, column = 2)
add = Button(btn_frame, text = "+", fg = "white", width = 10, height = 3, bd = 0, bg = "black", cursor = "hand2", command = lambda: click("+")).grid(row = 3, column = 3)

#Row-4
zero = Button(btn_frame, text = "0", fg = "white", width = 22, height = 3, bd = 0, bg = "black", cursor = "hand2", command = lambda: click("0")).grid(row = 4, column = 0, columnspan = 2)
decimalPointer = Button(btn_frame, text=".", fg = "white", width = 10, height = 3, bd = 0, bg="black", cursor = "hand2", command = lambda: click(".")).grid(row = 4, column = 2)
equalsTo = Button(btn_frame, text = "=", fg = "white", width = 10, height = 3, bd = 0, bg = "black", cursor = "hand2", command = lambda: click("=")).grid(row = 4, column = 3)

#run calculator
calc.mainloop()