import os
import time
from termcolor import colored

class Canvas:
    def __init__(self, width, height):
        self._x = width
        self._y = height
        self._canvas = [[' ' for y in range(self._y)] for x in range(self._x)]

    def hitsWall(self, point):
        return point[0] < 0 or point[0] >= self._x or point[1] < 0 or point[1] >= self._y

    def setPos(self, pos, mark):
        self._canvas[pos[0]][pos[1]] = mark

    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def print(self):
        self.clear()
        for y in range(self._y):
            print(' '.join([col[y] for col in self._canvas]))

class TerminalScribe:
    def __init__(self, canvas):
        self.canvas = canvas
        self.trail = '.'
        self.mark = '*'
        self.framerate = 0.2
        self.pos = [0, 0]

    def up(self):
        pos = [self.pos[0], self.pos[1]-1]
        if not self.canvas.hitsWall(pos):
            self.draw(pos)

    def down(self):
        pos = [self.pos[0], self.pos[1]+1]
        if not self.canvas.hitsWall(pos):
            self.draw(pos)

    def right(self):
        pos = [self.pos[0]+1, self.pos[1]]
        if not self.canvas.hitsWall(pos):
            self.draw(pos)

    def left(self):
        pos = [self.pos[0]-1, self.pos[1]]
        if not self.canvas.hitsWall(pos):
            self.draw(pos)

    #new functions that take an arugment
    def upCount(self, count):
        #use range starting at 1 to draw 'count' number of times
        for i in range(1, count):
            pos = [self.pos[0], self.pos[1]-1]
            if not self.canvas.hitsWall(pos):
                self.draw(pos)
    
    def downCount(self, count):
        for i in range(1, count):
            pos = [self.pos[0], self.pos[1]+1]
            if not self.canvas.hitsWall(pos):
                self.draw(pos)

    def rightCount(self, count):
        for i in range(1, count):
            pos = [self.pos[0]+1, self.pos[1]]
            if not self.canvas.hitsWall(pos):
                self.draw(pos)

    def leftCount(self, count):
        for i in range(1, count):
            pos = [self.pos[0]-1, self.pos[1]]
            if not self.canvas.hitsWall(pos):
                self.draw(pos)

    def draw(self, pos):
        self.canvas.setPos(self.pos, self.trail)
        self.pos = pos
        self.canvas.setPos(self.pos, colored(self.mark, 'red'))
        self.canvas.print()
        time.sleep(self.framerate)
    
    def drawSqaure(self, size):
        size = size
        for i in range(size):
            scribe.down()
        for i in range(size):
            scribe.right()
        for i in range(size):
            scribe.up()
        for i in range(size):
            scribe.left()

    def drawSqaureClean(self, size):
        self.size = size
        scribe.downCount(size)
        scribe.rightCount(size)
        scribe.upCount(size)
        scribe.leftCount(size)


canvas = Canvas(30, 30)
scribe = TerminalScribe(canvas)

#draws a sqaure usuing many for loops
#scribe.drawSqaure(10)

#draws a sqaure with using new functions that take an input instead of moving only 1 increment
scribe.drawSqaureClean(10)

"""
#draw sqaure manually
scribe.right()
scribe.right()
scribe.right()
scribe.down()
scribe.down()
scribe.down()
scribe.left()
scribe.left()
scribe.left()
scribe.up()
scribe.up()
scribe.up()
"""

__author__ = "Ryan Mitchel"
__modifications__ = "dh_tester"
