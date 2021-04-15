from tkinter import *
from tkinter import StringVar, IntVar, scrolledtext, END, messagebox, filedialog, CENTER

#Define functions 
def change_font(*args):
    font_1 = str(type_1.get())
    font_2 = int(size_1.get())
    font_3 = str(mode_1.get())
    x = 0
    if x < 1:
        font_1 = type_1.get()
        font_2 = size_1.get()
        font_3 = mode_1.get()

        if font_3 != 'none':
            my_font = (font_1,font_2,font_3)
        else:
            my_font = (font_1,font_2)
    input_text.config(font=my_font)

def open_file():
    window = filedialog.askopenfilename(initialdir="/")
    x = ""
    for i in window:
        x = x+(str(i))
    with open(x,'r') as f1:
        z = ""
        for y in f1:
            z = z+(str(y))
    ask = messagebox.askyesno("Open the other file","Are you sure to open the other file? Your unsafed file will be destroyed.")
    if ask:
        input_text.delete(0.0,END)
        input_text.insert(0.0,z)
    
def safe_our_main():
    ask = filedialog.asksaveasfilename()
    with open(ask,'w') as f1:
        for x in input_text.get(0.0,END):
            f1.write(x)

def safe_other_file(option_1,data_1):
    with open(option_1,'w') as f1:
        for x in data_1:
            f1.write(x)

def change_normal():
    input_text.delete(0.0, END)
    type_1.set("Terminal")
    size_1.set(12)
    mode_1.set('none')

def open_new():
    ask_2 = messagebox.askyesnocancel("Open a new file", "Are you sure?")
    #None False True
    if ask_2:
        ask_3 = messagebox.askyesno("Save a file", "Would you like to safe a file?")
        if ask_3:
            ask_4 = filedialog.asksaveasfilename()
            data_1 = input_text.get(0.0, END)
            safe_other_file(ask_4,data_1)
            
        else:
            change_normal()
def close():
    ask = messagebox.askyesno("Close the window","Are you sure?")
    if ask:
        root.destroy()
        root.quit()

def donothing():
    info = messagebox.showinfo("Info","I am working on it")
def change_color():
    if var.get() == False:
        bg_colour = '#E6F14A'
        root.config(bg='red',menu=menubar)
        input_text.config(bg='white')
        frame_1.config(bg=bg_colour)
    elif var.get():
        bg_colour = '#575D90'
        root.config(bg=bg_colour)
        input_text.config(bg='#84A07C')
        frame_1.config(bg='black')

def about_me():
    root2=Tk()
    root2.title("About me")
    root2.geometry('400x400')
    root2.resizable(0,0)
    root2.config(bg='black')

    text_window = Label(root2)
    var1 = Text(text_window,font=('Terminal',6,'italic'),fg='green',bg='black')
    var1.insert(INSERT, " Hello. I am Rafał I have been learning \n Python and I hope this program \n it is just the  BEGIN! I am \n cooperative, and really resourcefull. \nI am going to learn Python by the moment I get the job, then I want to start learning C# and start making a wonderful games for everybody, and  creating  software for\n the biggest entriprises on the Earth. If your read this, wish me luck :)" )
    var1.pack()
    text_window.pack()
    
    root2.mainloop()
def select_all():
    input_text.tag_add(SEL, "1.0", END)
    input_text.mark_set(INSERT, "1.0")
    input_text.see(INSERT)

def copy_f():
    root.clipboard_clear()
    text = input_text.get(SEL_FIRST, SEL_LAST)
    root.clipboard_append(text)

def cut():
    copy_f()
    input_text.insert(SEL_FIRST,SEL_LAST)

def paste_f():
    var = input_text.selection_get(selection='CLIPBOARD')
    input_text.insert('insert', var)
def delete_f():
    input_text.delete(SEL_FIRST,SEL_LAST)
    


#Define window
root = Tk()
root.title('Notepad')
root.iconbitmap('C:/Users/rafal/Desktop/WILK RAFAŁ/NAUKA/Programowanie/Python i GIT/THEArtOFDoing GUI apps/Exercises/pad.ico')
root.geometry('600x700')
root.resizable(0,0)


