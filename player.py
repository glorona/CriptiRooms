import pygame, os

class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.movex = 0
        self.movey = 0
        self.sprites = []
        self.current_sprite = 0
        for i in range(1, 21):
            img = pygame.image.load(os.path.join('ImagesDiscretas', 'hero' + str(i) + '.png'))
            imgScale = pygame.transform.scale(img,(32,40))
            self.sprites.append(imgScale)
            imgScale.convert_alpha()  # optimise alpha
            imgScale.set_colorkey((0,0,0))  # set alpha

        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

    def control(self, x, y):
        self.movex += x
        self.movey += y

    def checkCollision(self, obstacles, x, y):
        for obstacle in obstacles:
            if obstacle.colliderect(self.rect.x, self.rect.y + y, self.rect.width, self.rect.height):
                self.update(0,-y*2)
                return True
            if obstacle.colliderect(self.rect.x, self.rect.y - y, self.rect.width, self.rect.height):
                self.update(0,y*2)
                return True
            if obstacle.colliderect(self.rect.x + x, self.rect.y, self.rect.width, self.rect.height):
                self.update(-x*2,0)
                return True
            if obstacle.colliderect(self.rect.x - x, self.rect.y, self.rect.width, self.rect.height):
                self.update(x*2,0)
                return True
        return False


    def update(self,stepsx,stepsy):
        self.rect.x = self.rect.x + stepsx
        self.rect.y = self.rect.y + stepsy

        if stepsx < 0:
            self.current_sprite = 6
            self.current_sprite += 0.01
            if self.current_sprite >= 8:
                self.current_sprite = 6
            self.image = self.sprites[int(self.current_sprite)]

        # moving right
        if stepsx > 0:
            self.current_sprite = 18
            self.current_sprite += 0.01
            if self.current_sprite >= 20:
                self.current_sprite = 18
            self.image = self.sprites[int(self.current_sprite)]

        # moving up
        if stepsy > 0:
            self.current_sprite = 9
            self.current_sprite += 0.01
            if self.current_sprite >= 11:
                self.current_sprite = 9
            self.image = self.sprites[int(self.current_sprite)]

        # moving down
        if stepsy < 0:
            self.current_sprite = 3
            self.current_sprite += 0.01
            if self.current_sprite >= 5:
                self.current_sprite = 3
            self.image = self.sprites[int(self.current_sprite)]

    