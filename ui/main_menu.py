import customtkinter as ctk
from utils import theme, helpers


def create_main_menu(root):
    create_grid(root)
    button = ctk.CTkButton(
        root, 
        text="Start Game",
        bg_color=theme.BACKGROUND_COLOR, 
        fg_color=theme.SECONDARY_COLOR,
        text_color=theme.DARK_WHITE,
        hover_color=theme.TERTIARY_COLOR,
        width=100,
        height=50,
        anchor="center"
    )
    button.grid(
        row=3,
        column=2
    )

    main_image = helpers.prepare_image(root,"assets/dicepile.png",300)
    main_image.grid(row=2,column=2)

def create_grid(root):
    for i in range(5):
        root.grid_rowconfigure(i,weight=1)
        root.grid_columnconfigure(i,weight=1)