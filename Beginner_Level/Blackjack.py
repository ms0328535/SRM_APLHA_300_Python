import random

class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + " of " + self.suit


class Deck:

    def __init__(self):
        suits = ["Spades", "Clubs", "Hearts", "Diamonds"]
        ranks = ["A", "2", "3", "4", "5", "6",
                 "7", "8", "9", "10", "J", "Q", "K"]

        self.cards = []

        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()


class Hand:

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)

        if card.rank == "A":
            self.aces += 1

        if card.rank in ["J", "Q", "K"]:
            self.value += 10
        elif card.rank == "A":
            self.value += 11
        else:
            self.value += int(card.rank)

        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


class Chips:

    def __init__(self):
        self.total = 100
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet


def take_bet(chips):

    while True:
        try:
            chips.bet = int(input("Enter your bet: "))

            if 0 < chips.bet <= chips.total:
                break

            print("Invalid bet!")

        except ValueError:
            print("Enter a valid number!")


def show_some(player, dealer):

    print("\nDealer's Cards:")
    print("<Hidden Card>")
    print(dealer.cards[1])

    print("\nPlayer's Cards:")

    for card in player.cards:
        print(card)

    print("Player Total:", player.value)


def show_all(player, dealer):

    print("\nDealer's Cards:")

    for card in dealer.cards:
        print(card)

    print("Dealer Total:", dealer.value)

    print("\nPlayer's Cards:")

    for card in player.cards:
        print(card)

    print("Player Total:", player.value)


def hit(deck, hand):

    hand.add_card(deck.deal())


def player_busts(chips):
    print("Player Bust! Dealer Wins.")
    chips.lose_bet()


def player_wins(chips):
    print("Player Wins!")
    chips.win_bet()


def dealer_busts(chips):
    print("Dealer Bust! Player Wins.")
    chips.win_bet()


def dealer_wins(chips):
    print("Dealer Wins!")
    chips.lose_bet()


def push():
    print("It's a Tie!")


def play_game():

    print("WELCOME TO BLACKJACK!")

    player_chips = Chips()

    playing = True

    while playing:

        print("\nAvailable Chips:", player_chips.total)

        if player_chips.total <= 0:
            print("You have no chips left!")
            break

        take_bet(player_chips)

        deck = Deck()
        deck.shuffle()

        player = Hand()
        dealer = Hand()

        # Initial two cards
        for i in range(2):
            player.add_card(deck.deal())
            dealer.add_card(deck.deal())

        show_some(player, dealer)

        # Player's turn
        while player.value < 21:

            choice = input("\nHit or Stand? (h/s): ").lower()

            if choice == "h":
                hit(deck, player)

                print("\nPlayer's Cards:")

                for card in player.cards:
                    print(card)

                print("Player Total:", player.value)

            elif choice == "s":
                print("Player Stands!")
                break

            else:
                print("Enter h or s!")

        # Check player result
        if player.value > 21:
            player_busts(player_chips)

        else:

            # Dealer's turn
            while dealer.value < 17:
                hit(deck, dealer)

            show_all(player, dealer)

            if dealer.value > 21:
                dealer_busts(player_chips)

            elif player.value > dealer.value:
                player_wins(player_chips)

            elif player.value < dealer.value:
                dealer_wins(player_chips)

            else:
                push()

        print("\nRemaining Chips:", player_chips.total)

        if player_chips.total <= 0:
            print("Game Over!")
            break

        again = input("\nPlay Again? (y/n): ").lower()

        if again != "y":
            playing = False

    print("\nTHANK YOU FOR PLAYING BLACKJACK!")


play_game()