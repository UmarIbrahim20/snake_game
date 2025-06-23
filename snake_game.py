from tkinter import *
import random

## make some constants
## that dont chagne for game setting

GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED = 150 ## LOWER THE NUMBER FASTER THE GAME
SPACE_SIZE = 50 ## SIZE OF FOOD
BODY_PARTS = 3
SNAKE_COLOR = "#00ff00"
FOOD_COLOR = "#FF0000"
BACKGROUND_COLOR = "#000000"

class Snake:
    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.sqaures = []

        for i in range(0, BODY_PARTS):
            self.coordinates.append([0,0])

        for x,y in self.coordinates:
            square = canvas.create_rectangle(x,y, x+SPACE_SIZE, y+SPACE_SIZE, fill=SNAKE_COLOR, tags="snake")
            self.sqaures.append(square)
        
class Food:
    def __init__(self):
        ## food shows random
        x = random.randint(0, (GAME_WIDTH//SPACE_SIZE)-1)* SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT//SPACE_SIZE)-1)* SPACE_SIZE

        self.coordinates = [x, y]
        canvas.create_oval(x,y, x+SPACE_SIZE, y+ SPACE_SIZE, fill=FOOD_COLOR, tags="food")

def next_turn(snake, food):
    ## head of snakes
    x,y = snake.coordinates[0]

    if direction == "up":
        y-= SPACE_SIZE

    elif direction == "down":
        y += SPACE_SIZE

    elif direction == "left":
        x -= SPACE_SIZE

    elif direction == "right":
        x += SPACE_SIZE

    ## Update the coordinates of head of snake
    snake.coordinates.insert(0,(x,y))
    square = canvas.create_rectangle(x,y, x+SPACE_SIZE, y+SPACE_SIZE, fill=SNAKE_COLOR)
    snake.sqaures.insert(0,square)

    ## Logic to eat food x= head and y = tail
    if x == food.coordinates[0] and y == food.coordinates[1]:
        global score 

        score+=1
        label.config(text="Score:{}".format(score))
        canvas.delete("food")
        ## again create food instance
        food = Food()
    else:
        ## Delete last set of coordinates of snake
        del snake.coordinates[-1]

        ## update canvas
        canvas.delete(snake.sqaures[-1])

        del snake.sqaures[-1]

    if check_collisions(snake):
        game_over()
    
    else:
        window.after(SPEED, next_turn, snake, food)

def change_direction(new_directions):

    global direction
    print(f"new direaction: {new_directions}")

    if new_directions == 'left':
        if direction != 'right':
            direction = new_directions

    elif new_directions == 'right':
        if direction != 'left':
            direction = new_directions

    elif new_directions == 'up':
        if direction != 'down':
            direction = new_directions

    elif new_directions == 'down':
        if direction != 'up':
            direction = new_directions

def check_collisions(snake):
    x,y = snake.coordinates[0]

    if x < 0 or x >= GAME_WIDTH:
        print("Game Over")
        return True
    elif y < 0 or y >= GAME_HEIGHT:
        print("Game Over")
        return True

    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            print("Game over")
            return True
    
    return False

def game_over():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2, font=('consolas',70),text="Game Over", fill="red", tag="gameover")


## Window setting or publishing game window activation
window = Tk()

## set the game properties
window.title("Snake game")
window.resizable(False,False)

## socore label
score = 0
direction = 'down'

label = Label(window, text="Score:{}".format(score), font = ('consolas', 40))
label.pack()

canvas = Canvas(window, bg= BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()
canvas.focus_set()
## to center our window

## force to render the layout
window.update_idletasks()

## Fetch snake window size
window_width = window.winfo_width()
window_height = window.winfo_height()

## Fetch screen size
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")

## Bind keys
window.bind('<Left>', lambda event: change_direction('left'))
window.bind('<Right>', lambda event: change_direction('right'))
window.bind('<Up>', lambda event: change_direction('up'))
window.bind('<Down>', lambda event: change_direction('down'))

# Begin game with snake 
snake = Snake()
food = Food()
next_turn(snake, food)

window.mainloop()

 