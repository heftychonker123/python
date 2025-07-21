import random
class Player:
    def __init__(self):
        self.name=None
        self.answer=None
class Game:
    def __init__(self):
        self.secretnum=random.randint(1,1000)
        self.attempt=0
    def run(self):
        player=Player()
        player.name=input()
        while True:
            player.answer=input()
            try:
                answer=int(player.answer)
                if answer==self.secretnum:
                    break
                elif answer<self.secretnum:
                    print("The answer is larger")
                    self.attempt+=1
                else:
                    print("The answer is smaller")
                    self.attempt+=1
            except:
                print("PLease enter a valid interger from 1-1000")
        print(self.attempt)
game=Game()
game.run()