import curses
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN
from random import randint

curses.initscr()
window = curses.newwin(30, 60, 0, 0)
window.keypad(True)
curses.noecho()
curses.curs_set(0)
window.nodelay(True)

key = KEY_RIGHT
score = 0

snake = [[5, 8], [5, 7], [5, 6]]
food = [10, 25]

window.addch(food[0], food[1], 'O')

while key != 27:
    window.border(0)
    window.addstr(0, 2, 'Score: ' + str(score) + ' ')
    window.addstr(0, 27, ' SNAKE! ')

    window.timeout(140 - (len(snake) / 5 + len(snake) / 10) % 120)

    event = window.getch()
    key = key if event == -1 else event


    snake.insert(0, [snake[0][0] + (key == KEY_DOWN and 1) + (key == KEY_UP and -1),
                     snake[0][1] + (key == KEY_LEFT and -1) + (key == KEY_RIGHT and 1)])


    if snake[0][0] == 0 or snake[0][0] == 29 or snake[0][1] == 0 or snake[0][1] == 59: break


    if snake[0] in snake[1:]: break


    if snake[0] == food:
        food = []
        score += 1
        while food == []:

            food = [randint(1, 28), randint(1, 58)]
            if food in snake: food = []
        window.addch(food[0], food[1], 'O')
    else:
        last = snake.pop()
        window.addch(last[0], last[1], ' ')
    window.addch(snake[0][0], snake[0][1], '#')

curses.endwin()
print("\nScore: " + str(score))
