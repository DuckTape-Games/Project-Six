from utils import helpers

### Colors
BACKGROUND_COLOR = "#d97a7a"
SECONDARY_COLOR = "#8f3f3f"
TERTIARY_COLOR = "#4b2020"

DARK_WHITE = "#E1D9D1"


### Images
dice = []
for i in range(6):
    dice.append(helpers.resource_path("assets/die_" + str(i+1) + ".png"))