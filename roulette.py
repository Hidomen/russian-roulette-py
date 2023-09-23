import random

gun = [0,0,0,0,0,0]

gun[random.randint(0,5)] = 1 # placing a bullet in gun
turn = 0

while True :
    player_act = input("WHEN YOU'RE READY TYPE -> GO \n").upper()
    if player_act == "GO" :
        #
        if gun[turn] == 0 :
            print("EMPTY")
            turn += 1
        else :
            print("BOOM YOU'RE DEAD")
            break
    else : 
        print("INVALID ACT PLEASE TYPE GO")