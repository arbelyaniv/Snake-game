from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.goto(0, 270)
        self.color("white")
        self.hideturtle()
        self.score = -1
        with open("/Users/yaniv/Desktop/New Projects/Snake/data.txt", mode="r") as file:
            self.high_score = int(file.read())
        self.plus()

    def plus(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score} High score: {self.high_score}", move=False, align='center', font=("Courier", 20, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("/Users/yaniv/Desktop/New Projects/Snake/data.txt", mode= "w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.plus()




