import random

colors = ['Red', 'Green', 'Blue', 'Yellow']
values = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'Skip', 'Reverse', '+2']
wilds = ['Wild', 'Wild +4']


def draw_card(card):
    color, value = card
    card_lines = [
        " --------- ",
        f"|{color[0]:<9}|",
        "|         |",
        f"|   {value:<5}|",
        "|         |",
        f"|{color[0]:>9}|",
        " --------- "
    ]
    return "\n".join(card_lines)

def create_deck():
    deck = []
    for color in colors:
        for value in values:
            deck.append((color, value))
            if value != '0':  
                deck.append((color, value))
    for _ in range(4):
        for wild in wilds:
            deck.append(('Wild', wild))
    random.shuffle(deck)
    return deck

def show_hand(hand):
    for idx, card in enumerate(hand):
        print(f"Card {idx + 1}:")
        print(draw_card(card))
        print()

def valid_play(card, top_card):
    return card[0] == top_card[0] or card[1] == top_card[1] or card[0] == 'Wild'

def savage_win_message():
    print("\n💀💀💀 Savage Mode Activated 💀💀💀")
    print("You just UNO-REKT your opponent. Better luck next time, loser 😎🔥")
    print("Game Over.\n")

def uno_game():
    deck = create_deck()
    player_hand = [deck.pop() for _ in range(7)]
    bot_hand = [deck.pop() for _ in range(7)]
    discard_pile = [deck.pop()]

    turn = 0  

    while True:
        print(f"\nTop Card on Discard Pile:\n{draw_card(discard_pile[-1])}\n")

        if turn == 0:
            print("Your Turn 🔥")
            show_hand(player_hand)
            playable = [card for card in player_hand if valid_play(card, discard_pile[-1])]
            if playable:
                print("Playable Cards:")
                for i, card in enumerate(playable):
                    print(f"{i + 1}: {card}")
                choice = int(input("Choose card number to play or 0 to draw: "))
                if choice == 0:
                    drawn = deck.pop()
                    player_hand.append(drawn)
                    print("\nYou drew:")
                    print(draw_card(drawn))
                else:
                    selected = playable[choice - 1]
                    player_hand.remove(selected)
                    discard_pile.append(selected)
            else:
                print("No valid moves. You draw a card.")
                player_hand.append(deck.pop())
            if not player_hand:
                savage_win_message()
                break
            turn = 1
        else:
            print("Bot's Turn 🤖")
            bot_played = False
            for card in bot_hand:
                if valid_play(card, discard_pile[-1]):
                    print(f"Bot played:\n{draw_card(card)}")
                    bot_hand.remove(card)
                    discard_pile.append(card)
                    bot_played = True
                    break
            if not bot_played:
                print("Bot had no valid moves and drew a card.")
                bot_hand.append(deck.pop())
            if not bot_hand:
                print("\nBot Won! You got schooled by AI 🤖💀\n")
                break
            turn = 0

if __name__ == "__main__":
    uno_game()
