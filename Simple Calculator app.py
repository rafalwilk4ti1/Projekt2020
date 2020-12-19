from tkinter import *

#Define window
root = Tk()
root.title("Calculator")
root.iconbitmap('C:/Users/rafal/Desktop/WILK RAFAŁ/NAUKA/Programowanie/Python i GIT/THEArtOFDoing GUI apps/Exercises/calc.ico')
root.geometry('300x400')
root.resizable(0,0)


#Define functions

def clear_f():
    entry_1.delete(0,END)

    enable_buttons()

def quit_f():
    root.quit()

def display(number):
    entry_1.insert(END, number)

    #If we have a dot, we don't want to have the second one 
    if '.' in entry_1.get():
        button_p.config(state=DISABLED)

def operate(operator):
    global operation
    global first_number

    operation = operator
    first_number = entry_1.get()

    #We delete the value (first_number) to have clear window 
    entry_1.delete(0, END)


    #If we have pressed 'multiply_button' for insistance, we don't want to have pressed the other button 

    add_button.config(state=DISABLED)
    b_1_x_button.config(state=DISABLED)
    power_2_button.config(state=DISABLED)
    power_n_button.config(state=DISABLED)
    multiple_button.config(state=DISABLED)
    divide_button.config(state=DISABLED)
    substraction_button.config(state=DISABLED)

    #Nonetheless we back to normal while 'equal_button' or 'button_p' had been pressed
    button_p.config(state=NORMAL)



def equal():
    """Run a math"""
    if operation == 'add':
        value = float(first_number) + float(entry_1.get())
    elif operation == 'divide':
        if entry_1.get() !=0 and first_number!=0:
            value = float(first_number) / float(entry_1.get())
        else:
            value = "ERROR"
    elif operation == 'multiply':
        value = float(first_number) * float(entry_1.get())
    elif operation == 'substract':
        value = float(first_number) - float(entry_1.get())
    elif operation == 'exponent':
        value = float(first_number) ** float(entry_1.get())
    
    entry_1.delete(0,END)

    entry_1.insert(0,value)


    enable_buttons()

def enable_buttons():
    """Enable all buttons on the calculator"""
    button_p.config(state=NORMAL)
    add_button.config(state=NORMAL)
    b_1_x_button.config(state=NORMAL)
    power_2_button.config(state=NORMAL)
    power_n_button.config(state=NORMAL)
    multiple_button.config(state=NORMAL)
    divide_button.config(state=NORMAL)
    substraction_button.config(state=NORMAL)  

def inverse():
    """Calculate the inverse of a given number. """
    #Do not allow fo 1/0
    if entry_1.get() == '0':
        value = "ERROR"
    else:
        value = 1/float(entry_1.get())

    entry_1.delete(0,END)

    entry_1.insert(0,value)

def square():
    if entry_1.get()=='0':
        value = float(1)
    else: 
        value = float(entry_1.get()) **2
    
    entry_1.delete(0,END)
    entry_1.insert(0,value)

def negate():
    "Negate a given number"
    value = -1*float(entry_1.get())

    entry_1.delete(0,END)
    entry_1.insert(0,value)

#deafult configuration
number_color = '#01110A'
function_color = '#54C6EB'
clear_quit = '#CDA2AB'
bg_colour = '#95A3A4'
button_font = ('Arial',18)
display_font=('Arial',30)
#font_calculator = Font(family='Times New Roman',size=12)
root.config(bg=bg_colour)


#Define labels
first_frame = Frame(root,bg=bg_colour)
second_frame = Frame(root)

first_frame.pack(padx=2, pady=(5,20))
second_frame.pack(padx=2,pady=5)


#Define text
entry_1 = Entry(first_frame,width=50,borderwidth=5, font=display_font,bg='white',justify=RIGHT)
entry_1.pack(padx=5,pady=5)


#Define buttons - label_2
clear_b = Button(second_frame,text='Clear',font=button_font,command=clear_f,bg=clear_quit,fg='black')
quit_b = Button(second_frame,text=' Quit ',font=button_font,command=quit_f,bg=clear_quit,fg='black')

