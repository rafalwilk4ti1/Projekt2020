#Metric helper
from tkinter import *
from tkinter import ttk


#Define function
def metric_helper():

    metric_values = {
        'femto':10**-15, 
        'pico':10**-12,
        'nano':10**-9,
        'micro':10**-6,
        'milli':10**-3,
        'centi':10**-2,
        'deci':10**-1,
        'base value':10**0,
        'deca':10**1,
        'hecto':10**2,
        'kilo':10**3,
        'mega':10**6,
        'giga':10**9,
        'tera':10**12,
        'peta':10**15
    }
    #Clear the output field
    second_entry.delete(0, END)
    #Get all user information
    start_form = first_entry.get()
    metric_1 = option_window_input.get()
    metric_2 = option_window_output.get()

    #Converting numbers
    before_mod = float(start_form) * float(metric_values[metric_1])
    after_mod = float(before_mod) / float(metric_values[metric_2])

    second_entry.insert(0, str(after_mod))

#Define functions
def clear(event):
    first_entry.delete(0, END)

    


def back_to_normal(root):
    len_first = first_entry.get()
    print(root.x, root.y)
    if len(len_first) <19 and root.x > 175 and root.y > 25:
        first_entry.insert(0,'Enter your quantity')


            
        


#Define window
root = Tk()
root.title('Metric Helper')
root.iconbitmap('C:/Users/rafal/Desktop/WILK RAFAŁ/NAUKA/Programowanie/Python i GIT/THEArtOFDoing GUI apps/Exercises/ruler.ico')
root.geometry('470x130')
root.resizable(0,0)

bg_colour = '#EE6C4D'
button_colour = "#F38D68"
root.config(bg=bg_colour)

#Define label
first_label = Label(root, text='=', bg=bg_colour)
first_label.grid(row=0,column=1,ipadx=20)

#Define entries
first_entry = Entry(root, justify='center')
first_entry.grid(row=0,column=0,ipadx=20)
first_entry.insert(0, 'Enter your quantity')
first_entry.bind("<Button-1>",clear)


second_entry = Entry(root, justify='center')
second_entry.grid(row=0,column=2,ipadx=20)


#define a list to choose metric
list_of_metrics = ['femto', 'pico', 'nano', 'micro', 'milli', 'centi', 'deci','base value','deca', 'hecto', 'kilo', 'mega','giga', 'tera','peta']

#define vars to set type 
input_choice = StringVar()
output_choice = StringVar()

#define optionMenu
option_window_input = ttk.Combobox(root,value=list_of_metrics,justify='center')
option_window_output = ttk.Combobox(root,value=list_of_metrics, justify='center')
option_window_input.set('base value')
option_window_output.set('base value')


second_label = Label(root, text='to', bg=bg_colour)

second_label.grid(row=1,column=1,padx=20,pady=10)
option_window_input.grid(row=1, column=0,sticky='e',padx=20,pady=10)
option_window_output.grid(row=1, column=2,sticky='w',padx=20,pady=10)

#Creating button to convert
convert_button = Button(root,bg=button_colour,text='Convert',justify='left', command=metric_helper)
convert_button.grid(row=2,column=1,ipadx=20,ipady=10)

#creating clear and typing
root.bind("<Button-1>",back_to_normal)

#run root mainloop
root.mainloop()




