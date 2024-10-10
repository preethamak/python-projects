import tkinter  # to get the graphics
import random  # to place food at random place

ROWS = 20
COLS = 20
TILE_SIZE = 20

WIN_WIDTH = TILE_SIZE * COLS
WIN_HEIGHT = TILE_SIZE * ROWS


class Tile:  # to create a snake tile and food tile
    def __init__(self, x, y):
        self.x = x
        self.y = y


# gaming window
window = tkinter.Tk()
window.title("SNAKE GAME")
window.resizable(False, False)

canvas = tkinter.Canvas(window, bg="black", width=WIN_WIDTH, height=WIN_HEIGHT, borderwidth=0, highlightthickness=0)
canvas.pack()

# center the window
window_width = WIN_WIDTH
window_height = WIN_HEIGHT
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# for the midpoint
window_x = int((screen_width / 2) - (window_width / 2))
window_y = int((screen_height / 2) - (window_height / 2))

window.geometry(f'{window_width}x{window_height}+{window_x}+{window_y}')

# initialize tile
snake = Tile(5 * TILE_SIZE, 5 * TILE_SIZE)
food = Tile(10 * TILE_SIZE, 10 * TILE_SIZE)
snake_body = []  # multiple tile objects

# defining the velocity
velocityx = 0
velocityy = 0
# terminating after collision
game_over = False

# score recording
score = 0


def change_direction(e):
    global velocityx, velocityy, game_over
    if game_over:
        return

    if e.keysym == "Up" and velocityy != 1:
        velocityx = 0
        velocityy = -1
    elif e.keysym == "Down" and velocityy != -1:
        velocityx = 0
        velocityy = 1
    elif e.keysym == "Right" and velocityx != -1:
        velocityx = 1
        velocityy = 0
    elif e.keysym == "Left" and velocityx != 1:
        velocityx = -1
        velocityy = 0


def move():
    global snake, food, snake_body, game_over, score
    if game_over:
        return

    # gameover when snake collides with the edges of window
    if snake.x < 0 or snake.x >= WIN_WIDTH or snake.y < 0 or snake.y >= WIN_HEIGHT:
        game_over = True
        return

    # game over when the snake collides with its own body
    for tile in snake_body:
        if snake.x == tile.x and snake.y == tile.y:
            game_over = True
            return

    # moving the snake body
    if len(snake_body) > 0:
        snake_body.insert(0, Tile(snake.x, snake.y))
        snake_body.pop()

    # contact with the food
    if snake.x == food.x and snake.y == food.y:
        snake_body.append(Tile(snake.x, snake.y))

        # placing the food in different position
        food.x = random.randint(0, COLS - 1) * TILE_SIZE
        food.y = random.randint(0, ROWS - 1) * TILE_SIZE
        score += 10

    # moving the snake in the x and y direction
    snake.x += velocityx * TILE_SIZE
    snake.y += velocityy * TILE_SIZE


def draw():  # draw the snake
    global snake, snake_body, food, score, game_over
    move()

    # delete the previous frames
    canvas.delete("all")

    # draw food
    canvas.create_oval(food.x, food.y, food.x + TILE_SIZE, food.y + TILE_SIZE, fill="lime green")

    # draw snake
    canvas.create_rectangle(snake.x, snake.y, snake.x + TILE_SIZE, snake.y + TILE_SIZE, fill="red")
    for tile in snake_body:
        canvas.create_rectangle(tile.x, tile.y, tile.x + TILE_SIZE, tile.y + TILE_SIZE, fill="red")

    # writing the game over condition after colliding
    if game_over:
        canvas.create_text(window_width / 2, window_height / 2, font="Arial 20",
                           text=f'GAME OVER: {score} GOOD LUCK!', fill="white")
    else:
        canvas.create_text(30, 20, font="Arial 10", text=f'Score: {score}', fill="white")
    window.after(150, draw)  # 1/10secs, 10frames/sec


draw()
window.bind("<KeyRelease>", change_direction)
window.mainloop()
