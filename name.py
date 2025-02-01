# Place the sprite for lives
heart = codesters.Sprite("Heart_0b9", -220, 200)
heart.set_size(2) 
# Text for lives
lives = 10
lives_text = codesters.Text(str(lives), -180, 200, "red")
lives_text.set_size(2)
# Text for bullets
bullets = 10                       
ammo = codesters.Sprite("Ammo_066", -220, 165)
ammo_text = codesters.Text(str(bullets), -180, 165, "yellow")
ammo_text.set_size(2)

# Set up the scene
stage.set_background("jupiter")
stage.disable_right_wall()
stage.disable_left_wall()
stage.set_bounce(0.2)
stage.disable_floor()
# Display the score on the screen
score = 0
score_png = codesters.Sprite("Score_3ad", -205, 135)
score_text = codesters.Text(str(score), -150, 135, "blue")
score_text.set_size(2)
# Add the character and set a negative speed for them
soldier = codesters.Sprite("Soldier_no_Fire_V2_8c0")
soldier.set_y_speed(-10)
# Add a platform and initially set its speed to 0, but it will be changed later
platform = codesters.Sprite("Platform_c9b",0, -200)
platform.set_x_speed(-5)
# Variable to cancel the loop
a = 0

# Function for jumping
def jump():
    soldier.get_x()
    # Simulate fire from the jetpack
    fire_jet = codesters.Sprite("Fire_Jet_pack_af0",soldier.get_x()-15,soldier.get_y()-15)
    fire_jet.hide()
    soldier.jump(10)
    # Set x speed to 0 to prevent the character from following the platform
    soldier.set_x_speed(0)
  
# Function for moving left   
def move_left():
    soldier.move_left(50)
# Function for moving right
def move_right():
    soldier.move_right(50)
    # Set x speed to 0 to prevent the character from following the platform
    soldier.set_x_speed(0)
    
stage.event_key("left", move_left)
stage.event_key("right", move_right)
stage.event_key("up", jump)

# Function to check for hits
def strike(sprite, hit_sprite):
    global score
    global score_text
    name = hit_sprite.get_image_name()
    # Check for winning condition
    if score >= 5:
        # Disable the loop and all events
        a = 1
        stage.remove_all_events()
        soldier.hide()
        text = codesters.Text("You Win !!!", 0, 0, "yellow")
        text.set_size(4)
    if name == "Enemy_1_8ad":
        score += 1
        stage.remove_sprite(hit_sprite)
        stage.remove_sprite(score_text)
        score_text = codesters.Text(str(score), -150, 135, "blue")
        score_text.set_size(2)
    if name == "Enemy_2_d13":
        stage.remove_sprite(hit_sprite)
        score += 1
        stage.remove_sprite(hit_sprite)
        stage.remove_sprite(score_text)
        score_text = codesters.Text(str(score), -150, 135, "blue")
        score_text.set_size(2)
    if name == "Enemy_3_549":
        stage.remove_sprite(hit_sprite)
        score += 1
        stage.remove_sprite(hit_sprite)
        stage.remove_sprite(score_text)
        score_text = codesters.Text(str(score), -150, 135, "blue")
        score_text.set_size(2)

# Function for shooting    
def shot():
    global bullets
    global ammo_text
    sound = codesters.Sound("drum_bell")
    sound.play()
    stage.remove_sprite(ammo_text)
    bullets -= 1
    # Update the bullets counter  
    ammo_text = codesters.Text(str(bullets),-180, 165, "yellow")
    ammo_text.set_size(2)
    # Reload
    if bullets <= 0:
        bullets = 0
        stage.wait(0.5)
        bullets = 10
    # Simulate gunfire
    sprite = codesters.Sprite("Fire_a0d",soldier.get_x()+5,soldier.get_y())
    sprite.set_size(0.1)
    sprite.hide()
    # Spawn a bullet
    bullet = codesters.Sprite("Bullet_a84",soldier.get_x()+5,soldier.get_y())
    bullet.set_y_speed(0)
    bullet.set_x_speed(5)
    
    bullet.event_collision(strike)

stage.event_key("space", shot)

# Check what we collided with 
def collision(sprite, hit_sprite):
    global lives
    global lives_text
    
    name = hit_sprite.get_image_name()
    # Check the specific case for landing on a platform 
    if name == "Platform_c9b":
        if soldier.get_y_speed() < 0:
            speed = hit_sprite.get_x_speed()
            soldier.set_y_speed(0)
            soldier.set_x_speed(speed)
    if name == "Enemy_1_8ad":
        soldier.set_opacity(0.2)
        stage.wait(0.2)
        soldier.set_opacity(1)
        lives -= 1
        stage.remove_sprite(lives_text)
        lives_text = codesters.Text(str(lives), -180, 200, "red")
        lives_text.set_size(2)
    if name == "Enemy_3_549":
        soldier.set_opacity(0.2)
        stage.wait(0.2)
        soldier.set_opacity(1)
        lives -= 1
        stage.remove_sprite(lives_text)
        lives_text = codesters.Text(str(lives), -180, 200, "red")
        lives_text.set_size(2)
    if name == "Enemy_2_d13":
        soldier.set_opacity(0.2)
        stage.wait(0.2)
        soldier.set_opacity(1)
        lives -= 1
        stage.remove_sprite(lives_text)
        lives_text = codesters.Text(str(lives), -180, 200, "red")
        lives_text.set_size(2)
    if name == "Enemy_bullet_4c0":
        soldier.set_opacity(0.2)
        stage.wait(0.2)
        soldier.set_opacity(1)
        lives -= 1
        stage.remove_sprite(lives_text)
        lives_text = codesters.Text(str(lives), -180, 200, "red")
        lives_text.set_size(2)
    # Check for game over 
    if lives <= 0:
        lives_text = codesters.Text("0", -180, 200, "red")
        lives_text.set_size(2)
        a = 1
        stage.remove_all_events()
        soldier.hide()
        text = codesters.Text("Game Over", 0, 0, "red")
        text.set_size(4)
            
soldier.event_collision(collision)

# Function to check if the character has gone off the screen
def game_over():
    
    if soldier.get_y() < -260:
        text = codesters.Text("Game Over", 0, 0, "red")
        text.set_size(4)
    if soldier.get_x() < -260: 
        text = codesters.Text("Game Over", 0, 0, "red")
        text.set_size(4)

# List of all sprites 
enemy_list = ["Enemy_2_d13", "Enemy_1_8ad", "Enemy_3_549"]
x = 200
c = 300

# Enemy attack 
def enemy_shot(sprite):     
    enemy_bullet = codesters.Sprite("Enemy_bullet_4c0", sprite.get_x(), sprite.get_y())
    enemy_bullet.glide_to(-400, soldier.get_y())

enemy = ""

def respawn(sprite, speed, distance):
    global enemy       
    enemy = codesters.Sprite(sprite, distance, random.randint(-200, 200))
    enemy.set_x_speed(speed)
    stage.event_interval(enemy_shot(enemy), 0.1)

while a == 0:
    game_over()
    speed = 0
    if soldier.get_y_speed() == 0:
        speed = 0
        soldier.set_y_speed(speed)
    if soldier.get_y_speed() < 0 or soldier.get_y_speed() > 0:
        speed = -10
        soldier.set_y_speed(speed)
    platform = codesters.Sprite("Platform_c9b", c, random.randint(-200, 200))
    platform.set_size(random.random())
    platform.set_x_speed(-5)
    
    c += 300
    
    respawn(random.choice(enemy_list), -5, x)
    
    x += 200





