from tkinter import *
from PIL import ImageTk
from PIL import Image
import winsound





#Define window
root = Tk()
root.title('Morse Code Translator')
root.iconbitmap('C:/Users/rafal/Desktop/WILK RAFAŁ/NAUKA/Programowanie/Python i GIT/THEArtOFDoing GUI apps/Exercises/morse.ico')
root.geometry('500x350')
root.resizable(1,1)

#Configuration root 
font_root = ('SimSun', 10)
bg_root = "#778899"
color_frame ='#dcdcdc'
button_color = '#c0c0c0'
text_color = '#f8f8ff'



root.config(bg=bg_root)



#Define functions
def second_window():
    #Define window
    root2 = Toplevel()
    root2.title('Morse Guide')
    root2.iconbitmap('C:/Users/rafal/Desktop/WILK RAFAŁ/NAUKA/Programowanie/Python i GIT/THEArtOFDoing GUI apps/Exercises/morse.ico')
    root2.geometry('350x350+'+ str(root.winfo_x()+500) + "+" + str(root.winfo_y()))
    root2.resizable(0,0)
    #Configuration root2
    root2.config(bg=bg_root)
    # #create frame
    # frame_1 = Frame(root2)
    # frame_1.pack(fill=BOTH,expand=TRUE,padx=5,pady=10)
    path ='C:/Users/rafal/Desktop/WILK RAFAŁ/NAUKA/Programowanie/Python i GIT/THEArtOFDoing GUI apps/Exercises/morse_chart.jpg'
    image_board = ImageTk.PhotoImage(Image.open(path))
    image_1 = Label(root2, image=image_board)
    image_1.pack(pady=10,ipadx=5,ipady=5)
    button_close = Button(root2,text='Close',font=font_root,bg=button_color,command=root2.destroy)
    button_close.pack(pady=3,ipadx=60,ipady=30)
    #run root2's mainloop
    root2.mainloop()

def clear_f():
    #clear first and second window
    first_text.delete('1.0',END)
    second_text.delete('1.0',END) 

def convert():
    #function responsible for converting
    if number.get()==1:
        english_to_morse_f()
    elif number.get() == 2:
        morse_to_english_f()

def english_to_morse_f():
    #transalete english to morse
    text1 = first_text.get('0.0',END)
    for x in text1:
        new = str(english_to_morse[str(x)])
        second_text.insert(END,(str(new)+"  "))

def morse_to_english_f():
    #transalete morse to english 
    text1 = first_text.get('0.0',END)
    text2 = text1.split()
    for x in range(len(text2)):
        if text2[x] in morse_to_english.keys():
            new = morse_to_english[str(text2[x])]
            second_text.insert(END,str(new))

def play_morse():
    #set a location where the morse code is 
    if number.get() == 1:
        text = str(second_text.get('0.0',END))
    elif number.get() == 2:
        text = str(first_text.get('0.0',END))

    #making a sound depending what the significant is
    for x in text:
        if x == ".":
            winsound.Beep(1000, 100)
            root.after(100)
        elif x == "-":
            winsound.Beep(2000, 400)
            root.after(200)
        elif x == " ":
            root.after(300)
        elif x == '|':
            root.after(700)
        
#-.-  .-  .-..  ---  .--.  
   

#Define dictonaries
english_to_morse = {
    'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..',
    'e': '.', 'f': '..-.', 'g': '--.', 'h': '....',
    'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..',
    'm': '--', 'n': '-.', 'o': '---', 'p': '.--.',
    'q': '--.-', 'r': '.-.', 's': '...', 't': '-',
    'u': '..--', 'v': '...-', 'w': '.--', 'x': '-..-',
    'y': '-.--', 'z': '--..', '1': '.----',
    '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '0': '-----', ' ':' ', '|':'|', "":"" }

morse_to_english = dict((value,key) for key,value in english_to_morse.items() )

#Define frames
input_frame = LabelFrame(root)
output_frame = LabelFrame(root)
input_frame.pack(padx=16,pady=(16,8),fill=BOTH,expand=TRUE)
output_frame.pack(padx=16,pady=(8,16),fill=BOTH,expand=TRUE)

#Define buttons
guide_button = Button(input_frame,text="Morse Guide",font=font_root,bg=button_color,command=second_window)
convert_button = Button(output_frame,text='Covnert',font=font_root,bg=button_color,width=22,command=convert)
play_button = Button(output_frame,text='Play Morse',font=font_root,bg=button_color,command=play_morse)
clear_button = Button(output_frame,text='Clear',font=font_root,bg=button_color,command=clear_f)
quit_button = Button(output_frame,text='Quit',font=font_root,bg=button_color,command=quit)

guide_button.grid(row=2,column=0,sticky="WE",padx=5)
convert_button.grid(row=0,column=0,padx=5)
play_button.grid(row=1,column=0,sticky="WE",padx=5)
clear_button.grid(row=2,column=0,sticky="WE",padx=5)
quit_button.grid(row=3,column=0,sticky="WE",padx=5)

#Define variable INT
number = IntVar()

#Define radiobuttons
radio_1 = Radiobutton(input_frame,text='English ---> Morse Code ',variable=number,value=1)
radio_2 = Radiobutton(input_frame,text='Morse Code ---> English ',variable=number,value=2)
radio_1.grid(row=0,column=0,padx=5)
radio_2.grid(row=1,column=0,padx=5)

#Define text window
first_text = Text(input_frame,height=8,width=30)
second_text = Text(output_frame,height=8,width=30)
first_text.grid(rowspan=3,column=1,padx=1,pady=5,row=0,ipadx=20)
second_text.grid(rowspan=4,column=1,padx=1,pady=5,row=0,ipadx=20)


#Run root's mainloop
root.mainloop()
