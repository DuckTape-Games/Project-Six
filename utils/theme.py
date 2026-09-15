from utils import helpers

### Colors
BACKGROUND_COLOR = "#33475B"
SECONDARY_COLOR = "#919191"
TERTIARY_COLOR = "#111820"

DARK_WHITE = "#E1D9D1"




### Images
dice = []
for i in range(6):
    dice.append(helpers.resource_path("assets/die_" + str(i+1) + ".png"))

main_menu_music = helpers.resource_path("audio/music/main_menu.wav")


player_character = helpers.resource_path("assets/characters/player.png")
snake_eyes = helpers.resource_path("assets/characters/snake_eyes.png")