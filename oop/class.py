class BKQ_ear:
    def __init__(self):
        self.rightear=None
        self.leftear=1
    def return_state(self,direction):
        if direction=="Right":
            return self.rightear
        if direction=="Left":
            return self.leftear
        else:
            return "Please enter a valid direction"
j=BKQ_ear()
t=j.return_state(input())
while t=="Please enter a valid direction":
    t=j.return_state(input())
print(t)