import unittest

from inner import *


class TestInner(unittest.TestCase):

    def testShow_card(self):
        card = [0]
        self.assertEqual(show_card(card), '♠A, ')

    def testCount(self):
        card = [7, 42]
        # ♠8 + ♣4
        self.assertEqual(count(card), 12)

    def testBlackJack(self):
        card = [0, 50]
        self.assertEqual(black(card), 'blackjack')


if __name__ == '__main__':
    unittest.main()




#inner 현재 구gui호환이라 함수 이름이 다름

marks = ['♠', '◆', '♥', '♣']
card_english = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

def show_card(card):
    card_list = ''
    for i in card:
        card_list += marks[i // 13] + card_english[i % 13] + ", "
    return card_list
    
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
    
#보드에 있던 조건을 함수로 구현
def black(player):
    black = 0

    for i in player:
        if i % 13 == 0:
            black += 1
        elif i % 13 >= 10:
            black += 2
        else:
            pass
    if black == 3:
        return 'blackjack'
