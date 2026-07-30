import os, sys #Used for file based systems
from PIL import Image
import customtkinter as ctk

### Makes onefile mode work in pyinstaller
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


### Converts between Tkinter coordinates and Turtle coordinates
#Not giving any coordinates returns 0,0 unless tk is specified
#Use tk for Tkinter
#Use trtl for Turtle
def tk_trtl_coord_convert(x=None,y=None,base_system="trtl",screen_x=900,screen_y=700):
    if x is None and y is None:
        if base_system.lower() == "tk":
            return (screen_x/2,screen_y/2)
        return (0,0)

    
    def convert_to_tk(value,size,orientation="x"):
        if orientation.lower() == "x":
            return value + (size/2)
        return (size/2) - value

    
    def convert_to_trtl(value,size,orientation="x"):
        if orientation.lower() == "x":
            return value - (size/2)
        return (size/2) - value

    
    if base_system.lower() == "trtl":
        if x is None:
            return (None, convert_to_tk(y,screen_y,"y"))
        if y is None:
            return (convert_to_tk(x,screen_x,"x"),None)
        return(convert_to_tk(x,screen_x,"x"),convert_to_tk(y,screen_y,"y"))

    
    if x is None:
        return(None, convert_to_trtl(y,screen_y,"y"))
    if y is None:
        return(convert_to_trtl(x,screen_x,"x"),None)
    return (convert_to_trtl(x,screen_x,"x"),convert_to_trtl(y,screen_y,"y"))



########################
### Resizes an Image ###
########################

def prepare_image(root, image, new_width=None, new_height=None):
    """
    If neither dimension is given, the original image is returned.
    If both dimensions are given, the image is stretched to fit them.
    If only one dimension is given, the original aspect ratio is preserved.
    """

    def resize_image(image, new_width=None, new_height=None):
        # Reads the source image dimensions for ratio calculations
        original_width, original_height = image.size

        # Returns the original image when no new size is requested
        if not new_width and not new_height:
            return image

        # Calculates the matching height when only a width is given
        if new_width and not new_height:
            ratio = new_width / original_width
            new_height = int(original_height * ratio)

        # Calculates the matching width when only a height is given
        elif new_height and not new_width:
            ratio = new_height / original_height
            new_width = int(original_width * ratio)

        # Creates the resized image with the calculated dimensions
        return image.resize((new_width, new_height))


    image = Image.open(image).convert("RGBA")

    if new_height or new_width:
        image = resize_image(image, new_width, new_height)

    placable_image = ctk.CTkImage(
        light_image=image,
        dark_image=image,
        size=image.size
    )

    image_label = ctk.CTkLabel(
      root,
      image=placable_image,
      text="",
      fg_color="transparent"
    )
    image_label.image = placable_image

    return image_label



