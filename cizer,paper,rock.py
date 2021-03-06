import random
def playGame():
    options=["scissor","paper","rock"]
    computer_selection = random.choice(options)
    your_hand=int(input('it is your turn!\nchose one\n1.scissor\n2.paper\n3.rock\n'))
    print(your_hand)

    if your_hand > 0 and your_hand <=3:
    #condition for lose the match
        print("Computer Selection - ",computer_selection)
        if options[your_hand-1] == computer_selection:
            print("Draw")
        elif your_hand==1 and computer_selection=="rock":
            print('you lose')
        elif your_hand==2 and computer_selection=="scissor":
            print('you lose')
        elif your_hand==3 and computer_selection=="paper":
            print('you lose')
        else:
            print("You Win")
    else:
        print('you know one intresting thing\n we are playing SCISSOR! PAPPER AND ROCK!\nLOL!')
for i in range(0,10):
    playGame()