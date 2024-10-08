import random
plyrin = True
delrin = True
deck = [2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,9,10, 'J', 'Q', 'K', 'A','J', 'Q', 'K', 'A','J', 'Q', 'K', 'A','J', 'Q', 'K', 'A'] #bcz 4 sets of cards
plyrhand = []
delrhand = []

#dealing the cards
def dealCards(turn):
    card = random.choice(deck)
    turn.append(card)
    deck.remove(card)
    
#calculate the total of each hand 
def total(turn):
    total = 0
    face = ['K', 'Q', 'J']
    for card in turn:
        if card in range(1,11):
            total+=card
        elif card in face:
            total +=1
        else:
            if total >  11:
                total +=10
            else:
                total += 11
    return total

#check the winner  
def revealwinner():
    if len(delrhand) == 2:
        return delrhand[0]
    elif len(delrhand) > 2:
        return delrhand[0], delrhand[1]
    
#game loop              
for _ in range(2):
    dealCards(delrhand)
    dealCards(plyrhand)
    
while plyrin or delrin:
    print(f"dealer had {revealwinner()} and X")
    print(f"you have {plyrhand} for a total of {total(plyrhand)}")
    if plyrin:
        stayOrHit = input("1: stay\n2: hit \n")
    if total(delrhand)>16:
        delrin = False
    else:
        dealCards(delrhand)
    if stayOrHit == '1':
        plyrin = False
    else:
        dealCards(plyrhand)
        
    if total(plyrhand)>=21:
        break
    elif total(delrhand) >=21:
        break
    
if total(plyrhand) == 21:
    print(f"\n you have {plyrhand} for a total of {total(plyrhand)} and the dealer has {delrhand} for the total of {total(delrhand)}")
    print("blackjack!! YOU WIN! ")
elif total(delrhand) == 21:
    print(f"\n you have {plyrhand} for a total of {total(plyrhand)} and the dealer has {delrhand} for the total of {total(delrhand)}")
    print("blackjack!! DEALER WIN!! ")
elif total(plyrhand) > 21:
    print(f"\n you have {plyrhand} for a total of {total(plyrhand)} and the dealer has {delrhand} for the total of {total(delrhand)}")
    print("you brust!, DEALER WIN!")
elif total(delrhand) > 21:
    print(f"\n you have {plyrhand} for a total of {total(plyrhand)} and the dealer has {delrhand} for the total of {total(delrhand)}")
    print("dealer brust, YOU WIN!!")

elif 21-total(delrhand) < 21-total(plyrhand):
    print(f"\n you have {plyrhand} for a total of {total(plyrhand)} and the dealer has {delrhand} for the total of {total(delrhand)}")
    print("DEALER WIN!!, he has less cards ")
    
elif 21-total(delrhand) > 21-total(plyrhand):
    print(f"\n you have {plyrhand} for a total of {total(plyrhand)} and the dealer has {delrhand} for the total of {total(delrhand)}")
    print("YOU WIN!!, dealer has more cards than you ")