from tkinter import *
from tkinter import font

#Define functions 
def add_item():
    adding = str(first_entry.get())
    list_box.insert(END,(" * "+adding))
    first_entry.delete(0,END)

def clean_list():
    list_box.delete(0, 1000000)


def remover():
    list_box.delete(ANCHOR)

def saver_list():
    with open('checklist.txt', 'w') as f:
        list_tuple = list_box.get(0, END)
        for x in list_tuple:
            if x.endswith('\n'):
                f.write(x)
                
            else:
                f.write(x+'\n')




def opener():
    try:
        with open('checklist.txt', 'r') as f:
            for line in f:
                list_box.insert(END,line)

    except:
        return
    

def quiting():
    root.quit()

#Define windows
root = Tk()
root.title('Simple Checklist')
root.iconbitmap('C:/Users/rafal/Desktop/WILK RAFAŁ/NAUKA/Programowanie/Python i GIT/THEArtOFDoing GUI apps/Exercises/check.ico')
root.geometry('400x400')
root.resizable(1,1)

bg_color = '#89AAE6'
font_color = 'black'
font_style = font.Font(family='Helvetica', weight='bold',size=15)
root.config(bg=bg_color)



#Define labels
label_1 = Label(root,bg=bg_color,)
label_1.grid(row=0,column=0)

label_2 = Label(root,bg=bg_color)
label_2.grid(row=1,column=0)


label_3 = Label(root,bg=bg_color)
label_3.grid(row=2,column=0)


#Define entries

first_entry = Entry(label_1, width=50,borderwidth=3)
first_entry.grid(row=0, column=0,padx=10,pady=5)

#define listbox and scrollbard
scroll_bar = Scrollbar(label_2)
list_box = Listbox(label_2,width=32, height=12, font=font_style,borderwidth=2, yscrollcommand=scroll_bar.set )
list_box.grid(row=1,column=0)
scroll_bar.grid(row=1,column=1,sticky='NS')
scroll_bar.config(command=list_box.yview)

#first_entry = StringVar
#first_text = StringVar
#xscrollcommand
#---------------------------
#If you expect that users will often enter more text than the onscreen 
#size of the widget, you can link your entry widget to a scrollbar.


#Define buttoms

add_items = Button(label_1,text='Add Items',borderwidth=3,command=add_item)
add_items.grid(row=0,column=1,pady=5)


remove_items = Button(label_3,text='Remove Items',borderwidth=3,width=11,command=remover)
clear_list = Button(label_3,text='Clear List',borderwidth=3,width=11,command=clean_list)
save_list = Button(label_3,text='Save list',borderwidth=3,width=11,command=saver_list)
quit_option =Button(label_3,text='Quit',borderwidth=3,width=11,command=quiting)

remove_items.grid(row=0, column=0,ipadx=2,ipady=2,padx=3)
clear_list.grid(row=0, column=1,ipadx=2,ipady=2,padx=3)
save_list.grid(row=0, column=2,ipadx=2,ipady=2,padx=3)
quit_option.grid(row=0, column=3,ipadx=2,ipady=2,padx=3)








#open the previous list if available
opener()


#run root mainloop
root.mainloop()