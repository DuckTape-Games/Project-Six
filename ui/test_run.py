import customtkinter as ctk
from utils import helpers, theme


def start_run(root):
    helpers.clear_screen(root)
    for i in range(5):
        root.grid_rowconfigure(i,weight=1)
        root.grid_columnconfigure(i,weight=1)

    player_character = helpers.prepare_image(root, theme.player_character,new_height=400)
    player_character.grid(row=1,column=0)

    enemy = helpers.prepare_image(root, theme.snake_eyes,new_height=300)
    enemy.grid(row=1,column=4)


    

    