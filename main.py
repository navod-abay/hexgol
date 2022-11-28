import tkinter as tk

WIDTH = 10 # number of tiles in a row
HEIGHT = 10 # number of rows in the honeycomb (both odd and even)
RADIUS = 20 # the length between a tile center and an edge
DISTANCE = 25 # the length between two tile centers


class Node:
    def __init__(self, u_id, row, pos):
        assert (u_id == row * WIDTH + pos)
        self.id = u_id
        self.row = row
        self.pos = pos
        self.state = False
        self.neighbours = self.find_neighbours()

    def draw_hexagon(self):
        pass

    def find_neighbours(self):
        neighbours = [(self.row, self.pos - 1), (self.row, self.pos + 1), (self.row + 1, self.pos - (self.row % 2)),
                      (self.row + 1, self.pos - (self.row % 2) - 1), (self.row - 1, self.pos - (self.row % 2)),
                      (self.row + 1, self.pos - (self.row % 2) - 1)]

        return neighbours


class Board(tk.Canvas):
    def __init__(self, root):
        super(Board, self).__init__(root)
        self.tiles = self.initiate_tiles()

    @staticmethod
    def initiate_tiles():
        return []


root = tk.Tk()
board = Board(root)
board.pack()
root.mainloop()
