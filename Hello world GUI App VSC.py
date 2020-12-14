import tkinter
from tkinter import X, Y, BOTH, IntVar, END
import PIL
from PIL import ImageTk
from PIL import Image


#Define a window

root = tkinter.Tk()
root.title('Hello world GUI App')
root.iconbitmap('C:/Users/rafal/Desktop/WILK RAFAŁ/NAUKA/Programowanie/Python i GIT/THEArtOFDoing GUI apps/Exercises/wave.ico')
root.geometry("500x500")
root.resizable(1,1)


#Define fonts and colors
root_color = '#224870'
input_color = '#2a4494'
output_color = '#4ea5d9'
root.config(bg=root_color)

#Define functions
def printer():
    if number.get() == 1:
        text = tkinter.Label(lower_frame, text=str('Hello ')+input_window.get()+'! Keep learning Tkinter! :)',bg=output_color)#getting entry window and print it
        text.pack()
    elif number.get()==2:
        text = tkinter.Label(lower_frame, text=str("Hello "+str(input_window.get())+"! Keep learning Tkinter! :)").upper(), bg=output_color)#the same function ^, with one example concerning size of letters
        text.pack()
    else:
        text = tkinter.Label(lower_frame, text="You need to choose one of the options!", bg=output_color)
        text.pack()
    input_window.delete(0,END)



#define frame

higher_frame = tkinter.LabelFrame(root, bg=input_color)
higher_frame.pack(pady=10)

lower_frame=tkinter.LabelFrame(root,bg=output_color)
lower_frame.pack(padx=10,pady=(0,10), fill=BOTH, expand=True)

#define widget
number = IntVar() 
number.set(0)
input_window = tkinter.Entry(higher_frame, text='Enter your name', width=20)
button_1 = tkinter.Button(higher_frame,text='Submit',command = printer)
input_window.grid(padx=10, pady=10)
button_1.grid(row=0,column=1, pady=0, padx=20, ipadx=25,ipady=0)

radio1 = tkinter.Radiobutton(higher_frame, text='Normal case', bg=input_color, variable=number, value=1,activebackground=input_color)
radio1.grid()
radio2 = tkinter.Radiobutton(higher_frame, text='Upper case',bg=input_color,variable = number, value=2,activebackground=input_color)
radio2.grid(sticky='e',column=1, row=1, padx=20)


#insert a photo of smiling face
smile_image = tkinter.PhotoImage(file='C:/Users/rafal/Desktop/WILK RAFAŁ/NAUKA/Programowanie/Python i GIT/THEArtOFDoing GUI apps/Exercises/smile.png')
smile_label = tkinter.Label(lower_frame,image=smile_image, bg=output_color)
smile_label.pack()




#run root main's loop
root.mainloop()