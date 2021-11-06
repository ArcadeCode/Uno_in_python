#imports :
import random

#Set of cards
CARDSdeck = [] #deck of the game #Carte de la pioche
CARDSplayer = [] #deck of players #Les cartes utilisé par les joueurs
CARDSUsed = [] #the deck of used cards #Les cartes ayant été posées
for x in range(108) :
    CARDSdeck.append(x)
print(CARDSdeck)

#Class, Function starting :

def giveCard (numberOfCards) : #Give a number of card at one player #Donne un nombre de cartes à un joueur
    CARDSthisPlayer = []
    for x in range(numberOfCards) :
        randomNumber = random.randint(1, CARDSdeck)
        CARDSplayer.append(CARDSdeck[randomNumber])
        CARDSthisPlayer.append(CARDSdeck[randomNumber])
        del CARDSdeck[randomNumber]
    print(CARDSdeck)
    print(CARDSplayer)
    print(CARDSthisPlayer)
    return CARDSthisPlayer

class Player :
    "Player object"
    def __init__(self):
        self.players = []

    def getStartCards(self, numberOfCard, playerName):
        self.name = playerName
        self.cardsStock = giveCard(numberOfCard)
        self.players.append(self.name)


class Card:
    "The def of Uno Card."
    def __init__(self, CARDSdeck) :
        self.playerDeck = {}
        self.deck = CARDSdeck
        for x in Player.players :
            self.playerDeck[Player.players[x] = "none"]




#Launch objects
A = Player()
B = Player()
C = Player()

A.getStartCards(7, "Martin")
#B.getStartCards(7, "Arcade")
#C.getStartCards(7, "George")