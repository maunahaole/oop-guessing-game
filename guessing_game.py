class GuessingGame():

    def __init__(self, answer_num):
        self.answer = answer_num
        self.is_solved = False
        
    def guess(self, guess):
        if guess < self.answer:
            return "low"
        if guess > self.answer:
            return "high"
        if guess == self.answer:
            self.is_solved = True
            return "correct"
        
    def solved(self):
        return self.is_solved
     
game_1 = GuessingGame(10)
   
print(game_1.solved())
print(game_1.guess(5))
print(game_1.guess(20))
print(game_1.solved())
print(game_1.guess(10))
print(game_1.solved())

game_2 = GuessingGame(50)

print(game_2.solved())
print(game_2.guess(20))
print(game_2.guess(100))
print(game_2.solved())
print(game_2.guess(50))
print(game_2.solved())
