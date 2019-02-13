lottery_player_dict = {'name': 'Joel lol', 'numbers': (5, 9, 12, 3, 1, 21)}

class LotteryPlayer:
    def __init__(self, name):
        self.name = name
        self.numbers = (5, 9, 12, 3, 1, 21)
    
    def total(self):
        return sum(self.numbers)

player_one = LotteryPlayer('Joel')
player_one.numbers = (1, 2, 3, 4, 5)
player_two = LotteryPlayer('Atum')

