#!/usr/bin/python
# By Yongzhao Yang 2022.01.25

CARDS = ["2","3","4","5","6","7","8","9","T","J","Q","K","A"]


def main():
    # catch user inputs from cmd line
    try:
        # get arguments
        firsthand = str(sys.argv[1])
        secondhand = str(sys.argv[2])
    finally:
        print("Error: Input format: <First Hand> <Second Hand> ")

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

    # get hands ranking
    first_ranks, first_cards = ranking(first_pair)
    second_ranks, second_cards = ranking(second_pair)

    # get output --->>
    if max(first_ranks) > max(second_ranks):
        print("First hand wins!")
    elif max(first_ranks) < max(second_ranks):
        print("Second hand wins!")
    else:
        # remove max ranking
        first_ranks.remove(first_ranks[first_ranks.index(max(first_ranks))])
        second_ranks.remove(second_ranks[second_ranks.index(max(second_ranks))])
        if max(first_ranks) == max(second_ranks):
            # remove max ranking
            first_ranks.remove(first_ranks[first_ranks.index(max(first_ranks))])
            second_ranks.remove(second_ranks[second_ranks.index(max(second_ranks))])
            if max(first_ranks) > max(second_ranks):
                print("First hand wins!")
            elif max(first_ranks) == max(second_ranks):
                print("It’s a tie!")
            else:
                print("Second hand wins!")
        elif max(first_ranks) > max(second_ranks):
            print("First hand wins!")
        else:
            print("Second hand wins!")


def ranking(x):
    # x: a dict
    keys = list(x)
    values = list(x.values())
    rank_definition = {'4': 3000, '3': 2000, '2': 1000, '1': 1}
    ranks = list(rank_definition[str(item)] for item in values)
    cards_ranks = [CARDS.index(item)+1 for item in keys]
    # final_rank = [*map(mul,ranks,cards_ranks)]
    final_rank = [a + b for a, b in zip(ranks, cards_ranks)]
    return final_rank, cards_ranks


if __name__ == '__main__':
    import sys, re, os
    main()


