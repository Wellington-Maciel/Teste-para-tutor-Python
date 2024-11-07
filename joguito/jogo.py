import random 
import math  
from pygame import Rect  
import pgzrun  


WIDTH = 800
HEIGHT = 600


MENU = 0
GAME = 1
state = MENU


music_on = True


hero = Actor('hero_stand', (400, 300))  
hero.speed = 3 


enemies = []
enemy_images = ['enemy1', 'enemy2']  
enemy_speed = 2  


def create_enemy():
    x = random.randint(0, WIDTH)
    y = random.randint(0, HEIGHT)
    enemy = Actor(random.choice(enemy_images), (x, y))
    enemies.append(enemy)


for i in range(5):
    create_enemy()


def draw_menu():
    screen.clear()  
    screen.draw.text("Menu Principal", (300, 100), fontsize=50, color="white")
    screen.draw.text("Pressione ENTER para Começar", (200, 200), fontsize=30, color="white")
    screen.draw.text("Pressione S para Ativar/Desativar o Som", (200, 250), fontsize=30, color="white")
    screen.draw.text("Pressione Q para Sair", (200, 300), fontsize=30, color="white")


def toggle_sound():
    global music_on
    music_on = not music_on
    if music_on:
        music.play("background_music")  
    else:
        music.stop()


def update_game():
    if keyboard.left:
        hero.x -= hero.speed
        hero.image = 'hero_walk'  
    if keyboard.right:
        hero.x += hero.speed
        hero.image = 'hero_walk'
    if keyboard.up:
        hero.y -= hero.speed
        hero.image = 'hero_walk'
    if keyboard.down:
        hero.y += hero.speed
        hero.image = 'hero_walk'

    
    if not (keyboard.left or keyboard.right or keyboard.up or keyboard.down):
        hero.image = 'hero_stand'

    
    for enemy in enemies:
        dx = hero.x - enemy.x
        dy = hero.y - enemy.y
        dist = math.hypot(dx, dy)
        if dist > 0:
            dx, dy = dx / dist, dy / dist
            enemy.x += dx * enemy_speed
            enemy.y += dy * enemy_speed

        
        if hero.colliderect(enemy):
            reset_game()


def reset_game():
    global state
    state = MENU
    hero.pos = (400, 300)
    for enemy in enemies:
        enemy.pos = (random.randint(0, WIDTH), random.randint(0, HEIGHT))


def draw_game():
    screen.clear()
    hero.draw()
    for enemy in enemies:
        enemy.draw()


def on_key_down(key):
    global state
    if state == MENU:
        if key == keys.RETURN:
            state = GAME
        elif key == keys.S:
            toggle_sound()
        elif key == keys.Q:
            exit()


def update():
    if state == GAME:
        update_game()


def draw():
    if state == MENU:
        draw_menu()
    elif state == GAME:
        draw_game()


if music_on:
    music.play("background_music")


pgzrun.go()
