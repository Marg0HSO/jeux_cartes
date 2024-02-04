from random import randint

bank_card = []
player_card = []

def play():

    bank_card = [randint(1, 13) for i in range(2)]
    player_card = [randint(1, 13) for i in range(2)]

    game = True

    while game:
        print(player_card)

        if sum(player_card)==21:
            print("Black Jack")
            return True
          
        elif sum(player_card)>21:
            print("Depassé")
            return False
          
        else:
            choice = int(input("Voulez vous piocher une autre carte : 1/oui, 2/non"))
            while choice not in [1, 2]:
                print("entrez un nombre valide")
                choice = int(input("Voulez vous piocher une autre carte : 1/oui, 2/non"))

        if choice == 1:
            player_card.append(randint(1, 13))
        else:
            bank_game = True
            while game:
              
                if sum(bank_card)<17:
                    bank_card.append(randint(1, 13))
                  
                else:
                    print(bank_card)
                    game = False

                    if sum(bank_card)>21:
                        print("depassé")
                        return True
                    elif sum(bank_card)<sum(player_card):
                        print("player win")
                        return True
                    elif sum(bank_card)>sum(player_card):
                        print("Bank win")
                        return False
                    elif bank_card==21:
                        print("Bank Black Jack")
                        return False

win = play()

if win == True:
    print("Vous avez gagner la partie")
else:
    print("Vous avez perdu la partie")
