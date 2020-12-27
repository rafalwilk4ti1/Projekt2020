from tkinter import *
from tkinter import Scale, filedialog
import colorsys

#Define a window
root = Tk()
root.title("Color Theme Maker")
root.iconbitmap('C:/Users/rafal/Desktop/WILK RAFAŁ/NAUKA/Programowanie/Python i GIT/THEArtOFDoing GUI apps/Exercises/color_wheel.ico')
root.geometry('500x600')
root.resizable(0,0)

#Define functions

#converting colors
def _from_rgb(rgb):
    r,g,b = rgb
    return f'#{r:02x}{g:02x}{b:02x}'
#converting colors
def rgb_to_hex(rgb):
    return '%02x%02x%02x' % (rgb)

#saving our colors to file
def save():
    name_file = filedialog.asksaveasfilename()
    with open(name_file,'w') as f1:
        f1.write("Your color from Color Theme Maker:\n\n")
        for x,y in stored_colors.items():
            f1.write(str(x)+str(y)+'\n\n')
             
    
    
#we use the same function provide required value
def recall_function(y):
    store(y)


#Making function to set colors 
def set_colors(r,g,b):
    red_slider.set(r)
    green_slider.set(g)
    blue_slider.set(b)
    square_box2.config(bg=_from_rgb((r,g,b)))
    color_tuple.config(text= "("+str(r)+"),"+"("+str(g)+"),"+"("+str(b)+")" )
    var = rgb_to_hex((r,g,b))
    x = var.replace('a','f') 
    color_hex.config(text="#"+str(x))
#Downloading values from sliders
def sliders(*args):
    global red,green,blue
    red = red_slider.get()
    green = green_slider.get()
    blue = blue_slider.get()
    print(red,green,blue)
    set_colors(red,green,blue)



#Store function to store our colors in second frame
def store(y):
    # radio = Radiobutton(outtput_frame,variable=stored_color, value=x)
    # radio.grid(row=x,column=0,sticky='W')
    r = red_slider.get()
    g = green_slider.get()
    b = blue_slider.get()
   
   
    rgb_colors = _from_rgb((r,g,b))
    var = rgb_to_hex((r,g,b))
    x = var.replace('a','f') 
    bg_color = "#"+x
    r = str(r)
    g = str(g)
    b = str(b)
    #mini operation to make sure that our "the new window" cover the old one
    if len(r) <3:
        r = "0" + r
        if len(r) <3:
            r="0"+r

    if  len(g) <3: 
        g = "0" + g
        if len(g) < 3:
            g = "0"+g

    if len(b) <3:
        b = "0" + b
        if len(b) <3:
            b = "0" + b
    print(r,g,b)
 #creating a "cover" for old widgets
    recall_button2 = Button(outtput_frame,text='Recall Color',command=lambda: recall_function(y),state=ACTIVE)
    new_rgb_label = Label(outtput_frame,text="("+str(r)+")"+"("+str(g)+")"+"("+str(b)+")")
    new_hex_label = Label(outtput_frame,text="#"+str(x))
    new_black_square = Label(outtput_frame,width=3,height=1,bg='black')
    new_white_box = Label(outtput_frame,bg=bg_color,width=3,height=1)
    
    recall_button2.grid(row=y,column=1,padx=(10,30))
    new_rgb_label.grid(row=y,column=2,padx=20,ipadx=5)
    new_hex_label.grid(row=y,column=3,padx=20,ipadx=5)
    new_black_square.grid(row=y,column=4,padx=20,pady=2,ipadx=5,ipady=5)
    new_white_box.grid(row=y, column=4)
    stored_colors[y] = (new_rgb_label.cget('text'),new_hex_label.cget('text'))

#Define frames
input_frame = LabelFrame(root,padx=5)
outtput_frame = LabelFrame(root,padx=5)
input_frame.pack(fill=BOTH, expand=True,padx=5,pady=5)
outtput_frame.pack(fill=BOTH,expand=True,padx=5,pady=5)

