deck_of_cards = input().split(" ")
number_of_shuffles = int(input())
for shuffle in range(number_of_shuffles):
    final_deck = []
    middle_deck = len(deck_of_cards) // 2  # result in int
    left_part = deck_of_cards[0:middle_deck]
    right_part = deck_of_cards[middle_deck::]

    for index in range(len(left_part)): #could be right_part, there´s no diff
        final_deck.append(left_part[index])
        final_deck.append(right_part[index])

    deck_of_cards = final_deck
print(final_deck)
