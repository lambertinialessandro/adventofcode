
'''
Your puzzle answer was 249356515.

Both parts of this puzzle are complete! They provide two gold stars: **
'''

import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from utils.read_file import read_file
from utils.test_solution import test_solution

@test_solution(name="DAY 07 PART 2", runs=100)
def main():
    print("\n### DAY 07 PART 2 ###")

    cards_list = {
        "A": 14, "K": 13, "Q": 12, "T": 11,
        "9": 10, "8": 9, "7": 8, "6": 7,
        "5": 6, "4": 5, "3": 4, "2": 3, "J": 2
        }
    a_val = cards_list["A"]
    j_val = cards_list["J"]

    content = read_file(os.path.join(os.path.dirname(__file__),"input.txt")).strip()
    if not content: return

    plays = []
    for line in content.split("\n"):
        [cards, bid] = line.split(" ")
        cards = [cards_list[symbol] for symbol in cards]

        score = 0
        unique_cards = list(set(cards))
        num_unique_cards = len(unique_cards)
        count_unique_cards = sorted(
            [{"symbol": symbol, "count": cards.count(symbol)} for symbol in unique_cards],
            key=lambda x: x["count"],
            reverse=True
        )

        if j_val in unique_cards:
            unique_cards.remove(j_val)
            num_unique_cards = num_unique_cards - 1

            if count_unique_cards[0]["symbol"] == j_val:
                count_unique_cards.pop(0)
            
            if num_unique_cards == 0:
                new_j_val = a_val
            elif num_unique_cards == 4:
                new_j_val = max(count_unique_cards, key=lambda x: x["symbol"])["symbol"]
            else:
                new_j_val = count_unique_cards[0]["symbol"]
                
            cards_replace_j = [new_j_val if x == j_val else x for x in cards]
            unique_cards = list(set(cards_replace_j))

            num_unique_cards = len(unique_cards)
            count_unique_cards = sorted(
                [{"symbol": symbol, "count": cards_replace_j.count(symbol)} for symbol in unique_cards],
                key=lambda x: x["count"],
                reverse=True
            )
        
        if num_unique_cards == 1:
            # Five of a kind
            score = 7
        elif num_unique_cards == 2:
            if count_unique_cards[0]["count"] == 4:
                # Four of a kind
                score = 6
            else:
                # Full house
                count_unique_cards = sorted(count_unique_cards[:2], key=lambda x: x["count"], reverse=True)
                score = 5

        elif num_unique_cards == 3:
            if count_unique_cards[0]["count"] == 3:
                # Three of a kind
                score = 4
            else:
                # Two pair
                count_unique_cards = sorted(count_unique_cards[:2], key=lambda x: x["symbol"], reverse=True)
                score = 3
        elif num_unique_cards == 4:
            # One pair
            score = 2
        else:
            # High card
            score = 1

        plays.append({"bid": int(bid), "score": score, "cards": cards})
    
    total_winnings = sum([
        (i+1) * play["bid"]
        for i, play in enumerate(
            sorted(plays, key=lambda x: (x["score"], x["cards"]))
    )])
    print(f"\n# SOLUTION: total winnings: {total_winnings}\n")

if __name__ == "__main__":
    main()
