class GameStats():
    #Остлеживание статистики для игры
    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = False
        with open('record.txt') as f_o:
            high_score1 = f_o.read()
        self.high_score = int(high_score1)


    def reset_stats(self):
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 0