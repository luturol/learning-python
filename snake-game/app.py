class SnakeGame(object):
    screen = None

    def __init__(self, rows_count, column_count):
        self.screen = self.initialize_screen(rows_count, column_count)
    
    def initialize_screen(self, rows_count, column_count):
        #creates the 2D list with 0 in all values
        screen = [[0 for x in range(column_count)] for y in range(rows_count)]

        #get the rows
        for row in range(len(screen)):
            if row == 0 or row == len(screen) - 1:
                screen[row] = self.add_same_value_entire_list(screen[row], 1)
            else:
                for column in range(len(screen[row])):
                    if column == 0 or column == len(screen[row]) - 1:
                        screen[row][column] = 1        

        return screen

    def add_same_value_entire_list(self, list, value):
        populatedList = [value for i in range(len(list))]

        return populatedList

    def print_screen(self):
        screen_text = ''
        for row in self.screen:
            for column in row:
                screen_text = screen_text + self.translated_value(column)

            screen_text = screen_text + '\n'
        return screen_text

    def translated_value(self, value):
        if value == 1:
            return '#'
        elif value == 2:
            return '*'        
        elif value == -1: #snake body
            return 'O'
        elif value == -2: #runing snake head left <----
            return '<'
        elif value == -3: #runing  snake head right ---->
            return '>'
        else:
            return ' '


snake = SnakeGame(8, 8)
print(snake.print_screen())
