import time
playeravatar = ["dragon", "giant", "witch", "grim reaper"]
player1name = input("Player 1, enter your name(or nickname): ")
player2name = input("Player 2, enter your name(or nickname): ")
# moves
dragonmoves = ["fireball", "resistance", "claws of death"]
giantmoves = ["stomp", "roar", "smash"]
witchmoves = ["whip", "shield", "thunderbolt"]
grimreapermoves = ["blade of souls", "undead army", "soul extraction"]

# player avatar choose
choose = input("Player 1! Choose your fighter!(dragon, giant, witch, grim reaper): ")
while choose.lower() not in playeravatar:
    choose = input("Choice not available. Choose your fighter!(dragon, giant, witch, grim reaper): ")

# player 1 health
if choose.lower() == "dragon" or choose.lower() == "giant":
    playerhealth = 200
    print(player1name, ", You have 200 health!!")
else:
    playerhealth = 100
    print(player1name, ", You have 100 health!!")

# player 2 avatar choose
choose2 = input("Player 2! Choose your fighter!(dragon, giant, witch, grim reaper): ")
while choose2.lower() not in playeravatar:
    choose2 = input("Choice not available. Choose your fighter!(dragon, giant, witch, grim reaper): ")

# player 2 health
if choose2.lower() == "dragon" or choose2.lower() == "giant":
    player2health = 200
    print(player2name, ", You have 200 health!!")
else:
    player2health = 100
    print(player2name, ", You have 100 health!!")

