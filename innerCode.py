import random

marks = ['spades', 'diamonds', 'hearts', 'clubs']
card_english = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']


# 파일 입출력
def load():
    try:
        f = open("money.dat", 'r')
        return int(f.readline())
    except FileNotFoundError:
        f = open("money.dat", 'w')
        f.write('100000')
        return 100000


def write(money):
    f = open("money.dat", 'w')
    f.write(money)
    f.close()


def set_money(now, betting, num):
    # lose : 0
    if num == 0 or num == 4:
        write(str(now - betting))
        return now - betting
    # win : 1
    elif num == 1:
        write(str(now + betting))
        return now + betting
    # Black jack : 3
    elif num == 3:
        write(str(int(now + (1.5 * betting))))
        return int(now + (betting * 1.5))
    else:
        return now


# 카드 두장(베팅 시 카드 지급)지급후에 카드뭉치에서 제거
def twocard(card):
    cardList = []
    for i in range(2):
        cardList.append(card.pop(0))
    return cardList


# 새로운 카드 받기
def cardappend(cardlist, card):
    cardlist.append(card.pop(0))


# end 버튼 클릭 이벤트, Lose: 0 Win: 1 Draw 2
def fight(player_result, dealer_result):
    if player_result > dealer_result or dealer_result > 21:
        return 1
    elif player_result < dealer_result or dealer_result == 21:
        return 0
    if player_result == dealer_result:
        return 2


def burst(result):
    if result > 21:
        return 4
    elif result == 21:
        return 3
    else:
        return 5  # nothing, draw


def set_card():
    return random.sample(range(52), 17)


def count(card):
    result = 0
    cnt = 0
    for data in card:
        if data % 13 >= 10:
            result += 10
        else:
            result += data % 13 + 1
            # if data == A
            if data % 13 == 0:
                cnt += 1

    for _ in range(cnt):
        # A : 1 or 11
        if result + 10 <= 21:
            result += 10
        else:
            break

    return result


def intToString_card(card):
    card_list = []
    for data in card:
        card = str(marks[data//13]) + str(card_english[data % 13])
        card_list.append(card)
    return card_list
