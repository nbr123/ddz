import random

# 定义扑克牌
suits = ['♠', '♥', '♣', '♦']
ranks = ['3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A', '2']
deck = [rank + suit for rank in ranks for suit in suits] + ['小王', '大王']

# 洗牌
random.shuffle(deck)

# 发牌
player1 = deck[:17]
player2 = deck[17:34]
player3 = deck[34:51]
bottom_cards = deck[51:]

# 排序函数
def sort_hand(hand):
    order = {r: i for i, r in enumerate(ranks + ['小王', '大王'])}
    return sorted(hand, key=lambda card: order[card[:-1]] if card[:-1] in order else order[card])

# 排序玩家手牌
player1 = sort_hand(player1)
player2 = sort_hand(player2)
player3 = sort_hand(player3)

# 打印玩家手牌和底牌
print("玩家1的手牌:", player1)
print("玩家2的手牌:", player2)
print("玩家3的手牌:", player3)
print("底牌:", bottom_cards)

# 简单的出牌示例
def play_card(player_hand, card):
    if card in player_hand:
        player_hand.remove(card)
        print(f"出牌: {card}")
    else:
        print("无法出牌，手中没有这张牌")

# 玩家1出牌示例
play_card(player1, player1[0])
print("玩家1的手牌:", player1)

# ... 继续实现游戏逻辑，如叫地主、出牌规则等
