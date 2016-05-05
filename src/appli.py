# -*- coding: utf-8 -*-
"""
Created on Wed May 04 15:58:45 2016

@author: Yanik
"""

#%%
"""Import libraries
"""
#import numpy as np
from tkinter import * #Change for Tkinter if python 2
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk

import dicom
import os
import numpy as np

from skimage import img_as_float
from skimage import io

"""function to be called when mouse is clicked"""
def printcoords(event):
    #outputting x and y coords to console
    print (event.x,event.y)
        
"""Create a class"""
class Interface(Frame):
    
    """class which is derived from a frame"""
    def __init__(self, fenetre, **kwargs):
        Frame.__init__(self, fenetre, width=768, height=576, **kwargs)
        self.pack(fill=BOTH)
        self.nb_clic = 0
        
        #Build widgets
        self.message = Label(self, text="You didn't click on the button")
        self.message.pack()
                
        self.button_click = Button(self, text="Click center", fg="red",
                                   command=self.cliquer)
        self.button_click.pack(side="right")
        
        self.button_stop = Button(self, text="Stop click", command=self.stop_click)
        self.button_stop.pack(side="right")
        
        self.button_open = Button(self, text="Open", fg="blue", 
                                  command=self.openImg)
        self.button_open.pack(side="left")
        
       
        self.frame = Frame(self, bd=2, relief=SUNKEN)
        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.grid_columnconfigure(0, weight=1)
        self.xscroll = Scrollbar(self.frame, orient=HORIZONTAL)
        self.xscroll.grid(row=1, column=0, sticky=E+W)
        self.yscroll = Scrollbar(self.frame)
        self.yscroll.grid(row=0, column=1, sticky=N+S)
        self.canvas = Canvas(self.frame, bd=0, xscrollcommand=self.xscroll.set, yscrollcommand=self.yscroll.set)
        self.canvas.grid(row=0, column=0, sticky=N+S+E+W)
        self.xscroll.config(command=self.canvas.xview)
        self.yscroll.config(command=self.canvas.yview)
        self.frame.pack(fill=BOTH, expand=1)

        
    def cliquer(self):
        """there was a click on the button
        we change the value  of the label message"""
        #mouseclick event
        self.canvas.bind("<Button 1>", printcoords)
        
    def stop_click(self):
        self.canvas.unbind("<Button 1>") #use returned variable of bind fct as 2nd param if unbind only one fct 
        
        
    def openImg(self):
        #open image and display in canvas
        File = askopenfilename(parent=fenetre, initialdir="C:/",title='Choose an image.')
        self.img = ImageTk.PhotoImage(Image.open(File))
        self.canvas.create_image(0,0,image=self.img,anchor="nw")
        self.canvas.config(scrollregion=self.canvas.bbox(ALL))
    

#%%
#Instantiate window
fenetre = Tk()
interface = Interface(fenetre)
interface.mainloop()
#interface.destroy()
#fenetre.destroy()