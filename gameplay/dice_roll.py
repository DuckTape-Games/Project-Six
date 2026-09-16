import random

#A die's side has 2 values: [0] is the value and [1] is the bonus effect. Use None in [1] if there is no bonus effect
#Any mathematical secondary effects will have x2, ^5, etc. 

poison_venom = None #This boolean functions as a global tri bool. Affects the next roll, doesn't matter which player rolled the effect and which player gets affected
                    #None -> No active poison or venom
                    #False -> Venom is active. The next base roll by either player is halved
                    #True -> Poison is active. The next roll has its mathematical effect's number cut in half when applicable



#The turn functionality
#The player and the enemy both roll, and then the effects are decided with the player's effect going first
def turn(player_dice,enemy_dice):
    global poison_venom
    poison_venom = None

    player_turn_total = (0,None)
    enemy_turn_total = (0,None)
    for i in range(len(player_dice)):

        if player_turn_total[1] != "right":
            player_roll = roll_die(player_dice[i])
            turn = check_effect(
                player_roll,
                player_turn_total[0],
                player_dice,
                i,
                enemy_turn_total[0]
            )
            player_turn_total = (turn[0], turn[1])
            enemy_turn_total = (turn[2], enemy_turn_total[1])
        else:
            player_turn_total = (player_turn_total[0],None)

        if enemy_turn_total[1] != "right":
            enemy_roll = roll_die(enemy_dice[i])
            turn = check_effect(
                enemy_roll,
                enemy_turn_total[0],
                enemy_dice,
                i,
                player_turn_total[0]
            )
            enemy_turn_total = (turn[0], turn[1])
            player_turn_total = (turn[2], player_turn_total[1])
        else:
            enemy_turn_total = (enemy_turn_total[0],None)

    return (player_turn_total[0], enemy_turn_total[0])



#Returns a random side from a die
def roll_die(sides):
    return sides[random.randint(1,len(sides))-1]


#Checks the effects of the rolled die
def check_effect(roll, turn_total, dice, active_die_num, opponent_total):
    global poison_venom
    if poison_venom is not False:
        turn_total += roll[0] #The rolled number gets added first before the effect is calculated
    else: #Applies venom
        turn_total += (roll[0]/2)
        if turn_total > int(turn_total):
            turn_total = int(turn_total) + 1

    try:
        if roll[1] is not None and roll[1][0] in ["+","x","X","^","-","/","v","V"]: 
                effect_value = int(roll[1][1:])
                if poison_venom:#Applies poison before applying the active roll's effect
                    effect_value /= 2
                    if effect_value > int(effect_value):
                        effect_value += 1
                    effect_value = int(effect_value)
        poison_venom = None

        if roll[1] == None: #Returns if there is no effect
            return (turn_total,None,opponent_total)

        if roll[1].lower() == "poison": #Activates poison for the next roll
            poison_venom = True
            return (turn_total,None,opponent_total)

        if roll[1].lower() == "venom": #Activates venom for the next roll
            poison_venom = False
            return (turn_total,None,opponent_total)
        
        if roll[1][0] == "+": #Adds the value indecated beside the +
            return (turn_total + effect_value, None, opponent_total)

        if roll[1][0].lower() == "x": #Multiplies the total by the value indicated beside the x
            return (turn_total * effect_value, None, opponent_total)

        if roll[1][0] == "^": #Raises the running total to the power indicated after ^
            return (turn_total ** effect_value, None, opponent_total)

        if roll[1][0] in ["-","/","v","V"]:
            if opponent_total > 0:

                if roll[1][0] == "-": #Subtracts from the opponent's total
                    opponent_total -= effect_value
                    if opponent_total <= 0:
                        return (turn_total, None, 0)
                    return (turn_total, None, opponent_total)

                if roll[1][0] == "/": #Divides the opponent's total. Always rounds up to the nearest whole number
                    opponent_total /= effect_value
                    if opponent_total > int(opponent_total):
                        opponent_total = int(opponent_total) + 1
                    return (turn_total, None, opponent_total)

                if roll[1][0].lower() == "v": #Takes the root of the opponent's total. Always rounds up to the nearest whole number
                    opponent_total = opponent_total ** (1/effect_value)
                    if opponent_total > int(opponent_total):
                        opponent_total = int(opponent_total) + 1
                    return (turn_total, None, opponent_total)

        if roll[1].lower() == "center": #Rerolls the active die
            return check_effect(
                roll_die(dice[active_die_num]),
                turn_total,
                dice,
                active_die_num, 
                opponent_total
            )

        if roll[1].lower() == "left": #Rerolls both the previous die and the active die. left acts as center when it is the first die in the sequence
            if active_die_num > 0:
                turn_total = check_effect(
                    roll_die(dice[active_die_num - 1]),
                    turn_total,
                    dice,
                    active_die_num - 1, 
                    opponent_total
                )
            else:
                turn_total = (turn_total,None,opponent_total)
            if turn_total[1] != "right":
                return check_effect(
                    roll_die(dice[active_die_num]),
                    turn_total[0],
                    dice,
                    active_die_num, 
                    turn_total[2]
                )
            return turn_total

        if roll[1].lower() == "right": #Skips the player's next roll
            return (turn_total,"right",opponent_total)

    except (ValueError, RecursionError): #Catches future errors such as a die starting with x but not being multiply or the rare edge case where a die happens to roll left or center 1000 times 
        pass
    except Exception as e: #Catches errors and notifies the user, but lets the game continue
        print(e)
    return (turn_total,None,opponent_total)