#!/usr/bin/python

# By Yongzhao Yang 2022.01.25

CARDS = ["2","3","4","5","6","7","8","9","T","J","Q","K","A"]


def main():
    # catch user inputs from cmd line
    try:
        # get arguments
        firsthand = str(sys.argv[1])
        secondhand = str(sys.argv[2])
    except:
        print("Error: Input format: <First Hand> <Second Hand> ")
        raise

    # convert string to char list
    firsthand = list(firsthand)
    secondhand = list(secondhand)
    total = firsthand + secondhand
    if max([total.count(item) for item in total]) > 4 or len(firsthand) != 5 or len(secondhand) != 5 :
        sys.exit("Oops, Hands are incorrect, Exit!")
    else:
        print("Hands are correct, Continue...")

    # remove duplicate char from a list
    first = list(set(firsthand))
    second = list(set(secondhand))

    # count char from a list
    num_first = [firsthand.count(item) for item in first]
    num_second = [secondhand.count(item) for item in second]

    # save char and count into one dict
    first_pair = {item:num_first[first.index(item)] for item in first}
    second_pair = {item: num_second[second.index(item)] for item in second}

    # get ranking
    first_ranks, first_cards = ranking(first_pair)
    second_ranks, second_cards = ranking(second_pair)

    # get output
    # if ranking is high
    if sum(first_ranks) > sum(second_ranks):
        print("First hand wins!")
    elif sum(first_ranks) == sum(second_ranks):
        if CARDS.index(first[num_first.index(max(num_first))]) > CARDS.index(second[num_second.index(max(num_second))]):
            print("- First hand wins!")
        elif CARDS.index(first[num_first.index(max(num_first))]) == CARDS.index(second[num_second.index(max(num_second))]):
            first_cards.remove(first_cards[num_first.index(max(num_first))])
            second_cards.remove(second_cards[num_second.index(max(num_second))])
            if sum(first_cards) > sum(second_cards):
                print("- First hand wins!")
            elif sum(first_cards) == sum(second_cards):
                print("It’s a tie!")
            else:
                print("- Second hand wins!")
        else:
            print("- Second hand wins!")
    else:
        print("Second hand wins!")


def ranking(x):
    # x: a dict
    keys = list(x)
    values = list(x.values())
    rank_definition = {'4': 2000, '3': 1000, '2': 200, '1': 1}
    ranks = list(rank_definition[str(item)] for item in values)
    cards_ranks = [CARDS.index(item)+1 for item in keys]
    return ranks, cards_ranks

if __name__ == '__main__':
    import sys, re, os
    from operator import mul
    main()


