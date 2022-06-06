print{"welcome to rock Paper sccissor"}
print{"-------------------------------"}
### set up varriables
cpuscore=0
playerscore=0
tiescore=0
posibilities=["Rock", "paper","Scissor"]

def checkforwinner(playhand,computerhand):
    if(playerHand =="Rock" and computerHand=="paper"):
        print("sorry you lost :)")
        return"cpu"
    elif(playerHand == "Rock" and computerHand =="scissors"):
        print("congrats! you have won:)")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
        return"player"
    elif(playerHand == "scissors" and computerHand == "paper"):
        print("congrats! you won:)")
        return"player"
    elif(playerHand =="scissors" and computerHand == "Rock"):
        print("sorry you lost!")
        return "cpu"
    elif(playerHand == "paper" and computerHand == "Rock"):                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    "paper and computerhand == "Rock"):
    print("congrate! you won:)")
    return "player"
    elif(playerhand =="paper" and computerhand == "scissors"):
    print("sorry,you lost!")
    return"cpu"
    else:
    print("it's a tie.play again")
    return"tie"
        ### start game loop
    while(playerscore !=3 and cpuscore !=3):
        ### validate input
        while True:
            playerHand = input("\npick a hand,Rock,Paper,or Scissors:")
            if(playerhand == "Rock" or playerhand == "paper or playerhand =="Scissor):
                break
            else:
                print("invalid input. Try again.")
                ###Generate pick
                computerhand=radom.choice(posibiehand)
                ### print results 
                print("your hand:",playerHand)
                print("Cpu hand:",computerHand)
                result=checker= checkerforwinner(playerHand,computerHand)
                if(result == "player"):
                    playScore+=1
                    elif(result == "cpu"):
                        cpuscore+=1
                        else:
                            tieScore+=1 
                            print("your score:,playerSore,"cpu",cpuScore,"ties",tieScore)