"""Tic Tac Toe with Turtle""
import turtle
from freegames import line

# Global variables
state = {'player': 0}  # 0 = X, 1 = O
players = ['X', 'O']
board = [None] * 9  # 3x3 grid

# Draw the grid
def grid():
    line(-67, 200, -67, -200)
    line(67, 200, 67, -200)
    line(-200, -67, 200, -67)
    line(-200, 67, 200, 67)

# Draw X
def drawx(x, y):
    line(x, y, x + 133, y + 133)
    line(x, y + 133, x + 133, y)

# Draw O
def drawo(x, y):
    turtle.up()
    turtle.goto(x + 67, y + 5)
    turtle.down()
    turtle.circle(62)

# Map coordinates to the cell
def floor(value):
    return ((value + 200) // 133) * 133 - 200

# Check for a win
def check_winner():
    wins = [
        [0,1,2],[3,4,5],[6,7,8],  # Rows
        [0,3,6],[1,4,7],[2,5,8],  # Columns
        [0,4,8],[2,4,6]           # Diagonals
    ]
    for line_idx in wins:
        a, b, c = line_idx
        if board[a] and board[a] == board[b] == board[c]:
            return board[a]
    return None

# Handle click
def tap(x, y):
    col = int((x + 200) // 133)
    row = int((200 - y) // 133)
    if col < 0 or col > 2 or row < 0 or row > 2:
        return
    index = row * 3 + col

    if board[index] is not None:
        return

    if state['player'] == 0:
        drawx(floor(x), floor(y))
        board[index] = 'X'
    else:
        drawo(floor(x), floor(y))
        board[index] = 'O'

    turtle.update()

    winner = check_winner()
    if winner:
        turtle.textinput("Game Over", f"{winner} wins!")
        turtle.bye()
        return
    elif all(board):
        turtle.textinput("Game Over", "Draw!")
        turtle.bye()
        return

    state['player'] = 1 - state['player']

# Turtle initialization
turtle.title("Tic Tac Toe ~ AliAref")
turtle.setup(420, 420, 370, 0)
turtle.hideturtle()
turtle.tracer(False)

grid()
turtle.update()
turtle.onscreenclick(tap)
turtle.done()
