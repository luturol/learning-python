class SnakeGame(object):
    screen = None

    def __init__(self, rows_count, column_count):
        self.screen = self.initialize_screen(rows_count, column_count)
    
    def initialize_screen(self, rows_count, column_count):
        #creates the 2D list with 0 in all values
        screen = [[0 for x in range(column_count)] for y in range(rows_count)]

        #get the rows
        for i in range(len(screen)):
            if i == 0 or i == len(screen) - 1:
                screen[i] = self.add_same_value_entire_list(screen[i], 1)

        return screen




    def add_same_value_entire_list(self, list, value):
        populatedList = [value for i in range(len(list))]

        return populatedList

     
snake = SnakeGame(8, 8)
print(snake.screen)
