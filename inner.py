import random


marks = ['♠', '◆', '♥', '♣']
card_english = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']


# 파일 입출력
def load():
    try:
        f = open("money.dat", 'r')
        return int(f.readline())
    except:
        f = open("money.dat", 'w')
        f.write('100000')
        return 100000


def write(money):
    f = open("money.dat", 'w')
    f.write(money)
    f.close()


def set_money(now, betting, num):
    if num == 0:
        write(str(now - betting))
        return now - betting
    elif num == 1:
        write(str(now + betting))
        return now + betting
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
    if player_result > 21:
        return 0
    elif dealer_result > 21:
        return 1
    else:
        if player_result == dealer_result:
            return 2
        elif player_result < dealer_result:
            return 0
        elif player_result > dealer_result:
            return 1


def get_fight_text(num):
    if num == 0:
        return "Lose"
    elif num == 1:
        return "Win"
    elif num == 3:
        return "Black Jack!!"
    else:
        return "Draw"


def set_card():
    return random.sample(range(52), 17)


def count(card):
    result = 0
    count_a = 0
    for i in card:
        if i % 13 >= 10:
            result += 10
        else:
            result += i % 13 + 1
            if i % 13 == 0:
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
        card_list += marks[i // 13] + card_english[i % 13] + ", "
    return card_list


def dealer_algo(result, who, card):
    while result <= 16:
        cardappend(who, card)
        if count(who) > 16:
            break


