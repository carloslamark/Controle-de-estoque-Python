from distutils import command
from email.mime import application
from tkinter import *
from tkinter.filedialog import Directory
from tkinter.font import BOLD
from ctypes.wintypes import RGB
from tkinter import ttk

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase import ttfonts
from reportlab.platypus import SimpleDocTemplate, Image
import webbrowser

import json_manager as json
import re