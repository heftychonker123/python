import pygame

class Player:
    def __init__(self, pos, screen):
        self.length = 1000
        self.posx = pos[0]
        self.posy = pos[1]
        self.all_pos = [pos]
        self.state = True
        self.display_size = screen.get_size()
        self.curr_direction = []

    def body_collision(self):
        return (self.posx, self.posy) in self.all_pos

    def screen_collide(self):
        return not (0 <= self.posx < self.display_size[0] - 15 and
                    0 <= self.posy < self.display_size[1] - 15)

    def direction(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.state = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    self.curr_direction = [(-1, 0)]
                elif event.key == pygame.K_s:
                    self.curr_direction = [(1, 0)]
                elif event.key == pygame.K_a:
                    self.curr_direction = [(0, -1)]
                elif event.key == pygame.K_d:
                    self.curr_direction = [(0, 1)]

    def move(self):
        for curr in self.curr_direction:
            self.posx += curr[1] * 60  # x is horizontal
            self.posy += curr[0] * 60  # y is vertical
            if not (self.body_collision() or self.screen_collide()):
                self.all_pos.append((self.posx, self.posy))
                if len(self.all_pos)>self.length:
                    self.all_pos.pop(0)
            else:
                self.state = False
class App:
    def run(self):
        pygame.init()
        screen = pygame.display.set_mode((1280, 720))
        clock = pygame.time.Clock()
        player = Player((640, 360), screen)

        while player.state:
            screen.fill("blue")
            player.direction()
            player.move()
            for i in player.all_pos:
                pygame.draw.rect(screen,"green", (i[0],i[1],60,60), width=0)
                pygame.draw.rect(screen,"black", (i[0],i[1],60,60), width=5)
            pygame.display.flip()
            clock.tick(10)
app = App()
app.run()
