import pygame, sys, random

class App():
    screenX, screenY = 640, 480
    rectX, rectY = screenX / 2, screenY / 2
    foodRad = 10
    foodX, foodY = 0, screenY - (foodRad + 20) 
    rectH = rectW = 50
    mov = 10
    point = 0
    velocity=10




    def __init__(self):
        pygame.init()
        pygame.font.init()

        try:
            self.font = pygame.font.Font("font/arial.ttf", 20)
        except:
            self.font = pygame.font.Font("arial.ttf",20)

        self.screen = pygame.display.set_mode((self.screenX, self.screenY))
        self.spawnFood()

        self.drawRect()


    def drawRect(self):
        pygame.draw.rect(self.screen, (255, 255, 255), (self.rectX, self.rectY, self.rectW, self.rectH))

    def drawFood(self):
        pygame.draw.circle(self.screen, (0,255,0), (self.foodX + self.foodRad, self.foodY + self.foodRad) ,self.foodRad )


    def deleteOldScene(self):
        pygame.draw.rect(self.screen, (0,0,0),(0,0,self.screenX,self.screenY))


    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == 771:
                self.move(event)

    
    def spawnFood(self):
        self.foodX = random.randint(0,(self.screenX / 10) - (self.foodRad / 10)) * 10 



    def move(self,event):
        if event.text == "a" and self.rectX > 0:
            self.rectX -= self.mov
        if event.text == "d" and self.rectX < self.screenX - self.rectW:
            self.rectX += self.mov
        
        self.refresh()


    def updateText(self):
        text = self.font.render( "Point: " + str(self.point), False, (255,255,255))
        self.screen.blit(text, (0,0))



    def refresh(self):
        self.deleteOldScene()
        self.drawFood()
        self.drawRect()
        self.updateText()
        pygame.display.update()

    def update(self):
        self.event()

        pygame.time.delay(30)
        if self.rectY < self.screenY - self.rectW:
            self.rectY += self.velocity
            self.refresh()
        

        if self.rectX + self.rectH - 10 == self.foodX or self.rectX - self.rectH + 40 == self.foodX:
            self.spawnFood()
            self.point += 1



        self.refresh()


app = App()

while True:
    app.update()
    