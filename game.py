# -- Pygame Game Template -- #

import pygame
import sys
import config # Import the config module 
def init_game (): 
    pygame.init()
    screen = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT)) # Use constants from config
    pygame.display.set_caption(config.TITLE)
    return screen


def handle_events ():
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
          return False
       elif event.type == pygame.KEYDOWN:
          if event.key == pygame.K_ESCAPE:
             return False
    return True


def draw_rect(screen, color, rect, thickness): 
   pygame.draw.rect(screen, color , rect, thickness)




def main():
   screen = init_game()
   clock = pygame.time.Clock() # Initialize the clock here
   running = True
   while running:
      running = handle_events()
      screen.fill(config.BLACK) # Use color from config


   #---------------shapes-------------------#
      # --- Stars --- #




      # --- City --- #
      rect = [0, 115 ,90, 275]
      draw_rect(screen, (50,50,50), rect,0)
      pygame.draw.rect(screen, (50, 50, 50), [95, 135 ,90, 255])
      pygame.draw.rect(screen, (50, 50, 50), [190, 155 ,90, 235])
      pygame.draw.rect(screen, (50, 50, 50), [285, 85 ,90, 305])
      pygame.draw.rect(screen, (50, 50, 50), [380, 45 ,90, 345])
      pygame.draw.rect(screen, (50, 50, 50), [475, 135 ,90, 255])
      pygame.draw.rect(screen, (50, 50, 50), [570, 105 ,90, 285])
      pygame.draw.rect(screen, (50, 50, 50), [665, 235 ,90, 155])
      pygame.draw.rect(screen, (50, 50, 50), [760, 135 ,90, 255])
      #--- water ---#
      my_rect1 = [-100, 390, 9500, 350]
      border_radius = 50
      thickness_r = 0
      pygame.draw.rect(screen, config.BLUE, my_rect1, thickness_r, border_radius)

      # --- Grass --- #
      circle_center = (400, 900)
      circle_radius = 500
      circle_color = config.BLACK
      circle_thick = 0
      pygame.draw.circle(screen, config.GREEN, circle_center, circle_radius, circle_thick )

      #--- Tree ---#
      pygame.draw.rect(screen, (150, 75, 0), [500, 400 ,30, 45])
      pygame.draw.polygon(screen, config.GREEN,[[590,400], [515, 250], [440, 400]])
      pygame.draw.polygon(screen, config.GREEN,[[590,350], [515, 230], [440, 350]])
   #----------------------------------------#
      


      pygame.display.flip()

      # -- Limit the frame rate to the specified frames per second (FPS) -- #
      clock.tick(config.FPS) # Use the clock to control the frame rate

   pygame.quit()
   sys.exit()

if __name__ == "__main__":
   main()