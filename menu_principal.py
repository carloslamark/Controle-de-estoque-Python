from distutils import command
from tkinter import *
from tkinter.filedialog import Directory
from tkinter.font import BOLD
from ctypes.wintypes import RGB
from tkinter import ttk

import json_manager as json
import re

from logging import root

import clients as cli
import products as prod


root = Tk()
clients = cli.Application() 
products = prod.Application()



class AplicationM():
    def __init__(self):
        self.root = root
        self.menu_screen()
        
        root.mainloop()

    def menu_screen(self):
        self.root.title("Menu Principal")
        self.root.configure(background= '#582f0e')
        self.root.geometry('1200x700')
        self.root.resizable(True, True)
        self.root.minsize(width=600, height=500)
        self.frame_1 = Frame(self.root, border=4, bg='#a68a64', highlightbackground='#936639', highlightthickness=3)
        self.frame_1.place(relx=0.02 , rely=0.02, relwidth=0.96, relheight=0.96)
        


AplicationM()