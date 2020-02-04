import os
from msvcrt import getch

class SnakeGame(object):
    screen = None

    def __init__(self, rows_count, column_count):
        self.screen = self.initialize_screen(rows_count, column_count)
        self.collided = False
    
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
        elif value == -2: #moving left snake head left <----
            return '<'
        elif value == -3: #moving right  snake head right ---->
            return '>'
        elif value == -4: #moving down
            return 'V'
        elif value == -5: #moving up
            return '^'
        else:
            return ' '

    def play(self):
        player = Player()
        key_pressed = 9999
        self.add_player_to_screen(player)

        while(self.defeated() is not True and key_pressed != 27):
            self.clear()
            print(self.print_screen())            
            key_pressed = self.read_key()
            player.move(self.translate_key(key_pressed))
            self.add_player_to_screen(player)

    def read_key(self):
        return ord(getch())
    
    def add_player_to_screen(self, player):  
        print(player.location_x)
        print(player.location_y)    
        if(player.position_cordination == 'E'):
            self.screen[player.location_x][player.location_y - 1] = 0
        elif (player.position_cordination == 'W'):
            self.screen[player.location_x][player.location_y + 1] = 0
        elif (player.position_cordination == 'N'):
            self.screen[player.location_x + 1][player.location_y] = 0
        elif (player.position_cordination == 'S'):
            self.screen[player.location_x - 1][player.location_y] = 0

        if(self.screen[player.location_x][player.location_y] == 0):
            self.screen[player.location_x][player.location_y] = player.body
        elif(self.screen[player.location_x][player.location_y] < 0):
            self.collided = True
    
    def translate_key(self, key):
        print (key)        
        if (key == 224):
            key = ord(getch())
            print(key)
            if (key == 72):
                return 'N'
            elif (key == 80):
                return 'S'
            elif (key == 75):
                return 'W'
            elif (key == 77):
                return 'E'
        else:
            pass

    def defeated(self):
        return self.collided

    def clear(self):
        os.system('cls' if os.name=='nt' else 'clear')
        
class Player(object):
    def __init__(self):
        self.nodes_size = 1
        self.position_cordination = 'E'
        self.last_cordination = 'E'
        self.location_x = 4
        self.location_y = 4     
        self.body = -3          

    def draw(self):
        body = ''
        for index in range(self.nodes_size):
            if(index == 0 and self.position_cordination == 'E'):
                body = '>'
            elif(index == 0 and self.position_cordination == 'W'):
                body = '<'
            elif(index == 0 and self.position_cordination == 'N'):
                body = '^'
            elif(index == 0 and self.position_cordination == 'S'):
                body = 'V'
            else:
                body += '-'
        
        return body

    def move(self, cordination):     
        print("Cordinations x = " + str(self.location_x) + " y = " + str(self.location_y))
        if (self.position_cordination != 'S' and cordination == 'N'):
            self.location_x -= 1
            self.body = -5
        elif (self.position_cordination != 'N' and cordination == 'S'):
            self.location_x +=1
            self.body = -4
        elif (self.position_cordination != 'W' and cordination == 'E'):            
            self.location_y += 1
            self.body = -3
        elif (self.position_cordination != 'E' and cordination == 'W'):
            self.location_y -= 1
            self.body = -2
        else:
            pass

        self.position_cordination = cordination
        print("Cordinations x = " + str(self.location_x) + " y = " + str(self.location_y))
    
snake = SnakeGame(32, 32)
snake.play()