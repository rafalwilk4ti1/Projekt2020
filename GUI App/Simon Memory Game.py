from tkinter import *
from random import randint
from tkinter import StringVar, ACTIVE, NORMAL, DISABLED

#Define window
root = Tk()
root.title('Simon Memory Game')
root.iconbitmap('C:/Users/rafal/Desktop/THEArtOFDoing GUI apps/Exercises/simon.ico')
root.geometry('400x410')
root.resizable(1,1)

#Root configuration
bg_color = '#15B162'
s_color = '#AEFFD8'
color_1 = '#046c27'
color_2 = '#0ef65b'
color_3 = '#c5c207'
color_4 = '#f8f53a'
color_5 = '#850505'
color_6 = '#f71d1d'
color_7 = '#054a94'
color_8 = '#3f98f8'
color_to_change = 'white'

font_root = ('SimSun', 12)
root.config(bg=bg_color)

time = 500
score = 0
game_sequences = []
player_sequence = []

#Define functions
def play_sequence():
    change_label("Playing!")
    delay = 0
    for value in game_sequences:
        if value == 1:
            root.after(delay,lambda : animation(red_button))
        elif value == 2:
            root.after(delay,lambda : animation(maroon_button))
        elif value == 3:
            root.after(delay,lambda : animation(yellow_button))        
        elif value == 4:
            root.after(delay,lambda : animation(olive_button))

        delay +=time
def press(value):
    player_sequence.append(value)
    if len(player_sequence) == len(game_sequences):
        check_round()

def check_round():
    #The player is correct, so change the label, update score, wait,
    #  then start  the next round.
    global player_sequence
    global game_sequences
    global score

    if player_sequence == game_sequences:
        change_label("Correct")
        score += len(player_sequence) + int(1000/time)
        root.after(500, play_game)
    else:
        change_label('Wrong!')
        score = 0
        disabled()
        game_sequences = []
        root.after(2000, lambda:change_label("New Game"))
    player_sequence = []

    label_1.config(text='Score' + str(score))


def animation(button):
    button.config(state=ACTIVE)
    root.after(time, lambda:button.config(state=NORMAL))

def level():
    global time
    if var.get() == 1:
        time = 1000
    elif var.get() == 2:
        time = 500
    elif var.get() == 3:
        time = 200

def play_game():
    while True:
        value = randint(1,4)
        if len(game_sequences) ==0:
            game_sequences.append(value)
            break
        elif value != game_sequences[-1]:
            game_sequences.append(value)
            break
    play_sequence()

def change_label(message):
    new_game.config(text=message)

    if message=='Wrong':
        new_game.config(bg='red')
    else:
        new_game.config(bg=bg_color)

def enabled():
    red_button.config(state=NORMAL)
    maroon_button.config(state=NORMAL)
    yellow_button.config(state=NORMAL)
    olive_button.config(state=NORMAL)

    play_game()

def disabled():
    red_button.config(state=DISABLED)
    maroon_button.config(state=DISABLED)
    yellow_button.config(state=DISABLED)
    olive_button.config(state=DISABLED)


#Define labels
label_1 = Label(root,bg=bg_color,text='Score:'+str(score)+'',anchor='e',font=font_root,height=5,padx=70)
label_1.pack(fill=X,expand=TRUE,pady=5)
label_2 = Label(root,bg=s_color,height=5)
label_2.pack(fill=X,expand=TRUE,padx=40)
label_3 = Label(root,text='Difficulty:',anchor="w",padx=20,bg=s_color)
label_3.pack(fill=BOTH,expand=TRUE,side=LEFT,padx=40, pady=(0,10))
#Define buttons
new_game = Button(label_1,text='New Game',font=font_root,command=enabled)
new_game.grid(sticky="W",padx=100,ipadx=30,ipady=1)

red_button = Button(label_2,bg=color_1,width=15,height=8,state=DISABLED,activebackground=color_2,command=lambda:press(1))
red_button.grid(row=0,column=0,padx=30,pady=15)
maroon_button = Button(label_2,bg=color_3,width=15,height=8,state=DISABLED,activebackground=color_4,command=lambda:press(2))
maroon_button.grid(row=0,column=1)
yellow_button = Button(label_2,bg=color_5,width=15,height=8,state=DISABLED,activebackground=color_6,command=lambda:press(3))
yellow_button.grid(row=1,column=0,padx=30,pady=15)
olive_button = Button(label_2,bg=color_7,width=15,height=8,state=DISABLED,activebackground=color_8,command=lambda:press(4))
olive_button.grid(row=1,column=1)

#Define Radio
var = IntVar()
easy_radio = Radiobutton(label_3,text='Easy',variable=var, value=1,bg=s_color,command=level).grid(row=0,column=0,padx=(100,10),pady=(1,10))
medium_radio = Radiobutton(label_3,text='Medium',variable=var, value=2,bg=s_color,command=level).grid(row=0,column=1,pady=(1,10))
hard_radio = Radiobutton(label_3,text='Hard',variable=var, value=3,bg=s_color,command=level).grid(row=0,column=2,pady=(1,10))


#run root mainloop
root.mainloop()
