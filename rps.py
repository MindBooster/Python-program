# human enter
# bot enter
import random
x='y'
while x=='Y' or x=='y':
    win_score = 0
    for i in range(5):
        human = input("Enter choice(rock/paper/scissor): ")
        bot = ["rock","paper","scissor"][random.randint(0,2)]


        take = {'rock':{'paper':[0, 1],'scissor':[1, 0],'rock':[0.5, 0.5]},
                'paper':{'paper':[0.5, 0.5],'scissor':[0, 1],'rock':[1, 0]},
                'scissor':{'paper':[1, 0],'scissor':[0.5, 0.5],'rock':[0, 1]}}

        result=take[human][bot]
        print(bot)
        

        if result==[0,1]:
            print("Loser!")
        elif result==[1,0]:
            print("Winner!")
        elif result==[0.5,0.5]:
            print("Draw")

        
        if result==[1,0]:
            
            win_score+=1

    print("Score: ",win_score)
    x=input("Do you want to play again?(Y/N) ")
else:
    quit()
