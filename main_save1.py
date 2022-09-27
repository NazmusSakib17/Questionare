# #ARCHIVED VERSION OF main.py








# import time
# from types import SimpleNamespace as simplify
# from tkinter import *
# from tkinter import ttk
# import tkinter.font as tkFont

# root = Tk()

# imgs = {
#     'frame': PhotoImage(file='frame.png'),
#     'ready_button': PhotoImage(file='ready_button.png')
# }
# imgs = simplify(**imgs)

# width = imgs.frame.width()  #of application
# height = imgs.frame.height()  #of application

# root.geometry(str(width) + 'x' + str(height))
# root.overrideredirect(1)
# #root.wm_attributes("-transparentcolor", "grey")

# # root.call("wm", "attributes", ".", "-topmost",
# #           "true")  # Remove shadow from window
# # root.call("wm", "attributes", ".", "-fullscreen", "true")  # Fullscreen mode
# # root.call("wm", "attributes", ".", "-alpha", "0.5")  # Window Opacity 0.0-1.0


# def exit_click():
#     root.quit


# def move_app(e):
#     root.geometry(f'+{e.x_root}+{e.y_root}')


# #photo side bar

# # frame_label = Label(root, border=0, bg='black', image=imgs.frame)
# # frame_label.pack(fill=BOTH, expand=True)
# c = Canvas(root,
#            width=width,
#            height=height,
#            background='black',
#            highlightthickness=0)

# c.create_image(0, 0, image=imgs.frame, anchor='nw')
# c.create_text((width / 2),
#               125,
#               text="RESIZE YOUR SCREEN\npress ready",
#               font=('Arial', 25, 'bold'),
#               fill="white",
#               justify='center')  #, anchor='nw')
# ready_button = c.create_image(width / 2,
#                               height - imgs.ready_button.height(),
#                               image=imgs.ready_button)

# c.pack()
# # ttk.Label(frame_label, text="Hello World!").grid(column=0, row=0)
# #frame photo bind
# #frame_label.bind("<B1-Motion>", move_app)

# #exit button photo
# #exit_photo = PhotoImage(file='exit.png')

# #exit label
# #exit_label = Label(root,image=exit_photo,border=0,bg='#332D2D')
# #exit_label.place(x=590,y=9)

# #exit bind
# #exit_label.bind("<Button>",lambda e:exit_click())
# last_refresh = time.time()
# while True:
#     new_refresh = time.time()
#     print(new_refresh - last_refresh)
#     last_refresh = new_refresh
#     root.update_idletasks()
#     root.update()
# root.mainloop()

# #import os
# #os.environ["SDL_VIDEODRIVER"] = "dummy"

# # import pygame
# # import tkinter as tk
# # from tkinter import ttk
# # import tkinter as tk
# # import tkinter.font as font

# # class RoundedButton(tk.Canvas):
# #     def __init__(self, parent, border_radius, padding,
# #                  color, text = "", command = None):

# #         tk.Canvas.__init__(self, parent, borderwidth = 0, relief = "flat",
# #                            highlightthickness = 0, bg = parent["bg"])

# #         self.color = color
# #         self.command = command
# #         self.id = None

# #         font_size = 16
# #         height = font_size + (2 * padding)
# #         width = self.font.measure(text) + (4 * padding)
# #         width = width if width >= 80 else 80

# #         self.font = font.Font(size = font_size, family = "Helvetica",
# #                               weight = "bold")

# #         if (
# #             border_radius > 0.5 * width
# #             or border_radius > 0.5 * height
# #         ):
# #             raise ValueError("Error: total border_radius must not "
# #                              "exceed width or height.")

# #         self.id = self._shape(border_radius)

# #         x0, y0, x1, y1 = self.bbox("all")
# #         self.width = (x1 - x0)
# #         self.height = (y1 - y0)

# #         self.configure(width = self.width, height = self.height)
# #         self.create_text(self.width / 2, self.height / 2,text = text,
# #                          fill = 'white', font =  self.font)

# #         self.bind("<ButtonPress-1>", self._on_press)
# #         self.bind("<ButtonRelease-1>", self._on_release)

# #     def _on_press(self, event):
# #         self.configure(relief = "sunken")

# #     def _on_release(self, event):
# #         self.configure(relief = "raised")
# #         if self.command is not None:
# #             self.command()

# #     def _shape(self, border_radius):
# #             radius = 2 * border_radius
# #             self.create_arc((0, radius, radius, 0),
# #                             start = 90, extent = 90,
# #                             fill = self.color, outline = self.color)

# #             self.create_arc((self.width - radius, 0, self.width,
# #                              radius), start = 0, extent = 90,
# #                              fill = self.color, outline = self.color)

# #             self.create_arc((self.width, self.height - radius,
# #                              self.width - radius, self.height),
# #                              start = 270, extent = 90, fill = self.color,
# #                              outline = self.color)

# #             self.create_arc((0, self.height - radius, radius, self.height),
# #                             start = 180, extent = 90, fill = self.color,
# #                             outline = self.color)

# #             return self.create_polygon(
# #                 (
# #                     0, self.height - border_radius,
# #                     0, border_radius, border_radius,
# #                     0, self.width - border_radius, 0,
# #                     self.width, border_radius, self.width,
# #                     self.height - border_radius,
# #                     self.width - border_radius,
# #                     self.height, border_radius,
# #                     self.height
# #                 ),
# #                 fill = self.color,
# #                 outline = self.color)
# # from resources import questions
# # questions = questions()
# # #questions.new('test')
# # import sys
# # #from PIL import Image, ImageDraw

# # root=tk.Tk()
# # root.title('Questionare')
# # mainframe = ttk.Frame(root, padding="3 3 12 12")
# # mainframe.grid(column=0, row=0, sticky=('N', 'W', 'E', 'S'))
# # root.columnconfigure(0, weight=1)
# # root.rowconfigure(0, weight=1)

# # feet = "tests"
# # feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
# # feet_entry.grid(column=2, row=1, sticky=('W', 'E'))

# # meters = "tes"
# # ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=('W', 'E'))

# # ttk.Button(mainframe, text="Calculate", command='calculate').grid(column=3, row=3, sticky="W")
# # test = RoundedButton(mainframe,50,padding = '3 3 12 12',)
# # ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky="W")
# # ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky="W")
# # root.mainloop()
# # pygame.init()
# # pygame.font.init()
# # print([1,2,4])
# # screen = pygame.display.set_mode((640, 480))
# # questions = {
# #     1: {
# #         'question': "Who was the first president",
# #         1: 'test',
# #         2: 'test',
# #         'answer': 1,
# #     }
# # }

# # # "Who is the current president ",
# # # "Who was the oldest living president",
# # # "Which president had the longest campaign",
# # # "Which class are presidents most relevant in",
# # # "Why did Abraham Lincoln not support slavery",
# # # "Which Easterner out of this list came to America first",
# # # "Who travels",
# # # "Who is the current vice president of america",
# # # "Whomost closely rules the world",
# # #}

# # for i, v in questions.items():
# #     print(i, v['question'])
# #     answer = input()
# #     print('you put: ', answer)
