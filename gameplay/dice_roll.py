import random

#A die's side has 2 values: [0] is the value and [1] is the bonus effect. Use None in [1] if there is no bonus effect
#Any mathematical secondary effects will have x2, ^5, etc. 

def turn(player_dice,enemy_dice):
    player_turn_total = 0
    enemy_turn_total = 0
    for i in range(len(player_dice)):
        player_roll = roll_die(player_dice[i])
        enemy_roll = roll_die(enemy_dice[i])
        player_turn_total = check_effect(player_roll,player_turn_total)
        enemy_turn_total = check_effect(enemy_roll,enemy_turn_total)

    return (player_turn_total,enemy_turn_total)





def roll_die(sides):
    return sides[random.randint(1,len(sides))-1]


def check_effect(roll,turn_total):
    turn_total += roll[0]

    try:

        if roll[1][0].lower() == "x":
            return turn_total * int(roll[1][1:])

        if roll[1][0] == "^":
            return turn_total ** int(roll[1][1:])

    except:
        return turn_total