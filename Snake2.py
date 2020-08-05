from tkinter import*
import random
import os

root = Tk()
canvas = Canvas(root, bg="black", height=401,width=401)
canvas.pack()

class Block():
    def __init__(self,x,y,color):
        self.x = x
        self.y = y
        self.color = color
        self.rect = canvas.create_rectangle(self.x,self.y,self.x+20,self.y+20,fill=color)

    def update(self):
        canvas.delete(self.rect)
        self.rect = canvas.create_rectangle(self.x,self.y,self.x+20,self.y+20,fill=self.color)

class Snake():

    def __init__(self,x,y,xs,ys):
        b = Block(x,y,"green2")
        self.xspeed = xs
        self.yspeed = ys
        self.blocks = []
        self.blocks.append(b)

    def move(self):
        for i,e in reversed(list(enumerate(self.blocks))):
            if(i == 0):
                self.blocks[i].x += 20*self.xspeed
                self.blocks[i].y += 20*self.yspeed
            else:
                self.blocks[i].x = self.blocks[i-1].x
                self.blocks[i].y = self.blocks[i-1].y

            self.blocks[i].update()


        if(self.blocks[0].x > 380 or self.blocks[0].y > 380 or
            self.blocks[0].x < 0 or self.blocks[0].y < 0):
            os.execl(sys.executable, sys.executable, *sys.argv)
        for i in range(len(self.blocks)-1):
            head = self.blocks[0]
            if(head.x == self.blocks[i+1].x and head.y == self.blocks[i+1].y):
                os.execl(sys.executable, sys.executable, *sys.argv)


    def key_pressed(self,event):
        if(event.char == 'a'):
            self.xspeed = -1
            self.yspeed = 0
        elif(event.char == 's'):
            self.xspeed = 0
            self.yspeed = 1
        elif(event.char == 'd'):
            self.xspeed = 1
            self.yspeed = 0
        elif(event.char == 'w'):
            self.xspeed = 0
            self.yspeed = -1
        elif(event.char == 'p'):
            root.destroy

    def grow(self):
        self.blocks.insert(1,Block(self.blocks[0].x,self.blocks[0].y,"green2"))

x,y = random.randint(0,19)*20,random.randint(0,19)*20
s = Snake(x,y,0,0)
x1,y1 = random.randint(0,19)*20,random.randint(0,19)*20
food = Block(x1,y1,"orange red")

def draw_window():
    for i in range(21):
        canvas.create_line(0+20*i, 0, 0+20*i, 401, fill="white")
        canvas.create_line(0, 20*i, 401, 0+20*i, fill="white")

def clock():
    s.move()
    if(s.blocks[0].x == food.x and s.blocks[0].y == food.y):
        x,y = random.randint(0,19)*20,random.randint(0,19)*20
        for i in range(len(s.blocks)):
            while(s.blocks[i].x == x and s.blocks[i].y == y):
                x,y = random.randint(0,19)*20,random.randint(0,19)*20
        food.x,food.y = x,y
        food.update()
        for i in range(3):
            s.grow()
    draw_window()
    root.after(150, clock)


root.bind("<Key>",s.key_pressed)
clock()
mainloop()
