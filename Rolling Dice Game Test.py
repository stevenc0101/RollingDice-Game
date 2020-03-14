import random
import time
print("Computer VS Player")
a = 10000
def cvp():
    print("Game Starts")
    time.sleep(1)
    global a  
    print("Remaining: $"+str(a))
    bet = int(input("Bet:$"))
    print("Rolling Dice......")
    time.sleep(1)
    print("Rolling......")
    time.sleep(3)
    dico = random.randint(0,6)
    print("Computer:"+str(dico))
    time.sleep(3)
    dipl = random.randint(0,6)
    print("Player:"+str(dipl))
    if dico>dipl:
	    print("You Loss")
	    a = a-bet
	    print("Remaining: $"+str(a))
          
    elif dico<dipl:
              print("You Win")
              a = a+bet
              print("Remaining: $"+str(a))
while a>0:
    cvp()
if a<=0:
    print("Sorry,Game Over")
   
         
         