# player 1 game mechanics
while playerhealth > 0 and player2health > 0:

    if choose.lower() == "dragon":
        move = input("Choose your move!(fireball, resistance, claws of death): ")
        while move.lower() not in dragonmoves:
            move = input("Choice not available. Choose your move!(fireball, resistance, claws of death): ")
    elif choose.lower() == "giant":
        move = input("Choose your move!(stomp, roar, smash): ")
        while move.lower() not in giantmoves:
            move = input("Choice not available. Choose your move!(stomp, roar, smash): ")
    elif choose.lower() == "witch":
        move = input("Choose your move!(whip, shield, thunderbolt): ")
        while move.lower() not in witchmoves:
            move = input("Choice not available. Choose your move!(whip, shield, thunderbolt): ")
    elif choose.lower() == "grim reaper":
        move = input("Choose your move!(blade of souls, undead army, soul extraction): ")
        while move.lower() not in grimreapermoves:
            move = input("Choice not available. Choose your move!(blade of souls, undead army, soul extraction): ")

    # player 2 game mechanics
    if choose2.lower() == "dragon":
        move2 = input("Choose your move!(fireball, resistance, claws of death): ")
        while move2.lower() not in dragonmoves:
            move2 = input("Choice not available. Choose your move!(fireball, resistance, claws of death): ")
    elif choose2.lower() == "giant":
        move2 = input("Choose your move!(stomp, roar, smash): ")
        while move2.lower() not in giantmoves:
            move2 = input("Choice not available. Choose your move!(stomp, roar, smash): ")
    elif choose2.lower() == "witch":
        move2 = input("Choose your move!(whip, shield, thunderbolt): ")
        while move2.lower() not in witchmoves:
            move2 = input("Choice not available. Choose your move!(whip, shield, thunderbolt): ")
    elif choose2.lower() == "grim reaper":
        move2 = input("Choose your move!(blade of souls, undead army, soul extraction): ")
        while move2.lower() not in grimreapermoves:
            move2 = input("Choice not available. Choose your move!(blade of souls, undead army, soul extraction): ")

    # move cancellation
    if move == move2:
        print("The moves cancelled out each other!! An energy wave travels through the air...")

    # player 1 dragon damage
    if move.lower() == "fireball":
        if move2.lower() != "resistance" and move2.lower() != "shield" and move != move2:
            player2health -= 10
            print(player1name, "dealt 10 damage!!")
        else:
            print("No damage dealt!!")
    elif move.lower() == "resistance":
        print(player1name, "has blocked all damage!!")
    elif move.lower() == "claws of death":
        if move2.lower() != "resistance" and move2.lower() != "shield" and move != move2:
            player2health -= 10
            print(player1name, "dealt 10 damage!!")
        else:
            print("No damage dealt!!")
       

    # player 1 giant damage
    if move.lower() == "stomp":
        if move2.lower() != "resistance" and move2.lower() != "shield" and move != move2:
            player2health -= 10
            print(player1name, "dealt 10 damage!!")
        else:
            print("No damage dealt!!")
    elif move.lower() == "roar":
        if move2.lower() != "resistance" and move2.lower() != "shield" and move != move2:
            player2health -= 10
            print(player1name, "dealt 10 damage!!")
        else:
            print("No damage dealt!!")
    elif move.lower() == "smash":
        if move2.lower() != "resistance" and move2.lower() != "shield" and move != move2:
            player2health -= 10
            print(player1name, "dealt 10 damage!!")
        else:
            print("No damage dealt!!")

    # player 1 witch damage
    if move.lower() == "whip":
        if move2.lower() != "resistance" and move2.lower() != "shield" and move != move2:
            player2health -= 40
            print(player1name, "dealt 40 damage!!")
        else:
            print("No damage dealt!!")
    elif move.lower() == "shield":
        print(player1name, "has blocked all damage!!")
    elif move.lower() == "thunderbolt":
        if move2.lower() != "resistance" and move2.lower() != "shield" and move != move2:
            player2health -= 40
            print(player1name, "dealt 40 damage!!")
        else:
            print("No damage dealt!!")
    # player 1 grim reaper damage
    if move.lower() == "blade of souls":
        if move2.lower() != "resistance" and move2.lower() != "shield" and move != move2:
            player2health -= 40
            print(player1name, "dealt 40 damage!!")
        else:
            print("No damage dealt!!")
    elif move.lower() == "undead army":
        if move2.lower() != "resistance" and move2.lower() != "shield" and move != move2:
            player2health -= 40
            print(player1name, "dealt 40 damage!!")
        else:
            print("No damage dealt!!")
    elif move.lower() == "soul extraction":
        if move2.lower() != "resistance" and move2.lower() != "shield" and move != move2:
            player2health -= 40
            print(player1name, "dealt 40 damage!!")
        else:
            print("No damage dealt!!")
          

    # player 2 dragon damage
    if move.lower() == "fireball":
        if move.lower() != "resistance" and move.lower() != "shield" and move != move2:
            playerhealth -= 10
            print(player2name, "dealt 10 damage!!")
            time.sleep(1)
            print(player1name, "has", playerhealth, "health left.")
            time.sleep(1)
            print(player2name, "has", player2health, "health left.")
        else:
            print("No damage dealt!!")
            time.sleep(1)
            print(player1name, "has", playerhealth, "health left.")
            time.sleep(1)
            print(player2name, "has", player2health, "health left.")
    elif move.lower() == "resistance":
        print(player2name, "has blocked all damage!!")
        time.sleep(1)
        print(player1name, "has", playerhealth, "health left.")
        time.sleep(1)
        print(player2name, "has", player2health, "health left.")
       
    elif move.lower() == "claws of death":
        if move.lower() != "resistance" and move.lower() != "shield" and move != move2:
            playerhealth -= 10
            print(player2name, "dealt 10 damage!!")
            time.sleep(1)
            print(player1name, "has", playerhealth, "health left.")
            time.sleep(1)
            print(player2name, "has", player2health, "health left.")
        else:
            print("No damage dealt!!")
            time.sleep(1)
            print(player1name, "has", playerhealth, "health left.")
            time.sleep(1)
            print(player2name, "has", player2health, "health left.")
           

    # player 2 giant damage
    if move.lower() == "stomp":
        if move.lower() != "resistance" and move.lower() != "shield" and move != move2:
            playerhealth -= 10
            print(player2name, "dealt 10 damage!!")
            time.sleep(1)
            print(player1name, "has", playerhealth, "health left.")
            time.sleep(1)
            print(player2name, "has", player2health, "health left.")
        else:
            print("No damage dealt!!")
            time.sleep(1)
            print(player1name, "has", playerhealth, "health left.")
            time.sleep(1)
            print(player2name, "has", player2health, "health left.")
    elif move.lower() == "roar":
        if move.lower() != "resistance" and move.lower() != "shield" and move != move2:
            playerhealth -= 10
            print(player2name, "dealt 10 damage!!")
            time.sleep(1)
            print(player1name, "has", playerhealth, "health left.")
            time.sleep(1)
            print(player2name, "has", player2health, "health left.")
        else:
            print("No damage dealt!!")
            time.sleep(1)
            print(player1name, "has", playerhealth, "health left.")
            time.sleep(1)
            print(player2name, "has", player2health, "health left.")
           
    elif move.lower() == "smash":
        if move.lower() != "resistance" and move.lower() != "shield" and move != move2:
            playerhealth -= 10
            print(player2name, "dealt 10 damage!!")
            time.sleep(1)
            print(player1name, "has", playerhealth, "health left.")
            time.sleep(1)
            print(player2name, "has", player2health, "health left.")
        else:
            print("No damage dealt!!")
            time.sleep(1)
            print(player1name, "has", playerhealth, "health left.")
            time.sleep(1)
            print(player2name, "has", player2health, "health left.")

    # player 2 witch damage
    if move.lower() == "whip":
        if move.lower() != "resistance" and move.lower() != "shield" and move != move2:
            playerhealth -= 40
            print(player2name, "dealt 40 damage!!")
            time.sleep(1)
            print(player1name, "has", playerhealth, "health left.")
            time.sleep(1)
            print(player2name, "has", player2health, "health left.")
        else:
            print("No damage dealt!!")
            time.sleep(1)
            print(player1name, "has", playerhealth, "health left.")
            time.sleep(1)
            print(player2name, "has", player2health, "health left.")
    elif move.lower() == "shield":
        print(player2name, "has blocked all damage!!")
        time.sleep(1)
        print(player1name, "has", playerhealth, "health left.")
        time.sleep(1)
        print(player2name, "has", player2health, "health left.")
    elif move.lower() == "thunderbolt":
        if move.lower() != "resistance" and move.lower() != "shield" and move != move2:
            playerhealth -= 40
            print(player2name, "dealt 40 damage!!")
            time.sleep(1)
            print(player1name, "has", playerhealth, "health left.")
            time.sleep(1)
            print(player2name, "has", player2health, "health left.")
        else:
            print("No damage dealt!!")
            time.sleep(1)
            print(player1name, "has", playerhealth, "health left.")
            time.sleep(1)
            print(player2name, "has", player2health, "health left.")
          
    # player 2 grim reaper damage
    if move.lower() == "blade of souls":
        if move.lower() != "resistance" and move.lower() != "shield" and move != move2:
            playerhealth -= 40
            print(player2name, "dealt 40 damage!!")
            time.sleep(1)
            print(player1name, "has", playerhealth, "health left.")
            time.sleep(1)
            print(player2name, "has", player2health, "health left.")
        else:
            print("No damage dealt!!")
            time.sleep(1)
            print(player1name, "has", playerhealth, "health left.")
            time.sleep(1)
            print(player2name, "has", player2health, "health left.")
    elif move.lower() == "undead army":
        if move.lower() != "resistance" and move.lower() != "shield" and move != move2:
            playerhealth -= 40
            print(player2name, "dealt 40 damage!!")
            time.sleep(1)
            print(player1name, "has", playerhealth, "health left.")
            time.sleep(1)
            print(player2name, "has", player2health, "health left.")
        else:
            print("No damage dealt!!")
            time.sleep(1)
            print(player1name, "has", playerhealth, "health left.")
            time.sleep(1)
            print(player2name, "has", player2health, "health left.")
    elif move.lower() == "soul extraction":
        if move.lower() != "resistance" and move.lower() != "shield" and move != move2:
            playerhealth -= 40
            print(player2name, "dealt 40 damage!!")
            time.sleep(1)
            print(player1name, "has", playerhealth, "health left.")
            time.sleep(1)
            print(player2name, "has", player2health, "health left.")
        else:
            print("No damage dealt!!")
            time.sleep(1)
            print(player1name, "has", playerhealth, "health left.")
            time.sleep(1)
            print(player2name, "has", player2health, "health left.")

# check if game lost
if playerhealth <= 0 and player2health <= 0:
    print("Tie!!")
elif player2health <= 0:
    print(player1name, "wins!!")
else:
    print(player1name, "wins!!")