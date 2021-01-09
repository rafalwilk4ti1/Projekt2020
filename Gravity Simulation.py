#Gravity Simulation
from tkinter import *
from tkinter import CURRENT
from matplotlib import pyplot

#Define a window
root = Tk()
root.title("Gravity Simulation")
root.iconbitmap('C:/Users/rafal/Desktop/THEArtOFDoing GUI apps/Exercises/earth.ico')
root.geometry('500x650')
root.resizable(1,1)

#Define global varuable 
time = 0
data = {}
for i in range(1,5):
    data['data_%d' % i] = []

#Define functions
def move(event):
    #Adding move to the ball, providing it's actuall BALL
    if "BALL" in main_canvas.gettags(CURRENT):
        x1 = main_canvas.coords(CURRENT)[0]
        x2 = main_canvas.coords(CURRENT)[2]
        
        #Set cordinates our ball by move our mouse
        main_canvas.coords(CURRENT, x1, event.y, x2, event.y-10) 
        
        #Block ball at the top of Canvas
        if main_canvas.coords(CURRENT)[3] < 15:
            main_canvas.coords(CURRENT, x1, 5, x2, 15)
        #Block ball at the bottom of Canvas
        elif main_canvas.coords(CURRENT)[3] >405:
            main_canvas.coords(CURRENT, x1 ,405 ,x2 ,415 )
        #Update our height value
        height_update()

def height_update():
    #Update height value
    for i in range(1,5):
        heights['height_%d' % i].config(text='Height: '+ str(round(415- (main_canvas.coords(balls['ball_%d' % i ])[3]),2)))
       

def step(t):
    #Negate a and v because canvas y value increase as you move down
    global time
    for i in range(1,5):
        #Do physics calculations and remember that our height starts from 0 to 415, but our balls start from 415
        a = -1 * float(acceleration['a_%d' % i].get())
        v =-1 * float(velocities['v_%d' % i ].get())
        d = v*t + .5*a*t**2
        #Download permanent values to set x1,x2 our balls
        x1 = main_canvas.coords(balls['ball_%d' % i])[0]
        x2 = main_canvas.coords(balls['ball_%d' % i])[2]
        #Moving our ball through the open space
        if main_canvas.coords(balls['ball_%d' % i ])[3] + d <415 :
            main_canvas.move(balls['ball_%d' % i],0,d)
            y2 = main_canvas.coords(balls['ball_%d' % i ])[3]
            main_canvas.create_line(x1,y2, x2,y2, tag="DASH")    
        #Block our ball at the end our Canvas
        else:
            main_canvas.coords(balls['ball_%d' % i ],x1, 405, x2, 415)
        #Second calculation
        vf = v + a*t
        #Update velocity values for each ball
        velocities['v_%d' % i ].delete(0,END)
        velocities['v_%d' % i ].insert(0,str(round(-1*vf, 2)))

        #Add data for the step to the data dict
        data['data_%d' % i].append((time,415-main_canvas.coords(balls['ball_%d' % i])[3]))
    
        #Update height
        height_update()

    #update time
    time += t

def run():
    #Run all balls without stopping, we carry about the final result
    step(t_slider.get())
    while 15 < main_canvas.coords(balls['ball_1'])[3] < 415 or 15 < main_canvas.coords(balls['ball_2'])[3] < 415 or 15 < main_canvas.coords(balls['ball_3'])[3] < 415 or 15 < main_canvas.coords(balls['ball_4'])[3] < 415:
        step(t_slider.get())

def reset():
    #Recover our open window
    #set position our balls
    x1 = 45
    x2 = 55
    for i in range(1,5):    
        main_canvas.coords(balls['ball_%d' % i ],x1, 405, x2, 415)
        x1 += 100
        x2 += 100
        #Recover velocities
        velocities['v_%d' % i].delete(0,END)
        velocities['v_%d' % i].insert(0,"0")
        #recover accelerations
        acceleration['a_%d' % i].delete(0,END)
        acceleration['a_%d' % i].insert(0,'0')
        #recover heights
        heights['height_%d' % i].config(text='Height: '+str(415 -  main_canvas.coords(balls['ball_%d' % i ])[3]))
        #delete dash
        delete_dash = main_canvas.gettags("DASH")
        main_canvas.delete(delete_dash)   

