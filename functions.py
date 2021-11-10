import random


mark = ['♠', '◆', '♥', '♣']
card_english = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']


def set_card():
    return random.sample(range(1, 53), 20)


def count(card):
    result = 0
    count_a = 0
    for i in card:
        if i % 13 >= 11 or i % 13 == 0:
            result += 10
        else:
            result += i % 13
            if i % 13 == 1:
                count_a += 1

    for i in range(count_a):
        if result + 10 <= 21:
            result += 10
        else:
            break
    return result


def show_card(card):
    card_list = ''
    for i in card:
        card_list += mark[i // 13] + card_english[i % 13] + ", "
    return card_list
