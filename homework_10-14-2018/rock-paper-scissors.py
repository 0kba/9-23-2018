
first = str.lower(input(print("first player: what is your name ?")))
second = str.lower(input(print("second player: what is your name ?")))


firstplayer = str.lower(input(print(f"{first}, please write rock,paper or scissors")))
secondplayer = str.lower(input(print(f"{second}, please write rock,paper or scissors")))

if firstplayer == "rock" :
    if secondplayer == "paper":
        print(f"{second} WINS!")
    elif secondplayer == "scissors":
        print(f"{first} WINS!")
    else: print("DRAW!")

elif firstplayer == "paper" :
    if secondplayer == "scissors":
        print(f"{second} WINS!")
    elif secondplayer == "rock":
        print(f"{first} WINS!")
    else: print("DRAW!")

elif firstplayer == "scissors" :
    if secondplayer == "paper":
        print(f"{first} WINS!")
    elif secondplayer == "rock":
        print(f"{second} WINS!")
    else: print("DRAW!")

else: print("please check the spelling")
