import random

# 1~13까지 '♠', 14~26까지 '◆', 28~39까지 '♥', 40~52까지 '♣'
mark = ['♠', '◆', '♥', '♣']
card_english = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']


# 1~52 중 중복 없이 랜덤으로 20개를 뽑아 리스트를 반환
def set_card():
    return random.sample(range(1, 53), 20)


# 카드 합 반환
def count(card):
    result = 0
    count_a = 0
    for i in card:
        # J, Q, K는 10이고 나머지는 그대로 숫자를 더함
        if i % 13 >= 11 or i % 13 == 0:
            result += 10
        else:
            result += i % 13
            if i % 13 == 1:
                count_a += 1

    # A인 경우 11이 가능하기 때문에 21을 넘지 않으면 10을 더해줌
    for i in range(count_a):
        if result + 10 <= 21:
            result += 10
        else:
            break
    return result


# 카드 리스트를 숫자가 아닌 문양('♠', '◆', '♥', '♣')과 문자('A', 'J', 'Q', 'K')로 표현해서 String 으로 반환
def show_card(card):
    card_list = ''
    for i in card:
        card_list += mark[i // 13] + card_english[i % 13] + ", "
    return card_list
