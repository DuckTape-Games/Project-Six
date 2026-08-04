import random

#A die's side has 2 values: [0] is the value and [1] is the bonus effect. Use None in [1] if there is no bonus effect
#Any mathematical secondary effects will have x2, ^5, etc. 

#The turn functionality
#The player and the enemy both roll, and then the effects are decided with the player's effect going first
def turn(player_dice,enemy_dice):
    player_turn_total = (0,None)
    enemy_turn_total = (0,None)
    for i in range(len(player_dice)):

        if player_turn_total[1] != "r":
            player_roll = roll_die(player_dice[i])
            player_turn_total = check_effect(
                player_roll,
                player_turn_total[0],
                player_dice,
                i
            )
        else:
            player_turn_total = (player_turn_total[0],None)

        if enemy_turn_total[1] != "r":
            enemy_roll = roll_die(enemy_dice[i])
            enemy_turn_total = check_effect(
                enemy_roll,
                enemy_turn_total[0],
                enemy_dice,
                i
            )
        else:
            enemy_turn_total = (enemy_turn_total[0],None)

    return (player_turn_total[0], enemy_turn_total[0])



#Returns a random side from a die
def roll_die(sides):
    return sides[random.randint(1,len(sides))-1]


#Checks the effects of the rolled die
def check_effect(roll, turn_total, dice, active_die_num):
    turn_total += roll[0] #The rolled number gets added first before the effect is calculated

    try:
        if roll[1] == None:
            return (turn_total,None)
        if roll[1][0] == "+": #Adds the value indecated beside the +
            return (turn_total + int(roll[1][1:]), None)

        if roll[1][0].lower() == "x": #Multiplies the total by the value indicated beside the x
            return (turn_total * int(roll[1][1:]), None)

        if roll[1][0] == "^": #Raises the running total to the power indicated after ^
            return (turn_total ** int(roll[1][1:]), None)

        if roll[1][0].lower() == "c": #Rerolls the active die
            return check_effect(
                roll_die(dice[active_die_num]),
                turn_total,
                dice,
                active_die_num
            )

        if roll[1][0].lower() == "l": #Rerolls both the previous die and the active die. left acts as center when it is the first die in the sequence
            if active_die_num > 0:
                turn_total = check_effect(
                    roll_die(dice[active_die_num - 1]),
                    turn_total,
                    dice,
                    active_die_num - 1
                )
            else:
                turn_total = (turn_total,None)
            if turn_total[1] != "r":
                return check_effect(
                    roll_die(dice[active_die_num]),
                    turn_total[0],
                    dice,
                    active_die_num
                )
            return turn_total

        if roll[1][0].lower() == "r":
            return (turn_total,"r")

    except (ValueError, RecursionError): #Catches future errors such as a die starting with x but not being multiply or the rare edge case where a die happens to roll left or center 1000 times 
        pass
    except Exception as e: #Catches errors and notifies the user, but lets the game continue
        print(e)
    return (turn_total,None)