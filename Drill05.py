import random

from pico2d import*

open_canvas()

arrow = load_image('hand_arrow.png')
background = load_image('TUK_GROUND_FULL.png')
character = load_image('animation_sheet.png')

def handle_events():
    global running

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False

def draw_hand():
    global hand_x, hand_y
    #clear_canvas()
    #background.draw(400, 30)
    arrow.draw(hand_x, hand_y)
    update_canvas()

def draw_character():
    global char_x, char_y
    character.clip_draw(0, 0, 100, 100, char_x, char_y)

def move_character():
    global x, y
    t = 0
    frame = 0
    while t <= 1:
        x = (1 - t) * char_x + t * hand_x  # char_x와 hand_x를 사용하여 x 계산
        y = (1 - t) * char_y + t * hand_y  # char_y와 hand_y를 사용하여 y 계산

        #clear_canvas()
        #background.draw(400, 30)
        '''if x <= char_x:
            character.clip_draw(0, 0, 100, 100, x, y)
        elif x >= char_x:
            character.clip_draw(0, 100, 100, 100, x, y)'''
        if x <= char_x:
            character.clip_draw(frame * 100, 0, 100, 100, x, y)
        elif x >= char_x:
            character.clip_draw(frame * 100, 100, 100, 100, x, y)
        update_canvas()

        frame = (frame + 1) % 8
        t += 0.05
        delay(0.1)

running = True
char_x, char_y = 50, 50

#background.draw(400, 30)

while running:
    moving = True
    clear_canvas()
    background.draw(400, 30)
    hand_x, hand_y = random.randint(0, 800), random.randint(0, 600)
    draw_hand()

    while moving:
        move_character()
        char_x, char_y = hand_x, hand_y
        moving = False
        #draw_character()
        #update_canvas()
        handle_events()

close_canvas()