class OutOfBoardException(Exception):

    def __init__(self, x, y, *args):
        super().__init__(*args)
        self.x = x
        self.y = y
    
    def __str__(self):
        return f'This coordinate: ({self.x}, {self.y}) is out of bounds. Try again!'

class NotEmptySpaceException(Exception):

    def __init__(self, space, *args):
        super().__init__(*args)
        self.space = space
    
    def __str__(self):
        return f'This space is already taken by ({self.space}). Try again!'

class NotAPlayerException(Exception):

    def __init__(self, player, *args):
        super().__init__(*args)
        self.player = player
    
    def __str__(self):
        return f'({self.player}) is not a valid player. Someting went wrong :('

class NotANumberException(Exception):

    def __init__(self, coord, *args):
        super().__init__(*args)
        self.coord = coord
    
    def __str__(self):
        return f'This coordinate ({self.coord}) is not a number.'
