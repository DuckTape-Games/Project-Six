'''
Code Name: Project Six
Concept: Dice based roguelike game
Lead Developer: Chris Herriman Jr
Publisher: DuckTape Games
Start Date: 4/27/2026
'''

#############
### SETUP ###
#############

#Imports
from random import randint as rnd #used for random number generation
import turtle as trtl #Used for graphics
import customtkinter as ctk #Used for UI -> Works within turtle
from pygame import mixer #Used for sound and music
import json #Used for data storage

from utils import theme
from ui import main_menu

#Variables
SCREEN_X = 900
SCREEN_Y = 700
root = ctk.CTk(fg_color=theme.BACKGROUND_COLOR)
root.geometry(str(SCREEN_X)+"x"+str(SCREEN_Y))
root.resizable(False,False)
root._set_appearance_mode("dark")

canvas = ctk.CTkCanvas(root, width=SCREEN_X, height=SCREEN_Y, bd=0, highlightthickness=0)
canvas.place(x=0,y=0)

screen = trtl.TurtleScreen(canvas)
screen.bgcolor(theme.BACKGROUND_COLOR)


main_menu.create_main_menu(root)

root.mainloop()