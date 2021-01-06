#APOD Photo Viewer
from tkinter import *
from tkcalendar import DateEntry
import requests
from PIL import ImageTk, Image 
from io import BytesIO
import webbrowser
from tkinter import filedialog

#Define a window
root = Tk()
root.title('APOD Photo Viewer')
root.iconbitmap('C:/Users/rafal/Desktop/THEArtOFDoing GUI apps/Exercises/rocket.ico')

#Define functions 
# xl68sQNnhwLF9xrgADJkoMDemKaVhB6gP7RmhzCM
# url adres = https://api.nasa.gov/planetary/apod?api_key=xl68sQNnhwLF9xrgADJkoMDemKaVhB6gP7RmhzCM

def get_request():
    global response
    url = 'https://api.nasa.gov/planetary/apod'
    api_key = 'xl68sQNnhwLF9xrgADJkoMDemKaVhB6gP7RmhzCM'
    date = calendar_1.get_date()
    
    querystring = {'api_key':api_key,'date':date}

    response = requests.request("GET", url, params=querystring)
    response = response.json()
    #print(response)
    set_data()


def set_data():
    """{'code': 400, 'msg': 'Date must be between Jun 16, 1995 and Jan 05, 2021.', 'service_version': 'v1'}
{'date': '2020-09-15', 'explanation': "Could there be life floating in the atmosphere of Venus? Although Earth's planetary neighbor has a surface
 considered too extreme for any known lifeform, Venus' upper atmosphere may be sufficiently mild for tiny airborne microbes. 
 This usually disfavored prospect took an unexpected upturn yesterday with the announcement of the discovery of Venusian phosphine. 
 The chemical phosphine (PH3) is a considered a biomarker because it seems so hard to create from routine chemical processes thought to occur
  on or around a rocky world such as Venus -- but it is known to be created by microbial life on Earth.  The featured image of Venus and its thick clouds was 
  taken in two bands of ultraviolet light by the Venus-orbing Akatsuki, a Japanese robotic satellite that has been orbiting the cloud-shrouded world since 2015.  
  The phosphine finding, if confirmed, may set off renewed interest in searching for other indications of life floating high in the atmosphere of our Solar
   System's second planet out from the Sun.   Experts Debate: How will humanity first discover extraterrestrial life?",
    'hdurl': 'https://apod.nasa.gov/apod/image/2009/VenusClouds_Akatzuki_960.jpg', 'media_type': 'image', 'service_version': 'v1', 
    'title': 'Biomarker Phosphine Discovered in the Atmosphere of Venus', 'url': 'https://apod.nasa.gov/apod/image/2009/VenusClouds_Akatzuki_960.jpg'}"""
    text_1 = response['explanation']
    label_o0.config(text=text_1)
    date_str = response['date']
    label_o2.config(text=date_str)
    title = response['title']
    root.title(title)
    get_photo()

def get_photo():
    global img
    global full_img
    global thumb

    #Put info is it a video or an image to var
    var = response['media_type']
    print(var)
    if var=="image":
        #get url adres to display in our app or to move us on youtube
        url = response['url']
        #getting answer is it everything correct
        photo_request = requests.get(url,stream=True)
        #turn into compatible with python/tkinter
        data_picture = photo_request.content
        full_img = Image.open(BytesIO(data_picture))
        
        thumb_data = photo_request.content
        thumb = Image.open(BytesIO(thumb_data))
        thumb.thumbnail((200,300))
        thumb = ImageTk.PhotoImage(thumb)
        label_o1.config(image=thumb)
    
    elif var=='video':
        #getting url
        url = response['url']
        #set url to label as a source link
        label_o1.config(text=url)
        #waiting for readerers
        root.after(5000)
        #opening our link
        webbrowser.open_new(url)
    
    label_o1.config(text=url)
def full_photo():
    #global img
    root2 = Toplevel()
    root2.title('Full picture to download')
    root2.iconbitmap('C:/Users/rafal/Desktop/THEArtOFDoing GUI apps/Exercises/rocket.ico')
    #root2.geometry("1920x1080")
    # photo = response['url']
    # photo_request = requests.get(photo,stream=True)
    # data_picture = photo_request.content
    img = ImageTk.PhotoImage(full_img)
    size_img = "%dx%d" % (img.width(), img.height())
    print(size_img)
    label_photo = Label(root2,image=img)
    label_photo.place(x=0, y=0, relwidth=1, relheight=1)
    root2.geometry(size_img)
    root2.mainloop()

def save_photo():
     
    safe_method = filedialog.asksaveasfilename(initialdir="./", title='Save Image', filetypes=(('JPEG','*.jpg'),('All Files', '*.*')))
    full_img.save(safe_method + ".jpg")

#Define Structure and configuration
bg_color = '#1cfeba'
color_font = '#e8d33f'
color_output = '#95f2d9' 
background = '#41463D'
nasa_blue = '#043c93'
light_blue = '#7aa5d3'
nasa_red = '#ff1923'
nasa_white = '#ffffff'
font = ('Cambria', 12)

root.config(bg='black')


#Defeine LabelFrame 

frame1 = Frame(root,bg='black',padx=10)
frame2 = Frame(root,bg=background,width=50,height=20)
frame1.pack()
frame2.pack(pady=10)


#Define a list to chooose data and creating callendar 
calendar_1 = DateEntry(frame1,width=10,font=font,background=background,foreground='gold',	
activebackground='#6dc74d',relief=GROOVE,)
calendar_1.grid(row=0,column=0)


#Define Buttoms 
submit_button = Button(frame1,bg=background,text='Submit',font=font,fg='gold',	
activebackground='#6dc74d',relief=GROOVE,command=get_request)
full_photo_button = Button(frame1,bg=background,text='Full Photo', font=font,fg='gold',	
activebackground='#6dc74d',relief=GROOVE,command=full_photo)
save_button = Button(frame1,bg=background,text='Save Picture', font=font,fg='gold',	
activebackground='#6dc74d',relief=GROOVE,command=save_photo)
exit_button = Button(frame1,text='EXIT',bg=background,font=font,command=root.destroy,fg='gold',	
activebackground='#6dc74d',relief=GROOVE)

submit_button.grid(row=0,column=1,padx=5,ipadx=20,pady=10)
full_photo_button.grid(row=0,column=2,padx=5,ipadx=20)
save_button.grid(row=0,column=3,padx=5,ipadx=20)
exit_button.grid(row=0,column=4,padx=(5,20),ipadx=20)

#Define 3-frames in output frame 
label_o0 = Label(frame2,font=font,bg='black',wraplength=600,justify=CENTER,fg='gold',relief=GROOVE,bd=3)
label_o1 = Label(frame2,font=font,bg='black',fg='gold',relief=GROOVE,bd=3,highlightcolor='gold')
label_o2 = Label(frame2,font=font,bg='black',fg='gold',relief=GROOVE,bd=3)
label_o0.grid(row=0,rowspan=2,column=0,columnspan=4,padx=10,pady=10)
label_o1.grid(row=0,column=4,padx=10,pady=10)
label_o2.grid(row=1,column=4,padx=10,pady=10)



#Run our interface and functions 
get_request()

#Run root's mainloop
root.mainloop()