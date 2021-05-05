from tkinter import *

# Create application window
window = Tk()
window.title('Simple Calculator')
window.resizable(False, False)
first_num = 0.0
second_num = 0.0
operation = ''

# Create text box for numbers and add it into the window
text_box = Entry(window, width=14, font=('Arial', 36), justify=RIGHT)
text_box.grid(row=0, column=0, columnspan=4)

# Function to insert numbers into the textbox
def insert_number(number):
    text_box.insert(END, number)

# Function to clear the textbox
def clear():
    text_box.delete(0, END)

# Function to square number
def square():
    square = float(text_box.get())**2
    text_box.delete(0, END)
    if square % 1 == 0:
        text_box.insert(END, int(square))
    else:
        text_box.insert(END, square)

# Function sets up for the adding operation
def add():
    global first_num 
    first_num = float(text_box.get())
    text_box.delete(0, END)
    global operation 
    operation = '+'

# Function sets up for the subtracting operation
def sub():
    global first_num
    first_num = float(text_box.get())
    text_box.delete(0, END)
    global operation
    operation = '-'

# Function sets up for the multiplication operation
def mul():
    global first_num
    first_num = float(text_box.get())
    text_box.delete(0, END)
    global operation
    operation = '*'

# Function sets up for the division operation
def div():
    global first_num
    first_num = float(text_box.get())
    text_box.delete(0, END)
    global operation
    operation = '/'

# Function switches the number between negative and positive
def neg():
    global first_num
    first_num = float(text_box.get())
    ans = first_num * -1
    text_box.delete(0, END)
    if ans % 1 == 0:
            text_box.insert(END, int(ans))
    else:
        text_box.insert(END, ans)

# Function completes each operation
def equals():

    if operation == '+':
        second_num = float(text_box.get())
        text_box.delete(0, END)
        ans = first_num + second_num
        if ans % 1 == 0:
            text_box.insert(END, int(ans))
        else:
            text_box.insert(END, ans)

    elif operation == '-':
        second_num = float(text_box.get())
        text_box.delete(0, END)
        ans = first_num - second_num
        if ans % 1 == 0:
            text_box.insert(END, int(ans))
        else:
            text_box.insert(END, ans)

    elif operation == '*':
        second_num = float(text_box.get())
        text_box.delete(0, END)
        ans = first_num * second_num
        if ans % 1 == 0:
            text_box.insert(END, int(ans))
        else:
            text_box.insert(END, ans)

    elif operation == '/':
        second_num = float(text_box.get())
        text_box.delete(0, END)
        ans = first_num / second_num
        if ans % 1 == 0:
            text_box.insert(END, int(ans))
        else:
            text_box.insert(END, ans)       

# Create all the buttons and add them into the window
button_1 = Button(window, text='1', padx=30, pady=30, command=lambda:insert_number(1))
button_1.grid(row=4, column=0)
button_2 = Button(window, text='2', padx=30, pady=30, command=lambda:insert_number(2))
button_2.grid(row=4, column=1)
button_3 = Button(window, text='3', padx=30, pady=30, command=lambda:insert_number(3))
button_3.grid(row=4, column=2)
button_add = Button(window, text='+', padx=29, pady=30, command=add)
button_add.grid(row=4, column=3)

button_4 = Button(window, text='4', padx=30, pady=30, command=lambda:insert_number(4))
button_4.grid(row=3, column=0)
button_5 = Button(window, text='5', padx=30, pady=30, command=lambda:insert_number(5))
button_5.grid(row=3, column=1)
button_6 = Button(window, text='6', padx=30, pady=30, command=lambda:insert_number(6))
button_6.grid(row=3, column=2)
button_sub = Button(window, text='-', padx=29, pady=30, command=sub)
button_sub.grid(row=3, column=3)

button_7 = Button(window, text='7', padx=30, pady=30, command=lambda:insert_number(7))
button_7.grid(row=2, column=0)
button_8 = Button(window, text='8', padx=30, pady=30, command=lambda:insert_number(8))
button_8.grid(row=2, column=1)
button_9 = Button(window, text='9', padx=30, pady=30, command=lambda:insert_number(9))
button_9.grid(row=2, column=2)
button_mul = Button(window, text='*', padx=29, pady=30, command=mul)
button_mul.grid(row=2, column=3)

button_0 = Button(window, text='0', padx=70, pady=30, command=lambda:insert_number(0))
button_0.grid(row=5, column=0, columnspan=2)
button_dot = Button(window, text='.', padx=33, pady=30, command=lambda:insert_number('.'))
button_dot.grid(row=5, column=2)
button_equals = Button(window, text='=', padx=29, pady=30, command=equals)
button_equals.grid(row=5, column=3)

button_c = Button(window, text='C', padx=30, pady=30, command=clear)
button_c.grid(row=1, column=0)
button_neg = Button(window, text='+/-', padx=25, pady=30, command=neg)
button_neg.grid(row=1, column=1)
button_pow2 = Button(window, text='x^2', padx=23, pady=30, command=square)
button_pow2.grid(row=1, column=2)
button_div = Button(window, text='/', padx=31, pady=30, command=div)
button_div.grid(row=1, column=3)

window.mainloop() # Loop for program to stay open