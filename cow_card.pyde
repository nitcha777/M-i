hidden = True

def setup():
    size(400, 400)

def cow(x, y, s):
    khao_wua(x, y, s)    
    ear_cow(x, y, s)
    ear1_cow(x, y, s)      
    head_cow(x, y, s)      
    spot_cow(x, y, s)     
    snout_cow(x, y, s)    
    nose_cow(x, y, s)      
    eye2_cow(x, y, s)     
    eye_cow(x, y, s)       
    eye1_cow(x, y, s)      
    cheek_cow(x, y, s)    

def khao_wua(x, y, s): 
    fill(240, 200, 120)
    ellipse(x - (s * 0.38), y - (s * 0.52), s * 0.24, s * 0.38)
    ellipse(x + (s * 0.38), y - (s * 0.52), s * 0.2, s * 0.38)

def ear_cow(x, y, s): # huu dan nork
    stroke(0)
    fill(255)
    ellipse(x - (s * 0.65), y - (s * 0.22), s * 0.45, s * 0.25)
    ellipse(x + (s * 0.65), y - (s * 0.22), s * 0.45, s * 0.25)

def ear1_cow(x, y, s): # huu dan nai
    stroke(0)
    fill(255, 182, 193)
    ellipse(x - (s * 0.65), y - (s * 0.22), s * 0.28, s * 0.15)
    ellipse(x + (s * 0.65), y - (s * 0.22), s * 0.28, s * 0.15)

def head_cow(x, y, s): # hua wua
    stroke(0)
    fill(255)
    ellipse(x, y, s * 1.6, s * 1.4)

def spot_cow(x, y, s): # lai wua
    noStroke()
    fill(40)
    ellipse(x - (s * 0.38), y - (s * 0.2), s * 0.45, s * 0.45)

def snout_cow(x, y, s): # pak yuen
    stroke(0)
    fill(255, 190, 200)
    ellipse(x, y + (s * 0.18), s * 0.75, s * 0.42)

def nose_cow(x, y, s): # ru jamuk
    stroke(0)
    fill(40)
    ellipse(x - (s * 0.12), y + (s * 0.14), s * 0.08, s * 0.12)
    ellipse(x + (s * 0.12), y + (s * 0.14), s * 0.08, s * 0.12)


def eye2_cow(x, y, s): # ta kow
    stroke(0)
    fill(255)
    ellipse(x - (s * 0.3), y - (s * 0.08), s * 0.3, s * 0.33)
    ellipse(x + (s * 0.3), y - (s * 0.08), s * 0.3, s * 0.33)

def eye_cow(x, y, s): # ta dam baew
    stroke(0)
    fill(40)
    ellipse(x - (s * 0.3), y - (s * 0.08), s * 0.23, s * 0.26)
    ellipse(x + (s * 0.3), y - (s * 0.08), s * 0.23, s * 0.26)

def eye1_cow(x, y, s): # pra kai ta
    noStroke()
    fill(255)
    ellipse(x - (s * 0.34), y - (s * 0.13), s * 0.09, s * 0.09)
    ellipse(x + (s * 0.26), y - (s * 0.13), s * 0.09, s * 0.09)

def cheek_cow(x, y, s): # kaem
    noStroke()
    fill(255, 182, 193, 180)
    ellipse(x - (s * 0.48), y + (s * 0.05), s * 0.2, s * 0.12)
    ellipse(x + (s * 0.48), y + (s * 0.05), s * 0.2, s * 0.12)

def cow_card(x, y, s, h):
    stroke(0)
    fill(255) # si card
    rect(x - (s / 2), y - (s * 1.5) / 2, s, s * 1.5, 12) # 12 kob
    
    if h:
        cow(x, y, s / 3)
    return "cow"

def draw():
    background(255)
    cow_card(width / 2, height / 2, 200, hidden)
