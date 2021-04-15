import time
import random
class Card():
    def __init__(self, rank, value, suit):
        self.rank = rank
        self.value = value
        self.suit = suit

    def display_card(self):
        print(str(self.rank)+" of "+str(self.suit))

class Deck():
    def __init__(self):
        self.cards = []

    def build_deck(self):
        suits = ["Hearts", "Diamonds", "Spades","Clubs"]
        ranks = { '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8,
                  '9':9, '10':10, 'J':10, 'Q':10, 'K':10, 'A':11,}

        for suit in suits:
            for rank, value in ranks.items():
                card = Card(rank, value, suit)
                self.cards.append(card)

    def shuffle_deck(self):
        random.shuffle(self.cards)

    def deal_card(self):
        card = random.choice(self.cards)
        return card

class Player():
    def __init__(self):
        self.hand = []
        self.hand_value = 0
        self.playing_hand = True

    def draw_hand(self, deck):
        for x in range(2):
            card = deck.deal_card()
            self.hand.append(card)

    def display_hand(self):
        print("\nPlayer's Hand: ")
        for card in self.hand:
            card.display_card()


    def hit(self,deck):
        card = deck.deal_card()
        self.hand.append(card)


    def get_hand_value(self):
        self.hand_value = 0
        ace_in = False
        for card in self.hand:
            self.hand_value += card.value
            if card.rank == 'A':
                ace_in = True
        if self.hand_value > 21 and ace_in:
            self.hand_value -=10
        print("\nTotal value of the hand "+str(self.hand_value))

    def update_hand(self,deck):
        if self.hand_value < 21:
            choice = input("\nWould you like to hit? (y/n): ")
            if choice == "y":
                self.hit(deck)
            elif choice =="n":
                self.playing_hand = False
        else:
            self.playing_hand = False

class Dealer():
    def __init__(self):
        self.hand = []
        self.hand_value = 0
        self.paying_hand = True

    def draw_hand(self, deck):
        for x in range(2):
            card = deck.deal_card()
            self.hand.append(card)

    def display_hand(self):
        input("Press ENTER to reveal the dealer cards")
        for card in self.hand:
            card.display_card()
        time.sleep(2)

    def hit(self, deck):
        self.get_hand_value()
        while self.hand_value < 17:
            card = deck.deal_card()
            self.hand.append(card)
            self.get_hand_value()
        print("\nDealer's set with a total of "+str(len(self.hand))+" cards.")

    def get_hand_value(self):
        self.hand_value = 0
        ace_in_hand = False
        for card in self.hand:
            self.hand_value += card.value
            if card.rank == 'A':
                ace_in_hand = True
        if self.hand_value > 21 and ace_in_hand:
            self.hand_value -= 10

class Game():
    def __init__(self, amount_money):
        self.money = int(amount_money)
        self.bet = 20
        self.winner = " "

    def set_bet(self):
        betting = True
        while betting:
            bet = int(input("\nEnter how much money you want to bet: "))
            if bet < 20:
                bet = 20
            if bet > self.money:
                print("\nI regret to inform you cannot afford the bet. :(")
            else:
                self.bet = bet
                betting = False
    def scoring(self, p_value, d_value):

        if p_value == 21:
            print("\nPlayer gets black jack! Player win :D")
            self.winner = "p"
        elif d_value == 21:
            print("\nDealer gets black jack! Dealer win! :D")
            self.winner = "d"

        elif p_value> 21:
            print("\nPlayer went over 21...")
            self.winner = "d"
        elif d_value> 21:
            print("\nDealer went over 21...")
            self.winner = "p"

        else:
            if p_value > d_value:
                print("\nDealer gets "+str(d_value)+". You win :)")
                self.winner = "p"
            elif d_value > p_value:
                print("\nPlayer gets "+str(p_value)+ ". You loose.")
                self.winner = "d"
            else:
                print("\nThe game is a tie... :/")
                self.winner = "Tie"


    def payout(self):
        if self.winner == "p":
             self.money += self.bet
        elif self.winner == "d":
            self.money -= self.bet


    def display_money(self):
        print("\nCurrent game is: "+str(self.money) +".")

    def display_money_and_bet(self):
        print("\nCurrent game $: " + str(self.money) + "\t\t\t Current Bet: $"+str(self.bet))

print("Welcome in the Python Casino Black Jack")
print("We are pleased to inform you that minimum bet is equal to $20 :)")

money = input("\nHow much money would you like to place on te table? ")
game = Game(money)
playing = True

while playing:
    game_deck = Deck()
    game_deck.build_deck()
    game_deck.shuffle_deck()

    player = Player()
    dealer = Dealer()

    game.display_money()
    game.set_bet()

    player.draw_hand(game_deck)

    dealer.draw_hand(game_deck)

    game.display_money_and_bet()
    print("\nThe dealer is showing a "+str(dealer.hand[0].rank) + " of " + str(dealer.hand[0].suit) + ".")

    while player.playing_hand:
        player.display_hand()
        player.get_hand_value()
        player.update_hand(game_deck)

    dealer.hit(game_deck)
    dealer.display_hand()

    game.scoring(player.hand_value, dealer.hand_value)
    game.payout()

    if game.money < 20:
        playing = False
        print("\nYou run out of money! Go home and come back when you have the money stupid beach ;p")
