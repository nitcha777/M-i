hidden = True

def setup():
    size(400, 400)

def cat(x, y, s):
    ear_cat(x, y, s)       
    ear1_cat(x, y, s)    
    head_cat(x, y, s)     
    nuad_maew(x, y, s)       
    eye_cat(x, y, s)     
    eye1_cat(x, y, s)     
    nose_cat(x, y, s)     
    mouth_cat(x, y, s)    
    cheek_cat(x, y, s)     

def head_cat(x, y, s):
    fill(180) 
    ellipse(x, y, s*1.8, s*1.4)

def ear_cat(x, y, s): # huu dan nork
    fill(180)
    triangle(x-(s*0.75), y-(s*0.2),     #L
             x-(s*0.35), y-(s*0.65), 
             x-(s*0.75), y-(s*0.85))
    triangle(x+(s*0.75), y-(s*0.2),     #R
             x+(s*0.35), y-(s*0.65), 
             x+(s*0.75), y-(s*0.85))

def ear1_cat(x, y, s): # huu dan nai
    fill(255, 182, 193)
    triangle(x-(s*0.67), y-(s*0.28),    #L
             x-(s*0.38), y-(s*0.6), 
             x-(s*0.70), y-(s*0.78))
    triangle(x+(s*0.67), y-(s*0.28),    #R
             x+(s*0.38), y-(s*0.6), 
             x+(s*0.70), y-(s*0.78))

def nuad_maew(x, y, s):
    line(x-(s*0.4), y+(s*0.08), x-(s*0.85), y+(s*0.02))  #L
    line(x-(s*0.4), y+(s*0.16), x-(s*0.85), y+(s*0.16))
    line(x-(s*0.4), y+(s*0.24), x-(s*0.85), y+(s*0.30))
    
    line(x+(s*0.4), y+(s*0.08), x+(s*0.85), y+(s*0.02))  #R
    line(x+(s*0.4), y+(s*0.16), x+(s*0.85), y+(s*0.16))
    line(x+(s*0.4), y+(s*0.24), x+(s*0.85), y+(s*0.30))

def eye_cat(x, y, s): # ta dam
    fill(0)
    ellipse(x-(s*0.32), y-(s*0.08), s*0.25, s*0.28) #L
    ellipse(x+(s*0.32), y-(s*0.08), s*0.25, s*0.28) #R

def eye1_cat(x, y, s): # ta kow
    fill(255)
    ellipse(x-(s*0.36), y-(s*0.13), s*0.1, s*0.1)
    ellipse(x+(s*0.28), y-(s*0.13), s*0.1, s*0.1)

def nose_cat(x, y, s): 
    fill(255, 120, 150)
    ellipse(x, y+(s*0.06), s*0.12, s*0.08)

def mouth_cat(x, y, s): 
    line(x, y+(s/9), x , y+(s/4))
    line(x, y+(s/4), x-(s/9), y+(s/3))
    line(x, y+(s/4), x+(s/9), y+(s/3))

def cheek_cat(x, y, s): 
    noStroke()
    fill(255, 182, 193, 180)
    ellipse(x-(s*0.48), y+(s*0.1), s*0.2, s*0.12)
    ellipse(x+(s*0.48), y+(s*0.1), s*0.2, s*0.12)

def cat_card(x, y, s, h):
    stroke(0)
    fill(255) # si card
    rect(x-(s/2), y-(s*1.5)/2, s, s*1.5,12) # 12 kob
    
    if h:
        cat(x, y, s / 3)
    return "cat"

def draw():
    background(255)
    cat_card(width/2, height/2, 200, hidden)
