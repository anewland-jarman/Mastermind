import pygame
import random
import sys
import pickle
import os

# Get the current working directory
cwd = os.getcwd()
# Initialize pygame
pygame.init()

# Set the dimensions of the window
width = 600
height = 800

# Create the window
screen = pygame.display.set_mode((width, height))

# Set the font for the prompt message
font = pygame.font.Font(None, 36)

# Set the background color
screen.fill((0, 0, 0))

def draw_input_box(x, y, width, height, prompt):
    screen.fill((0,0,0))
    # Draw a white rectangle for the input box
    pygame.draw.rect(screen, (255, 255, 255), (x, y, width, height), 1)

    # Render the prompt message as a text surface
    text_surface = font.render(prompt, True, (255, 255, 255))

    # Get the dimensions of the text surface
    text_width, text_height = text_surface.get_size()

    # Calculate the x and y positions for the text
    text_x = x + (width - text_width) // 2
    text_y = y + (height - text_height) // 2

    # Draw the text on the screen
    screen.blit(text_surface, (text_x, text_y))

def main():
    menuopened = False
    justclosed = False
    # Set the initial input string to an empty string
    input_string = ""

    # Set the initial position of the input box
    input_box_x = 100
    input_box_y = 200
    input_box_width = 500
    input_box_height = 50

    # Set the prompt message for the input box
    prompt = "Enter your name:"
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # Check for key press events
            elif event.type == pygame.KEYDOWN:
                # Update the input string based on the key press
                if event.key == pygame.K_BACKSPACE:
                    input_string = input_string[:-1]
                elif event.key == pygame.K_RETURN:
                    # Close the input box when the user presses enter
                    running = False
                else:
                    input_string += event.unicode
        prompt ="Enter your name:" + input_string
        draw_input_box(input_box_x,input_box_y,input_box_width,input_box_height,prompt)

        pygame.display.update()
    name = input_string

    print(input_string)
    # Initialize Pygame
    pygame.init()

    # Set the window size
    window_size = (600, 1000)

    #Create the window
    screen = pygame.display.set_mode(window_size)


    screen_width = 600
    screen_height = 800
    class Leaderboard():
        def __init__(self):    
            with open("leaderboarddata","rb") as f:
                griddata = pickle.load(f)
            # Create the grid data
            self.grid_data = griddata

            # Set the dimensions for the grid cells
            self.cell_width = 200
            self.cell_height = 50

            # Set the starting x and y positions for the grid
            self.x_pos = 100
            self.y_pos = 50


        def sort_list(self,lst):
            # Sort the list ignoring the first element
            sorted_list = sorted(lst[1:], key=lambda x: int(x[1]))

            # Add the first element back to the beginning of the list
            sorted_list.insert(0, lst[0])
            return sorted_list[:10]

        def show_leaderboard(self):
            with open("leaderboarddata","rb") as f:
                griddata = pickle.load(f)
            # Create the grid data
            self.grid_data = griddata
            screen.fill((0,0,0))
            self.grid_data = self.sort_list(self.grid_data)
            for row in self.grid_data:
                for cell in row:
                    # Create a rectangle for the cell
                    rect = pygame.Rect(self.x_pos, self.y_pos, self.cell_width, self.cell_height)

                    # Draw the cell
                    pygame.draw.rect(screen, (255,255,255), rect, 1)

                    # Create a text surface for the cell text
                    text_surface = font.render(cell, True, (255,255,255))

                    # Get the dimensions of the text surface
                    self.text_width,self.text_height = text_surface.get_size()

                    # Calculate the x and y positions for the text
                    self.text_x = self.x_pos + (self.cell_width - self.text_width) // 2
                    self.text_y = self.y_pos + (self.cell_height - self.text_height) // 2

                    # Draw the text on the screen
                    screen.blit(text_surface, (self.text_x, self.text_y))

                    # Increment the x position for the next cell
                    self.x_pos += self.cell_width
                    # Reset the x position for the next row
                self.x_pos = 100

                # Increment the y position for the next row
                self.y_pos += self.cell_height
        def hide_leaderboard(self,justclosed):
                screen.fill((0,0,0))
                # Reset the x and y positions for the next time the menu is opened
                self.x_pos = 100
                self.y_pos = 50
                justclosed = False
                return justclosed


    class PauseMenu(Leaderboard):
        def __init__(self):
            Leaderboard.__init__(self)
            self.screen = screen
            self.game_paused = False
            self.game_status = f"Game in Progress..."
            self.icon_visible = True
        def Return_game_paused(self):
            return self.game_paused
        def hide_pause_menu(self):
            self.screen.fill((0, 0 , 0))
            

        def show_pause_menu(self):
            # Set the font and text for the menu options
            self.font = pygame.font.Font(None, 32)
            self.game_status_text = self.font.render(self.game_status, True,(255,255,255))
            self.game_status_text_rect = self.game_status_text.get_rect(topleft =((screen_width - 200) / 2 + 20, (screen_height - 100) / 2)) 
            self.resume_text = self.font.render("Resume", True, (255, 255, 255))
            self.resume_text_rect = self.resume_text.get_rect(topleft=((screen_width - 200) / 2 + 20, (screen_height - 100) / 2 + 20))
            self.restart_text = self.font.render("Restart", True, (255, 255, 255))
            self.restart_text_rect = self.restart_text.get_rect(topleft=((screen_width - 200) / 2 + 20, (screen_height - 100) / 2 + 50))
            self.leaderboard_text = self.font.render("leaderboard",True, (255, 255, 255))
            self.leaderboard_text_rect = self.leaderboard_text.get_rect(topleft=((screen_width - 200) / 2 + 20, (screen_height - 100) / 2 + 80))
            self.quit_text = self.font.render("Quit", True, (255, 255, 255))
            self.quit_text_rect = self.quit_text.get_rect(topleft=((screen_width - 200) / 2 + 20, (screen_height - 100) / 2 + 110))

            # Set the dimensions and position of the menu background
            menu_width = 200
            menu_height = 100
            menu_x = (screen_width - menu_width) / 2
            menu_y = (screen_height - menu_height) / 2

            # Draw the menu background
            pygame.draw.rect(self.screen, (0, 0, 0), (menu_x, menu_y, menu_width, menu_height))

            # Display the menu options
            self.screen.blit(self.game_status_text, self.game_status_text_rect)
            self.screen.blit(self.resume_text, self.resume_text_rect)
            self.screen.blit(self.restart_text, self.restart_text_rect)
            self.screen.blit(self.leaderboard_text,self.leaderboard_text_rect)
            self.screen.blit(self.quit_text, self.quit_text_rect)

            # Update the display
            pygame.display.update()


        def restart_button_clicked(self, pos):
            global Mastermind, roundbutton
            if self.restart_text_rect.collidepoint(pos):
                main()
        def pause_button_clicked(self,pos):
            if  self.resume_text_rect.collidepoint(pos):
                self.game_paused = not self.game_paused
                return True
            return False
        def leaderboard_button_clicked(self,pos):
            if self.leaderboard_text_rect.collidepoint(pos):
                return True
        def quit_button_clicked(self,pos):
            if self.quit_text_rect.collidepoint(pos):
                return True
        
    class Square:
        def __init__(self, x, y, sizex,sizey, color,colors =  [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (0, 255, 255), (255, 0, 255)],text = "", font =  pygame.font.Font('freesansbold.ttf', 32)):
            self.colors =  colors
            self.x = x
            self.y = y
            self.width= sizex
            self.height = sizey
            self.color = color
            self.rect = pygame.Rect(self.x,self.y,self.width,self.height)
            self.text = text
            self.font =font
            self.tempx = self.x + self.width // 2
            self.tempy =self.y + self.height // 2
            self.position = (self.x, self.y,self.width, self.height)
        def draw(self, screen):
            pygame.draw.rect(screen, self.color,self.position)
            text_surface = self.font.render(self.text,True,(255,255,255))
            text_rect = text_surface.get_rect()
            text_rect.center = (self.tempx, self.tempy)
            screen.blit(text_surface, text_rect)
        def clicked(self, pos):
            # Check if the square was clicked by checking if the mouse position is inside the square
            if int(self.x) <= int(pos[0]) <= int(self.x + self.width) and self.y <= int(pos[1]) <= int(self.y + self.height) and Mastermind.round*100 == self.y:
                if self.colors.index(self.color) + 1 < len(self.colors):
                    self.color = self.colors[self.colors.index(self.color) + 1]
                else:
                    self.color = self.colors[0]

    # Create four squares
    class Row:
        def __init__(self,row,colors=[(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (0, 255, 255), (255, 0, 255)]):
            self.grey = (128,128,128)
            self.squares = [Square(100, row*100, 50,50, colors[0]), Square(200, row*100, 50,50, colors[1]), Square(300, row*100, 50,50, colors[2]), Square(400, row*100, 50,50, colors[3])]
            self.identifiers = [Square(0, row*100+20,20 ,20, self.grey), Square(50, row*100+20,20, 20, self.grey), Square(475, row*100+20,20, 20, self.grey), Square(525, row*100+20, 20,20, self.grey)]


    class Game(PauseMenu,Leaderboard):
        def __init__(self) -> None:
            PauseMenu.__init__(self)

            # Define a list of colors to cycle through
            self.savemenuclicked = False
            self.loadmenuclicked = False
            self.colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (0, 255, 255), (255, 0, 255)]
            self.randomcolors = [random.sample(self.colors,1)[0] for i in range(4)]
            print(self.randomcolors)
            self.round = 1
            self.currentrow = Row(self.round,self.colors)
            self.all_rows = [self.currentrow]
            self.status = 0
            
            pass

        def get_round(self):
            return self.round
 
                    

        def eventhandling(self):
            global menuopened,justclosed
            menuopened = False
            justclosed = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                elif event.type == pygame.MOUSEBUTTONUP:

                    if not self.game_paused:
                        self.status = roundbutton.clicked(event.pos,self.randomcolors)[1]
                        for row in self.all_rows:
                            for square in row.squares:
                                    square.clicked(event.pos)
                    if self.game_paused:
                        if self.quit_button_clicked(event.pos):
                            pygame.quit()
                            sys.exit()
                        self.restart_button_clicked(event.pos)
                        if self.pause_button_clicked(event.pos):
                            if self.game_paused:
                                self.hide_pause_menu()
                            else:
                                self.show_pause_menu()
                        if self.leaderboard_button_clicked(event.pos):
                            self.show_leaderboard()
                            self.x_pos = 100
                            self.y_pos = 100
                            


                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_ESCAPE:
                        self.game_paused = not self.game_paused
                        if self.game_paused:
                            self.show_pause_menu()
                        else:
                            self.hide_pause_menu()

                    
        def update_screen(self):

            for row in self.all_rows:
                for square in row.squares:
                        square.draw(screen)
                for square in row.identifiers:
                    square.draw(screen)
                roundbutton.draw(screen)

        def Gameloop(self):
            just_resumed = False
            self.just_opened_savemenu = False
            self.just_opened_loadmenu = False
            self.show_pause_menu()
            self.hide_pause_menu()
            mysterycolor = pygame.image.load("questionbox.png").convert()
            mysterycolor = pygame.transform.scale(mysterycolor,(50,50))
            while True:
                self.eventhandling()
              
                if not PauseMenu.Return_game_paused(self):
                    if just_resumed:
                        PauseMenu.hide_pause_menu(self)
                        just_resumed = False
                        
                    else:
                        self.update_screen()
                        if self.status == -1:
                            self.squares = [Square(100, 0, 50,50, self.randomcolors[0]).draw(screen), Square(200, 0, 50,50, self.randomcolors[1]).draw(screen), Square(300, 0, 50,50, self.randomcolors[2]).draw(screen), Square(400, 0, 50,50, self.randomcolors[3]).draw(screen)]
                            self.game_status = "Game Won!"

                        elif self.get_round() >=9:
                            self.squares = [Square(100, 0, 50,50, self.randomcolors[0]).draw(screen), Square(200, 0, 50,50, self.randomcolors[1]).draw(screen), Square(300, 0, 50,50, self.randomcolors[2]).draw(screen), Square(400, 0, 50,50, self.randomcolors[3]).draw(screen)]
                            self.game_status = "Game Over!"

                            
                        else:
                            screen.blit(mysterycolor,(100,0))
                            screen.blit(mysterycolor,(200,0))
                            screen.blit(mysterycolor,(300,0))
                            screen.blit(mysterycolor,(400,0))

                        
                else:
                    if not just_resumed:
                        screen.fill((0,0,0))
                        PauseMenu.show_pause_menu(self)
                        just_resumed = True
                        if menuopened:
                            self.show_leaderboard()
                        else:
                            if justclosed:
                                self.hide_leaderboard(justclosed)
                    

                pygame.display.update()

    class Nextround(Game):
        def __init__(self, round):
            self.font = pygame.font.Font(None, 25)
            self.x = 500
            self.round = round
            self.y = 600
            self.size = 20
            self.currentcolors = []
            self.next_round_text = self.font.render("Reveal", True, (0,0,0))
            self.next_round_rect = self.next_round_text.get_rect(topleft=(self.x ,self.y))
        def draw(self, screen):
            pygame.draw.rect(screen, (255, 255, 255), (self.x, self.y, 60, self.size))
            screen.blit(self.next_round_text,self.next_round_rect)
            pygame.display.update()
        def clicked(self, pos, randcolors):
            count = 0
            self.randcolors = randcolors
            if self.next_round_rect.collidepoint(pos):
                Mastermind.round +=1
                self.round += 1
                for i in range(0,4):
                    # Check if the current square's color matches the corresponding color in the randcolors list
                    if Mastermind.currentrow.squares[i].color == self.randcolors[i]:
                        Mastermind.currentrow.identifiers[i].color = (255,255,255)
                        count += 1

                    # Check if the current square's color is present in the randcolors list, but not in the correct position
                    elif Mastermind.currentrow.squares[i].color in self.randcolors:
                        Mastermind.currentrow.identifiers[i].color = (255,0,0)
                    # If the current square's color is not present in the randcolors list
                    else:
                        Mastermind.currentrow.identifiers[i].color = (128,128,128)
                # If all the colors match, return -1
                justwon = False
                if count == 4:
                    with open("leaderboarddata","rb") as f:
                        newlist = pickle.load(f)
                    newlist.append([name,str(self.round-1)])
                    justwon = True
                    if justwon:
                        with open("leaderboarddata","wb") as f:
                            pickle.dump(newlist,f)
                        return [self.round,-1,True]
                        justwon = False
                    
                elif count == 4 and justwon == True:
                    justwon = False
                # Create a new row of squares
                new_row = Row(self.round,Mastermind.colors)
                # Add the new row to the list of all rows
                Mastermind.all_rows.append(new_row)
                # Update the currentrow attribute to point to the new row
                Mastermind.currentrow = new_row
                return [self.round,self.round,True]
            return [self.round,self.round,False]
    Mastermind = Game()
    roundbutton = Nextround(1)
    Mastermind.Gameloop()

main()
