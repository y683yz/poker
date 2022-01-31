#!/usr/bin/python
# By Yongzhao Yang 2022.01.25

CARDS = ["2","3","4","5","6","7","8","9","T","J","Q","K","A"]


def main():
    # catch user inputs from cmd line
    try:
        # get arguments
        firsthand = str(sys.argv[1])
        secondhand = str(sys.argv[2])
    except ValueError:
        print ("Error: Using unsupported characters")
        print("Input format: <First Hand> <Second Hand> ")

    finally:
        print("Good, Input correctly")


    # convert string to char list
    firsthand = list(firsthand)
    secondhand = list(secondhand)
    total = firsthand + secondhand
    if max([total.count(item) for item in total]) > 4 and len(firsthand) > 5 and len(secondhand) > 5:
        sys.exit("Oops, Hands are incorrect, Exit!")
    else:
        print("Hands parsing is correct, Continue...")

    # remove duplicate char from a list
    first = list(set(firsthand))
    second = list(set(secondhand))

    # count char from a list
    num_first = [firsthand.count(item) for item in first]
    num_second = [secondhand.count(item) for item in second]

    # save char and count into one dict
    first_pair = {item:num_first[first.index(item)] for item in first}
    second_pair = {item: num_second[second.index(item)] for item in second}

    # get hands ranking
    first_ranks, first_cards = hand_ranking(first_pair)
    second_ranks, second_cards = hand_ranking(second_pair)

    # get output --->>
    if sum(second_ranks) > 5000:     # four of a kind
        if sum(first_ranks) > 5000:
            if max(first_ranks) < max(second_ranks):
                print("A1-Second hand wins!")
            else:
                print("A1-First hand wins!")
        else:       # except four of a kind
            print("A2-Second hand wins!")

    elif sum(second_ranks) in range(2501, 3050):    # full house
        if sum(first_ranks) in range(2501, 3050):    # full house
            if max(first_ranks) < max(second_ranks):
                print("B1-Second hand wins!")
            else:
                print("B1-First hand wins!")
        elif sum(first_ranks) > 5000:        # four of a kind
            print("B2-First hand wins!")
        else:                               # < full house
            print("B3-Second hand wins!")

    elif sum(second_ranks) in range(2001, 2050):    # triple
        if sum(first_ranks) in range(2001, 2050):    # triple
            if max(first_ranks) < max(second_ranks):
                print("C1-Second hand wins!")
            else:
                print("C1-First hand wins!")
        elif sum(first_ranks) in range(1, 1050):    # two pairs
            print("C3-Second hand wins!")
        elif sum(first_ranks) in range(2001, 5050):    # full house, four of a kind
            print("C4-First hand wins!")
        else:                       # two pairs, pair, highest card
            print("C5-First hand wins!")

    elif sum(second_ranks) in range(1007, 1038):    # two pairs
        if sum(first_ranks) in range(1007, 1038):    # two pairs
            if max(first_ranks) < max(second_ranks):
                print("D1-Second hand wins!")
            elif max(first_ranks) == max(second_ranks): # first pair
                # remove max ranking
                first_ranks.remove(first_ranks[first_ranks.index(max(first_ranks))])
                second_ranks.remove(second_ranks[second_ranks.index(max(second_ranks))])
                if max(first_ranks) == max(second_ranks):   # second pair
                    # remove max ranking
                    first_ranks.remove(first_ranks[first_ranks.index(max(first_ranks))])
                    second_ranks.remove(second_ranks[second_ranks.index(max(second_ranks))])
                    if max(first_ranks) < max(second_ranks):    # highest card
                        print("D2-Second hand wins!")
                    elif max(first_ranks) == max(second_ranks):
                        print("D2-It's a tie!")
                    elif max(first_ranks) > max(second_ranks):
                        print("D2-First hand wins!")
            else:
                print("D1-First hand wins!")
        elif sum(first_ranks) > 1038:  # full house, four of a kind. triple
            print("D3-First hand wins!")
        else:           # pair, highest card
            print("D3-Second hand wins!")

    elif sum(second_ranks) in range(501, 550):    # pair
        if sum(first_ranks) in range(501, 550):    # pair
            if max(first_ranks) < max(second_ranks):
                print("E1-Second hand wins!")
            else:
                print("E1-First hand wins!")
            if max(first_ranks) == max(second_ranks):
                # remove max ranking
                first_ranks.remove(first_ranks[first_ranks.index(max(first_ranks))])
                second_ranks.remove(second_ranks[second_ranks.index(max(second_ranks))])
                # remove same item in two ranks
                same_items = list(set(first_ranks).intersection(set(second_ranks)))
                first_ranks = list(set(first_ranks) - set(same_items))
                second_ranks = list(set(second_ranks) - set(same_items))
                if max(first_ranks) < max(second_ranks):
                    print("E2-Second hand wins!")
                else:
                    print("E2-First hand wins!")
        elif sum(first_ranks) > 1007:  # full house, four of a kind. triple, two pairs
            print("E3-First hand wins!")
        elif sum(first_ranks) < 60:  # highest cards
            print("E3-Second hand wins!")

    elif sum(second_ranks) < 60:  # highest cards
        if sum(first_ranks) < 60:
            # remove same item in two ranks
            same_items = list(set(first_ranks).intersection(set(second_ranks)))
            first_ranks = list(set(first_ranks)-set(same_items))
            second_ranks = list(set(second_ranks) - set(same_items))
            if first_ranks == [] and second_ranks == []:
                print("F1-It's a tie!")
            elif max(first_ranks) < max(second_ranks):  # highest cards
                print("F1-Second hand wins!")
            elif max(first_ranks) == max(second_ranks):
                print("F1-It's a tie!")
            elif max(first_ranks) > max(second_ranks):
                print("F1-First hand wins!")
        if sum(first_ranks) > 61:  # full house, four of a kind. triple, two pairs, pair
            print("F2-First hand wins!")


def hand_ranking(x):
    # x: a dict
    keys = list(x)
    values = list(x.values())
    rank_definition = {'4': 5000, '3': 2000, '2': 500, '1': 1}
    ranks = list(rank_definition[str(item)] for item in values)
    cards_ranks = [CARDS.index(item)+1 for item in keys]
    # final_rank = [*map(mul,ranks,cards_ranks)]
    final_rank = [a + b for a, b in zip(ranks, cards_ranks)]
    return final_rank, cards_ranks


if __name__ == '__main__':
    import sys
    main()