#Creating menu
#first column
menubar = Menu(root) #Creating Menu
filemenu = Menu(menubar, tearoff=0) #set place our manu
filemenu.add_command(label="New",command=open_new) #adding options
filemenu.add_command(label="Open",command=open_file)
filemenu.add_command(label="Save as",command=safe_our_main)
filemenu.add_command(label="Close",command=close)

filemenu.add_separator() #adding section in our filemenu
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu) #adding section in our menubar
#second column
editmenu = Menu(root)
editmenu = Menu(menubar,tearoff=0)
editmenu.add_command(label='Cut', command=cut)
editmenu.add_command(label='Copy', command=copy_f)
editmenu.add_command(label='Paste', command=paste_f)
editmenu.add_command(label='Delete', command=delete_f)
editmenu.add_command(label='Select All', command=select_all)

menubar.add_cascade(label='Edit', menu=editmenu)

#third column 
helpmenu = Menu(root)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label='Help Index', command=donothing)
helpmenu.add_command(label='About...',command=about_me)

var = BooleanVar()
helpmenu.add_checkbutton(label='Light/Dark mode',command=change_color,variable=var)


menubar.add_cascade(label='Help', menu=helpmenu)

#Configuration 
bg_colour = '#E6F14A'
root.config(bg='red',menu=menubar)

#Define frames
frame_1 = Frame(root,bg=bg_colour,width=100,height=100)
frame_1.pack(pady=5)

frame_2 = Frame(root,bg='red')
frame_2.pack(padx=5,pady=5,fill='y', expand=TRUE)

#Define buttons and images 
new_image = PhotoImage(file='C:/Users/rafal/Desktop/WILK RAFAŁ/NAUKA/Programowanie/Python i GIT/THEArtOFDoing GUI apps/Exercises/new.png')
new_button = Button(frame_1, image=new_image,command=open_new)
new_button.grid(row=0,column=0,padx=5)

open_image = PhotoImage(file='C:/Users/rafal/Desktop/WILK RAFAŁ/NAUKA/Programowanie/Python i GIT/THEArtOFDoing GUI apps/Exercises/open.png')
open_button = Button(frame_1,image=open_image,command=lambda:open_file())
open_button.grid(row=0,column=1,padx=5)

save_image = PhotoImage(file='C:/Users/rafal/Desktop/WILK RAFAŁ/NAUKA/Programowanie/Python i GIT/THEArtOFDoing GUI apps/Exercises/save.png')
save_button = Button(frame_1,image=save_image,command=safe_our_main)
save_button.grid(row=0,column=2,padx=5)

close_image = PhotoImage(file='C:/Users/rafal/Desktop/WILK RAFAŁ/NAUKA/Programowanie/Python i GIT/THEArtOFDoing GUI apps/Exercises/close.png')
close_button = Button(frame_1, image=close_image,command=close)
close_button.grid(row=0,column=3,padx=5)

#Define OptionMenu's and list to insert them as a value
font_types = ['Terminal', 'Modern', 'Script', 'Courier', 'Arial', 'Calibri', 'Cambria',
'Georgia', 'MS Gothic', 'SimSun', 'Tahoma', 'Times New Roman', 'Verdana', 'Wingdings']
type_1 = StringVar()
font_type = OptionMenu(frame_1, type_1, *font_types,command=change_font)
font_type.grid(row=0,column=4,padx=5)
type_1.set('Terminal')

font_sizes = [8, 10, 12, 14, 16, 20, 24, 32, 48, 64, 72, 96]
size_1 = IntVar()
font_size = OptionMenu(frame_1,size_1, *font_sizes,command=change_font)
font_size.grid(row=0,column=5,padx=5)
size_1.set(12)

font_modes = ['none', 'bold', 'italic']
mode_1 = StringVar()
font_mode = OptionMenu(frame_1,mode_1,*font_modes,command=change_font)
font_mode.grid(row=0,column=6,padx=5)
mode_1.set('none')



#Define scroll text
input_text = scrolledtext.ScrolledText(frame_2,width=1000,height=100)
input_text.pack()



#run root mainloop
root.mainloop()
print("Mischief Managed")
