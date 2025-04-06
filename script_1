#setting up the scene
stage.set_background_color("yellow")
stage.set_gravity(50)
stage.set_bounce(0)
stage.disable_right_wall()
stage.disable_left_wall()

#bringing speed to the stage
score = 0
score_board = codesters.Display(score, -200, 200)

#distanța de respaunare a triunghiurilor
distance = 400
#distanța de respaunare a platformelor
distance2 = 800
#personajul nostru
sprite = codesters.Square(-200,0,35, "red")


#funcția de generare a formei
def spawn():
    global distance, distance2, score
    #verificăm scorul pentru schimbarea culorii scenei
    if score > 50:
        stage.set_background_color("green")
        
    if score > 100 and score < 150:
        stage.set_background_color("purple")
        
    if score > 150:
        stage.set_background_color("blue")
    #spaunăm platforma
    platform = codesters.Rectangle(distance2,random.choice([-250, -150, -100]) , 35, 5, "orange")
    platform.set_gravity_off()
    platform.set_x_speed(-12)
    #spaunăm triunghiul
    triangle = codesters.Triangle(distance, 0, 20, "black")
    triangle.set_x_speed(-5)
    #adăugați o valoare distanței pentru generarea figurii următoare
    distance+=random.randint(100,200)
    distance2+=400
    
#funcția pentru mărirea scorului
def score_add():
    global score
    score+=1
    #verificăm scorul pentru victorie sau pentru o creștere suplimentară
    if score<=200:
        spawn()
        score_board.update(score)
    else:
        stage.event_interval(None)
        codesters.Text("You Win!!!", 0,0,"green").set_size(4)
        stage.remove_sprite(sprite)
        stage.remove_all_events()
        
stage.event_interval(score_add,0.1)


#functie de salt
def jump():
    #verificăm înălțimea de sărituri
    if sprite.get_y() < -220:
        
        sprite.jump(32)
        sprite.turn_right(180)
        
stage.event_key("space", jump)


#funcția de verificare a coliziunii
def collision(sprite, hit_sprite):
    name = hit_sprite.get_color()
    #ciocnire cu un triunghi
    if name == "black":
        codesters.Text("Game Over!!!", 0,0,"red").set_size(4)
        stage.remove_sprite(sprite)
        stage.remove_all_events()
    #ciocnirea platformei
    if name == "orange":
        sprite.jump(30)
        
sprite.event_collision(collision)

