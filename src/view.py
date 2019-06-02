import pygame
import queue

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WOOD = (255,211,155)
BROWN = (94, 9, 9)

 
# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 44
HEIGHT = 44 
# This sets the margin between each cell
MARGIN = 2

class View():
    def __init__(self,eventos,tablero):
        self.grid = tablero
        self.eventos = eventos
    
    def iniciar(self):
        # Set row 1, cell 5 to one. (Remember rows and
        # column numbers start at zero.)
        
        # Initialize pygame
        pygame.init()
        
        # Set the HEIGHT and WIDTH of the screen
        WINDOW_SIZE = [600, 450]
        screen = pygame.display.set_mode(WINDOW_SIZE)
        # Set title of screen
        pygame.display.set_caption("Go Board Game")
        
        # Loop until the user clicks the close button.
        done = False
        
        # Used to manage how fast the screen updates
        clock = pygame.time.Clock()
        while not done:
            done = self.dibujar_tablero(screen)
            print("==================\n")
            print(self.grid)
            print("==================\n")

            clock.tick(60)
            # Go ahead and update the screen with what we've drawn.
            pygame.display.flip()
        pygame.quit()
 

    def dibujar_tablero(self, screen):
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                done = True  # Flag that we are done so we exit this loop
                return done
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # User clicks the mouse. Get the position
                pos = pygame.mouse.get_pos()
                # Change the x/y screen coordinates to grid coordinates
                column = pos[0] // (WIDTH + MARGIN)
                row = pos[1] // (HEIGHT + MARGIN)
                #self.events_mutex.acquire()
                self.eventos.put((row,column))
                #self.events_mutex.release()
                
                # Set that location to one
                #self.grid[row][column] = 1
                print("Click ", pos, "Grid coordinates: ", row, column)
 
        # Set the screen background
        screen.fill(BROWN)
 
        # Draw the grid
        for row in range(8):
            for column in range(8):
                color = WOOD
                #if grid[row][column] == 1:
                    #color = GREEN
                #   pygame.draw.circle(screen,(0,0,0),((MARGIN + WIDTH) * column + MARGIN,(MARGIN + HEIGHT) * row + MARGIN),25)
                pygame.draw.rect(screen,
                                color,
                                [(MARGIN + WIDTH) * column + MARGIN + 20,
                                (MARGIN + HEIGHT) * row + MARGIN + 20,
                                WIDTH,
                                HEIGHT])
        for row in range(9):
            for column in range(9):
                if self.grid[row][column] == 'N':
                    pygame.draw.circle(screen,BLACK,((MARGIN + WIDTH) * column + MARGIN + 20,
                                (MARGIN + HEIGHT) * row + MARGIN + 20), 17)
                elif self.grid[row][column] == 'B':
                    pygame.draw.circle(screen,WHITE,((MARGIN + WIDTH) * column + MARGIN + 20,
                                (MARGIN + HEIGHT) * row + MARGIN + 20), 17)

                else:
                    pygame.draw.circle(screen,RED,((MARGIN + WIDTH) * column + MARGIN + 20,
                                (MARGIN + HEIGHT) * row + MARGIN + 20), 5)



    def main(self):
        self.iniciar()

if __name__ == "__main__":
    v = View()
    v.main()


 

