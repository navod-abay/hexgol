import tkinter as tk
import math

WIDTH = 10  # number of tiles in a row
HEIGHT = 10  # number of rows in the honeycomb (both odd and even)
R = 20  # Radias: the length between a tile center and an edge
RSec
DISTANCE = 25  # the length between two tile centers
SEC30 = 1 / math.cos(math.pi / 6)


class Node:
    def __init__(self, u_id, row, pos):
        self.id = u_id
        self.row = row
        self.pos = pos
        self.state = False
        self.neighbours = self.find_neighbours()

    def find_neighbours(self):
        neighbours = [(self.row, self.pos - 1), (self.row, self.pos + 1), (self.row + 1, self.pos - (self.row % 2)),
                      (self.row + 1, self.pos - (self.row % 2) - 1), (self.row - 1, self.pos - (self.row % 2)),
                      (self.row + 1, self.pos - (self.row % 2) - 1)]

        return neighbours


class Board(tk.Canvas):
    def __init__(self, root):
        super(Board, self).__init__(root)
        self.tiles = self.initiate_tiles()

    def initiate_tiles(self):
        tiles = []
        for row in range(1, HEIGHT + 1):
            for position in range(WIDTH + 1):
                unique_id = self.draw_hexagon(row, position)
                tile = Node(unique_id, row, position)
                tiles.append(tile)
        return tiles

    def draw_hexagon(self, r, p):
        if r % 2 == 1:  # calculate the center of the tile
            x = (2 * p - 1) * DISTANCE / 2
            y = (3 * r - 2) * DISTANCE * SEC30 / 2
        else:
            x = p * DISTANCE
            y = (3 * r - 1) * DISTANCE * SEC30 / 4
        tag = self.create_polygon(x - R, y +)


root = tk.Tk()
board = Board(root)
board.pack()
root.mainloop()
