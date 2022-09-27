#downloading necessary packages
import time
from types import SimpleNamespace as simplify
from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont
from PIL import Image
from PIL import ImageTk as itk

root = Tk()  #initiating the graphics program (tkinter)

###################### SETTINGS (EDIT HERE) ############################
imgs = {
    'frame': Image.open('frame.png'),
    'ready_button': Image.open('ready_button.png')
}

questions = {
    1: {
        'question': "Who was the first president",
        1: 'test',
        2: 'test',
        'answer': 1,
    }
}
# "Who is the current president ",
# "Who was the oldest living president",
# "Which president had the longest campaign",
# "Which class are presidents most relevant in",
# "Why did Abraham Lincoln not support slavery",
# "Which Easterner out of this list came to America first",
# "Who travels",
# "Who is the current vice president of america",
# "Whomost closely rules the world",
#}

######## DO NOT EDIT! from here on, unless you know what you are doing
#making machine readable images
imgs = simplify(**imgs)
imgs = {
    'frame': itk.PhotoImage(imgs.frame),
    'ready_button': itk.PhotoImage(imgs.ready_button)
}
imgs = simplify(**imgs)

#settings width, height of application
width = imgs.frame.width()  #of application
height = imgs.frame.height()  #of application

######## DO NOT EDIT! from here on, unless you know what you are doing
#initiating the application
root.geometry(str(width) + 'x' + str(height))
root.overrideredirect(1)


#IMPORTANT FUNCTIONS
def update_buttons():
    global last_refresh
    global new_refresh
    delta_time = new_refresh - last_refresh
    print(imgs.frame.cget('file'))


def ready_clicked(event):
    global new_size
    print('clicked', event)
    new_size = Image.open('ready_button.png')
    new_size = itk.PhotoImage(
        new_size.resize(
            (imgs.ready_button.width() - 20, imgs.ready_button.height() - 20)))
    # ready_button = c.create_image(
    #     width / 2,
    #     height - imgs.ready_button.height(),
    #     image=itk.PhotoImage(newt_size),
    # )
    # c.tag_bind(ready_button, "<Button-1>", ready_clicked)
    c.itemconfig(ready_button, image=new_size)
    #ready_button.pack()


def exit_click():
    root.quit


def move_app(e):
    root.geometry(f'+{e.x_root}+{e.y_root}')


#making the canvas
c = Canvas(root,
           width=width,
           height=height,
           background='black',
           highlightthickness=0)

c.create_image(0, 0, image=imgs.frame, anchor='nw')
c.create_text((width / 2),
              125,
              text="RESIZE YOUR SCREEN\npress ready",
              font=('Arial', 25, 'bold'),
              fill="white",
              justify='center')  #, anchor='nw')
ready_button = c.create_image(
    width / 2,
    height - imgs.ready_button.height(),
    image=imgs.ready_button,
)
c.tag_bind(ready_button, "<Button-1>", ready_clicked)
c.pack()  #canvas ready

#updating everything per refresh rate (THIS SHOULD BE THE END OF THE PROGRAM)
last_refresh = time.time()
while True:
    new_refresh = time.time()
    update_buttons()
    #print(new_refresh - last_refresh)
    last_refresh = new_refresh

    root.update_idletasks()
    root.update()

#root.mainloop()
