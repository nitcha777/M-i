hidden = True

def setup():
    size(400,400)

def rabbit(x,y,s):
    ear(x,y,s)
    ear1(x,y,s)
    head(x,y,s)
    eye(x,y,s)
    eye1(x,y,s)
    nose(x,y,s)
    mouth(x,y,s)
    cheek(x,y,s)

def head(x,y,s):
    fill(255)
    ellipse(x, y, s*1.8, s*1.5)

def ear(x, y, s): #huu dan nork
    fill(255)
    ellipse(x-(s/3), y-(s/1.1), s/2.5,s*1.3)
    ellipse(x+(s/3), y-(s/1.1), s/2.5,s*1.3)

def ear1(x, y, s): #huu dan nai
    fill(255, 182, 193)
    ellipse(x-(s/3), y-(s/1.1), s/5,s)
    ellipse(x+(s/3), y-(s/1.1), s/5,s)

def eye(x, y, s): #ta dam
    fill(40)
    ellipse(x-(s/3), y-(s/6), s/4,s/4)
    ellipse(x+(s/3), y-(s/6), s/4,s/4)

def eye1(x, y, s): #ta dan nai
    fill(255)
    ellipse(x-(s/2.8), y-(s/4), s/10, s/10)
    ellipse(x+(s/3.3), y-(s/4), s/10, s/10)

def nose(x, y, s):
    fill(255, 120, 150)
    ellipse(x, y+(s/10), s/8, s/12) 

def mouth(x, y, s):
    noFill()
    line(x, y+(s/7), x , y+(s/4))
    line(x, y+(s/4), x-(s/10), y+(s/3))
    line(x, y+(s/4), x+(s/10), y+(s/3))

def cheek(x, y, s):
    fill(255, 182, 193)
    ellipse(x-(s/2), y+(s/8), s/4, s/6)
    ellipse(x+(s/2), y+(s/8), s/4, s/6)

def rabbit_card(x, y, s, h):
    noFill()
    fill(255) #si card
    rect(x-(s/2), y-(s * 1.5)/ 2, s, s * 1.5,12) # 12 kob
    
    if h:
        rabbit(x, y, s / 3)
    return "rabbit"

def draw():
    background(255)
    rabbit_card(width/2,height/2,200,hidden)