def graph():
    #Creating our graph distance v time for 4 balls
    # Creating list to storage the collors balls  
    global data  
    colors = ['red','cyan','blue','purple']
    for i in range(1,5):
        #Initilize x,y values
        x = []
        y = []
        print(i-1)
        for data_list in data['data_%d' % i]:
            x.append(data_list[0])
            y.append(data_list[1])
    
    
        pyplot.plot(x,y,color=colors[i-1])
    pyplot.title('Distance vs Time')
    pyplot.xlabel('Time')
    pyplot.ylabel('Distance')
    pyplot.show()






#Define frames
canvas_frame = Frame(root)
canvas_frame.pack(pady=10)
input_frame = Frame(root)
input_frame.pack(fill=BOTH,expand=True)

#Define canvas window
main_canvas = Canvas(canvas_frame,width=400,height=415,bg='white')
main_canvas.grid(padx=5,pady=5,column=0,row=0)

#Creating lines
line_1 = main_canvas.create_line(2,415,2,0)
line_2 = main_canvas.create_line(100,415,100,0)
line_3 = main_canvas.create_line(200,415,200,0)
line_4 = main_canvas.create_line(300,415,300,0)
line_5 = main_canvas.create_line(400,415,400,0)

#Creating balls
balls = {}
balls['ball_1'] = main_canvas.create_oval(45,405,55,415,fill='red',tag="BALL")
balls['ball_2'] = main_canvas.create_oval(145,405,155,415,fill='cyan',tag="BALL")
balls['ball_3'] = main_canvas.create_oval(245,405,255,415,fill='blue',tag="BALL")
balls['ball_4'] = main_canvas.create_oval(345,405,355,415,fill='purple',tag="BALL")

#Creating d,vi,a,t
d_label = Label(input_frame,text='d').grid(row=0,column=0)
vi_label = Label(input_frame,text='vi').grid(row=1,column=0)
a_label = Label(input_frame,text='a').grid(row=2,column=0,ipadx=15)
t_label = Label(input_frame,text='t').grid(row=3,column=0)

#Creating heights/distance labels
heights = {}
for i in range(1,5):
    heights['height_%d' % i] = Label(input_frame,text='Height: '+str(415 -  main_canvas.coords(balls['ball_%d' % i ])[3]))
    heights['height_%d' % i].grid(row=0,column=i)

velocities = {}
for i in range(1,5):
    velocities['v_%d' % i] = Entry(input_frame,width=15)
    velocities['v_%d' % i].grid(row=1,column=i,padx=5)
    velocities['v_%d' % i].insert(0,'0')

acceleration = {}
for i in range(1,5):
    acceleration['a_%d' % i] = Entry(input_frame,width=15)
    acceleration['a_%d' % i].grid(row=2,column=i,padx=5)
    acceleration['a_%d' % i].insert(0,'0')

#Time slider
t_slider = Scale(input_frame,from_=0,to_=1,tickinterval=.1,resolution=.01,orient=HORIZONTAL)
t_slider.grid(row=3,column=1,columnspan=4,sticky='WE',pady=5,padx=10)
t_slider.set(1)

#Define buttoms
step_button = Button(input_frame,text='Step',command=lambda:step(t_slider.get()))
run_button = Button(input_frame,text='Run',command=run)
graph_button = Button(input_frame,text='Graph',command=graph)
reset_button = Button(input_frame,text='Reset',command=reset)
quit_button = Button(input_frame,text='Quit',command=root.destroy)

step_button.grid(row=4,column=1,sticky='WE',padx=(0,2))
run_button.grid(row=4,column=2,sticky='WE',padx=2)
graph_button.grid(row=4,column=3,sticky='WE',padx=2)
reset_button.grid(row=4,column=4,sticky='WE',padx=(2,0))
quit_button.grid(row=5,column=1,columnspan=4,sticky='WE')


#download cords from the button is clicked
root.bind("<B1-Motion>",move)

#run root's mainloop
root.mainloop()