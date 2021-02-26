

class ScorePlayer(): 

    def __init__(self): 
        self.score = 0

    def increase_score(self,how_much_to_increase_score):
        self.score += how_much_to_increase_score 

    def get_score_like_string(self):
        return str(self.score)