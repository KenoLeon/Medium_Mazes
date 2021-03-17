import PySimpleGUI as sg
import numpy as np


AppFont = 'Any 16'
sg.theme('DarkGrey5')
_VARS = {'cellCount': 10, 'gridSize': 400, 'canvas': False, 'window': False,
         'playerPos': False}
# cellMAP = np.random.randint(2, size=(_VARS['cellCount'], _VARS['cellCount']))
cellMAP = np.zeros((_VARS['cellCount'], _VARS['cellCount']), dtype=int)
cellSize = _VARS['gridSize']/_VARS['cellCount']
_VARS['playerPos'] = [0, 0]
print(repr(cellMAP))
# mazeMap
cellMAP = np.array([[0, 0, 0, 1, 0, 0],
                    [0, 0, 0, 1, 0, 0],
                    [0, 0, 0, 1, 0, 0],
                    [0, 0, 0, 1, 0, 0],
                    [0, 0, 0, 1, 0, 0],
                    [0, 0, 0, 1, 0, 0]])

# array([[0, 0, 0, 1, 0, 0],
#        [0, 0, 0, 1, 0, 0],
#        [0, 0, 0, 1, 0, 0],
#        [0, 0, 0, 1, 0, 0],
#        [0, 0, 0, 1, 0, 0],
#        [0, 0, 0, 1, 0, 0]])

# METHODS:


def drawGrid():
    cells = _VARS['cellCount']
    _VARS['canvas'].TKCanvas.create_rectangle(
        1, 1, _VARS['gridSize'], _VARS['gridSize'], outline='BLACK', width=1)
    for x in range(cells):
        _VARS['canvas'].TKCanvas.create_line(
            ((cellSize * x), 0), ((cellSize * x), _VARS['gridSize']),
            fill='BLACK', width=1)
        _VARS['canvas'].TKCanvas.create_line(
            (0, (cellSize * x)), (_VARS['gridSize'], (cellSize * x)),
            fill='BLACK', width=1)


def drawCell(x, y):
    _VARS['canvas'].TKCanvas.create_rectangle(
        x, y, x + cellSize, y + cellSize,
        outline='BLACK', fill='GREY', width=1)


def placeCells():
    for row in range(cellMAP.shape[0]):
        for column in range(cellMAP.shape[1]):
            if(cellMAP[column][row] == 1):
                drawCell((cellSize*row), (cellSize*column))


# INIT :
layout = [[sg.Canvas(size=(_VARS['gridSize'], _VARS['gridSize']),
                     background_color='white',
                     key='canvas')],
          [sg.Exit(font=AppFont)]]

_VARS['window'] = sg.Window('GridMaker', layout, resizable=True, finalize=True,
                            return_keyboard_events=True)
_VARS['canvas'] = _VARS['window']['canvas']
drawGrid()
drawCell(_VARS['playerPos'][0], _VARS['playerPos'][1])
placeCells()


while True:             # Event Loop
    event, values = _VARS['window'].read()
    if event in (None, 'Exit'):
        break
    # Filter key press
    if len(event) == 1:
        if ord(event) == 63232:  # UP
            print('UP')
            if (_VARS['playerPos'][1] - cellSize >= 0):
                _VARS['playerPos'][1] = _VARS['playerPos'][1] - cellSize
            else:
                print('WALL')
        elif ord(event) == 63233:  # DOWN
            print('DOWN')
            if (_VARS['playerPos'][1] + cellSize < 400):
                _VARS['playerPos'][1] = _VARS['playerPos'][1] + cellSize
            else:
                print('WALL')
        elif ord(event) == 63234:  # LEFT
            print('LEFT')
            if (_VARS['playerPos'][0] - cellSize >= 0):
                _VARS['playerPos'][0] = _VARS['playerPos'][0] - cellSize
            else:
                print('WALL')
        elif ord(event) == 63235:  # RIGHT
            print('RIGHT')
            if (_VARS['playerPos'][0] + cellSize < 400):
                _VARS['playerPos'][0] = _VARS['playerPos'][0] + cellSize
            else:
                print('WALL')
    print(_VARS['playerPos'])

    # Clear canvas, draw grid and cells
    _VARS['canvas'].TKCanvas.delete("all")
    drawGrid()
    placeCells()
    drawCell(_VARS['playerPos'][0], _VARS['playerPos'][1])
_VARS['window'].close()