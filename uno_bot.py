import random

colors = ['Red', 'Green', 'Blue', 'Yellow']
values = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'Skip', 'Reverse', '+2']
wilds = ['Wild', 'Wild +4']

def draw_card(card):
    color, value = card
    if color == 'Wild':
        card_lines = [
            " --------- ",
            f"|{'WILD':^9}|",
            "|         |",
            f"|{value:^9}|",
            "|         |",
            f"|{'WILD':^9}|",
            " --------- "
        ]
    else:
        card_lines = [
            " --------- ",
            f"|{color[0]:<9}|",
            "|         |",
            f"|{value:^9}|",
            "|         |",
            f"|{color[0]:>9}|",
            " --------- "
        ]
    return card_lines

def create_deck():
    deck = [(color, value) for color in colors for value in values]
    deck += [(color, value) for color in colors for value in values if value != '0']
    deck += [('Wild', wild) for wild in wilds for _ in range(4)]
    random.shuffle(deck)
    return deck

def show_hand(hand):
    all_lines = ['' for _ in range(7)]
    for card in hand:
        card_lines = draw_card(card)
        for i in range(7):
            all_lines[i] += card_lines[i] + '  '
    for line in all_lines:
        print(line)

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
        print(f"\nTop Card on Discard Pile:\n" + "\n".join(draw_card(discard_pile[-1])) + "\n")

        if turn == 0:
            print("Your Turn 🔥")
            show_hand(player_hand)
            playable = [card for card in player_hand if valid_play(card, discard_pile[-1])]
            if playable:
                print("Playable Cards:")
                for i, card in enumerate(playable):
                    print(f"{i + 1}: {card}")

                try:
                    choice = int(input("Choose card number to play or 0 to draw: "))
                except ValueError:
                    choice = 0

                if choice == 0:
                    if deck:
                        drawn = deck.pop()
                        player_hand.append(drawn)
                        print("\nYou drew:")
                        print("\n".join(draw_card(drawn)))
                    else:
                        print("Deck is empty. No card drawn.")
                elif 1 <= choice <= len(playable):
                    selected = playable[choice - 1]
                    player_hand.remove(selected)
                    discard_pile.append(selected)
                else:
                    print("Invalid choice. You lose your turn.")
            else:
                if deck:
                    print("No valid moves. You draw a card.")
                    player_hand.append(deck.pop())
                else:
                    print("No valid moves and deck is empty.")

            if not player_hand:
                savage_win_message()
                break
            turn = 1

        else:
            print("Bot's Turn 🤖")
            bot_played = False
            for card in bot_hand:
                if valid_play(card, discard_pile[-1]):
                    print(f"Bot played:\n" + "\n".join(draw_card(card)))
                    bot_hand.remove(card)
                    discard_pile.append(card)
                    bot_played = True
                    break
            if not bot_played:
                if deck:
                    print("Bot had no valid moves and drew a card.")
                    bot_hand.append(deck.pop())
                else:
                    print("Bot had no valid moves and the deck is empty.")

            if not bot_hand:
                print("\nBot Won! You got schooled by AI 🤖💀\n")
                break
            turn = 0

if __name__ == "__main__":
    uno_game()