red_label = Label(input_frame,text='R')
red_slider = Scale(input_frame, from_=0, to=255,command=sliders)
red_button = Button(input_frame,text='Red',command=lambda: set_colors(255,0,0)) 

green_label = Label(input_frame,text='G')
green_slider = Scale(input_frame, from_=0, to=255,command=sliders)
green_button = Button(input_frame,text='Green',command=lambda: set_colors(0,128,0)) 

blue_label = Label(input_frame,text='B')
blue_slider = Scale(input_frame, from_=0, to=255,command=sliders)
blue_button = Button(input_frame,text='Blue',command=lambda: set_colors(0,0,255)) 

#Create Buttons for each cimplimentary color 
yellow_button = Button(input_frame,text='Yellow',command=lambda: set_colors(255,255,0))
cyan_button = Button(input_frame,text='Cyan',command=lambda: set_colors(0,255,255))
magenta_button = Button(input_frame,text='Magenta',command=lambda: set_colors(255,0,255))


#Create utility Buttons
store_button = Button(input_frame, text='Store Color' , command=lambda:store(stored_color.get()))
save_button = Button(input_frame,text='Save',command=save)
quit_button = Button(input_frame,text='Quit',command=root.destroy)
#Put labels, and buttons on to the frame,.... Use ipadx with rgb buttons to define column width, the use sticky on others
red_label.grid(row=0,column=0,padx=(0,40))
red_slider.grid(row=1,column=0,padx=5)
red_button.grid(row=2,column=0,ipadx=20,padx=(15,0))

green_label.grid(row=0,column=1,padx=(0,40))
green_slider.grid(row=1,column=1,padx=5,pady=20)
green_button.grid(row=2,column=1,ipadx=20)

blue_label.grid(row=0,column=2,padx=(0,40))
blue_slider.grid(row=1,column=2,padx=5)
blue_button.grid(row=2,column=2,ipadx=20)

yellow_button.grid(row=3,column=0,sticky='EW',padx=(15,0))
cyan_button.grid(row=3,column=1,sticky='EW')
magenta_button.grid(row=3,column=2,sticky='EW')

store_button.grid(row=4,column=0,columnspan=3,sticky='EW',padx=(15,0))
save_button.grid(row=4,column=3,sticky='WE')
quit_button.grid(row=4,column=4,sticky='WE')

#Create the colox box and labels on the frame
square_box = Label(input_frame,background='black',width=20,height=10)
square_box2 = Label(input_frame,background='white',width=20,height=10)
color_tuple = Label(input_frame,text='(0),(0),(0)')
color_hex = Label(input_frame,text='#000000')

#put the colox and labels on the frame
square_box.grid(row=1,column=3,columnspan=2,padx=35,pady=10,ipadx=10,ipady=10)
square_box2.grid(row=1,column=3,columnspan=2)
color_tuple.grid(row=2,column=3,columnspan=2)
color_hex.grid(row=3,column=3,columnspan=2)

#Setting up the output frame
stored_colors = {}
stored_color = IntVar()

#Creating checkbuttons, buttons, rgb colors, hex colors, little square
for x in range(6):
    radio = Radiobutton(outtput_frame,variable=stored_color, value=x)
    radio.grid(row=x,column=0,sticky='W')

    recall_button = Button(outtput_frame,text='Recall Color',state=DISABLED)
    rgb_label = Label(outtput_frame,text='(255),(255),(255)')
    hex_label = Label(outtput_frame,text='#ffffff')
    black_square = Label(outtput_frame,width=3,height=1,bg='black')
    white_box = Label(outtput_frame,bg='white',width=3,height=1)

    recall_button.grid(row=x,column=1,padx=(10,30))
    rgb_label.grid(row=x,column=2,padx=30)
    hex_label.grid(row=x,column=3,padx=30)
    black_square.grid(row=x,column=4,padx=30,pady=2,ipadx=5,ipady=5)
    white_box.grid(row=x, column=4)

#.cget returns the value of a specific option, store the text value of the tubple label and hex label
stored_colors[stored_color.get()] = [rgb_label.cget('text'),hex_label.cget('text')]

#Run root's mainloop
root.mainloop()