clear_b.grid(row=0, column=0,columnspan=2,sticky='WE',pady=1)
quit_b.grid(row=0, column=2,columnspan=2,sticky='WE',pady=1)

#Third row (Add padding to creat the size of the column because the largest size set the width)
#Define buttons - label_3
b_1_x_button = Button(second_frame,text='1/x',font=button_font,bg=function_color,command=inverse)
power_2_button = Button(second_frame,text='x^2',font=button_font,bg=function_color,command=square)
power_n_button = Button(second_frame,text='x^n',font=button_font,bg=function_color,command=lambda: operate('exponent'))
divide_button = Button(second_frame,text=' / ',font=button_font,bg=function_color,command=lambda: operate('divide'))

b_1_x_button.grid(row=1, column=0,pady=1,sticky="WE",ipadx=11)
power_2_button.grid(row=1, column=1,pady=1,sticky="WE",ipadx=11)
power_n_button.grid(row=1, column=2,pady=1,sticky="WE",ipadx=11)
divide_button.grid(row=1, column=3,pady=1,sticky="WE",ipadx=11)

#Define buttons - row_4

button_7 = Button(second_frame,text=' 7 ',font=button_font,bg='black',fg='white',command=lambda: display(7))
button_8 = Button(second_frame,text=' 8 ',font=button_font,bg='black',fg='white',command=lambda: display(8))
button_9 = Button(second_frame,text=' 9 ',font=button_font,bg='black',fg='white',command=lambda: display(9))
multiple_button = Button(second_frame,text=' * ',font=button_font,bg=function_color,command=lambda: operate('multiply'))

button_7.grid(row=2, column=0,pady=1,sticky="WE")
button_8.grid(row=2, column=1,pady=1,sticky="WE")
button_9.grid(row=2, column=2,pady=1,sticky="WE")
multiple_button.grid(row=2, column=3,pady=1,sticky="WE")


#Define buttons - row_5

button_4 = Button(second_frame,text=' 4 ',font=button_font,bg='black',fg='white',command=lambda: display(4))
button_5 = Button(second_frame,text=' 5 ',font=button_font,bg='black',fg='white',command=lambda: display(5))
button_6 = Button(second_frame,text=' 6 ',font=button_font,bg='black',fg='white',command=lambda: display(6))
substraction_button = Button(second_frame,text=' - ',font=button_font,bg=function_color,command=lambda: operate('substract'))

button_4.grid(row=3, column=0,pady=1,sticky="WE")
button_5.grid(row=3, column=1,pady=1,sticky="WE")
button_6.grid(row=3, column=2,pady=1,sticky="WE")
substraction_button.grid(row=3, column=3,pady=1,sticky="WE")

#Define buttons - row_6

button_1 = Button(second_frame,text=' 1 ',font=button_font,bg='black',fg='white',command=lambda: display(1))
button_2 = Button(second_frame,text=' 2 ',font=button_font,bg='black',fg='white',command=lambda: display(2))
button_3 = Button(second_frame,text=' 3 ',font=button_font,bg='black',fg='white',command=lambda: display(3))
add_button = Button(second_frame,text=' + ',font=button_font,bg=function_color,command=lambda: operate('add'))

button_1.grid(row=4, column=0,pady=1,sticky="WE")
button_2.grid(row=4, column=1,pady=1,sticky="WE")
button_3.grid(row=4, column=2,pady=1,sticky="WE")
add_button.grid(row=4, column=3,pady=1,sticky="WE")

#Define labels - row_7

plus_minus_button = Button(second_frame,text='+/-',font=button_font,bg='black',fg='white',command=negate)
button_0 = Button(second_frame,text=' 0 ',font=button_font,bg='black',fg='white',command=lambda: display(0))
button_p = Button(second_frame,text=' . ',font=button_font,bg='black',fg='white',command=lambda: display('.'))
equal_button = Button(second_frame,text=' = ',font=button_font,command=equal,bg=function_color)

plus_minus_button.grid(row=5, column=0,pady=1,sticky="WE")
button_0.grid(row=5, column=1,pady=1,sticky="WE")
button_p.grid(row=5, column=2,pady=1,sticky="WE")
equal_button.grid(row=5, column=3,pady=1,sticky="WE")




#run root mainloop
root.mainloop()
