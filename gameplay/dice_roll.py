from utils import theme,helpers
import random

result = None

def roll(root):
    global result
    if result is not None:
        result.destroy()
    result = helpers.prepare_image(root,theme.dice[random.randint(0,len(theme.dice)-1)],300)
    result.grid(row=2,column=2)
    