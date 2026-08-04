'''
Code Name: Project Six
Concept: Dice based roguelike game
Lead Developer: Chris Herriman Jr
Publisher: DuckTape Games
Development Start 7/24/2026
'''

#############
### SETUP ###
#############

#Imports
from random import randint as rnd #used for random number generation
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

mixer.init()
mixer.music.load(theme.main_menu_music)
mixer.music.play(-1)



main_menu.create_main_menu(root)

root.mainloop()