hidden = True

def setup():
    size(400, 400)

def chicken(x,y,s):
    ngon_kai(x,y,s)     
    head(x,y,s)    
    niang_kai(x,y,s)   
    pak_kai(x,y,s)          
    eye(x,y,s)       
    eye1(x,y,s)     
    cheek(x,y,s)     

def ngon_kai(x,y,s): 
    fill(235,60,60)
    ellipse(x-(s*0.18), y-(s*0.65), s*0.22, s*0.32)
    ellipse(x, y-(s*0.72), s*0.26, s*\0.38)
    ellipse(x+(s*0.18), y-(s*0.65), s*0.22, s*0.32)

def head(x,y,s):
    fill(255,245,180) 
    ellipse(x,y,s*1.6,s*1.4)

def niang_kai(x,y,s): 
    fill(235,60,60)
    ellipse(x-(s*0.07), y+(s*0.27), s*0.14, s*0.20)
    ellipse(x+(s*0.07), y+(s*0.27), s*0.14, s*0.20)

def pak_kai(x,y,s): 
    fill(255,140,0)
    triangle(x-(s*0.12), y+(s*0.06), 
             x+(s*0.12), y+(s*0.06), 
             x, y+(s*0.22))

def eye(x,y,s): # ta dam baew
    stroke(0)
    fill(40)
    ellipse(x-(s*0.3), y-(s*0.08), s*0.23, s*0.26)
    ellipse(x+(s*0.3), y-(s*0.08), s*0.23, s*0.26)

def eye1(x,y,s):
    fill(255)
    ellipse(x-(s*0.34), y-(s*0.13), s*0.09, s*0.09)
    ellipse(x+(s*0.26), y-(s*0.13), s*0.09, s*0.09)

def cheek(x,y,s): # kaem
    noStroke()
    fill(255, 182, 193, 180)
    ellipse(x-(s*0.48), y+(s*0.1), s*0.2, s*0.12)
    ellipse(x+(s*0.48), y+(s*0.1), s*0.2, s*0.12)

def chicken_card(x,y,s,h):
    stroke(0)
    fill(255) # si card
    rect(x-(s/2), y-(s*1.5)/2, s, s*1.5,12) # 12 kob
    
    if h:
        chicken(x, y, s/3)
    return "chicken"

def draw():
    background(255)
    chicken_card(width/2, height/2, 200, hidden)
