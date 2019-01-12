from tkinter import *
import time
import random
tk=Tk()
tk.title('Bounce')
tk.resizable(0,0)
canvas=Canvas(tk,width=500,height=500,bd=0,bg='white')
canvas.pack()
global count
global speed
global speed1
speed=3
speed1=4
count=0
print('Ballspeed  score/count paddlespeed')
class Ball(object):
    
    def __init__(self,canvas,paddle,color):
        self.canvas=canvas
        self.paddle=paddle
        self.id=canvas.create_oval(10,10,25,25,fill=color)
        self.canvas.move(self.id,245,100)
        start=[-2,1,-1,3,-3]
        random.shuffle(start)
        self.x=start[0]
        self.y=-3
        self.hit_bottom=False
        #self.canvas_height=canvas.winfo_width()
    def hit_paddle(self,pos):
        pos_paddle=self.canvas.coords(self.paddle.id)
        if pos[2] >= pos_paddle[0] and pos[0] <=pos_paddle[2]:
            if pos[3] >= pos_paddle[1] and pos[3] <= pos_paddle[3]:
                global count
                global speed,speed1
                count+=1
                
                print(speed,'           ',count,'             ',speed1)
                if count % 2==0:
                    
                    speed+=2
                    speed1+=1
                return True
            return False
    
    
    
    def draw(self):
        self.canvas.move(self.id,self.x,self.y)
        pos=self.canvas.coords(self.id)
        global speed
        if pos[0]<= 0 :
            self.x=speed
        if pos[1]<=0:
            self.y=speed
        if pos[2]>=500 :
            self.x=-speed       
        if pos[3] >= 500:
            self.hit_bottom=True
            canvas.create_text(245,100,text='GAME OVER',font=16)
            canvas.create_text(245,120,text='SCORE : '+str(count),font=16)

        if self.hit_paddle(pos)==True:
            self.y=-speed
    
             
class Paddle(object):
    
    def __init__(self,canvas,color):
        self.canvas=canvas
        self.id=canvas.create_rectangle(0,0,100,10,fill=color)
        self.canvas.move(self.id,200,300)
        self.x=4
        self.y=0
        self.canvas.bind_all("<KeyPress-Left>",self.turn_left)
        self.canvas.bind_all("<KeyPress-Right>",self.turn_right)
    def draw(self):
        self.canvas.move(self.id,self.x,self.y)
        pos=self.canvas.coords(self.id)
        
        if pos[0]<=0 :
            self.x=0
        if pos[2]>=500 :
            self.x=0
       
    def turn_left(self,event):
        global speed1
        self.x=-speed1
    def turn_right(self,event):
        global speed1
        self.x=speed1

paddle=Paddle(canvas,'blue')        
ball=Ball(canvas,paddle,'red')

while 1:
    if ball.hit_bottom == False:
        ball.draw()
        paddle.draw()
        score=' '
        score=str(count)
    tk.update_idletasks()
    tk.update()
    time.sleep(0.05)
tk.mainloop()
