from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 20, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0

        with open("data.txt", 'r') as file:
            self.high_score = int(file.read())

        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.color('white')
        self.speed("fastest")
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)
    
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", 'w') as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update_score()

    # def game_over(self):
    #     self.clear()
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER, Your final score is: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()
