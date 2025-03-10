# -- Pygame Game Template -- #

import pygame
import sys
import config # Import the config module 
import random
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
#----- Functions -----#
# -- Draw rectangle --#
def draw_rect(screen, color, rect, thickness): 
   pygame.draw.rect(screen, color , rect, thickness)

#----Draw Text ----#
def draw_text(screen, text, font, text_col, x, y):
   
   img = font.render(text, True, text_col)
   screen.blit(img, (x, y))


def main():
   screen = init_game()
   clock = pygame.time.Clock() # Initialize the clock here
   txt_font1 = pygame.font.SysFont("Ariel", 25)

   running = True
   while running:
      running = handle_events()
      screen.fill(config.BLACK) # Use color from config

   #----- shapes -----#
      # --- Stars --- #
      for offset in range(0,800,40):
         rect = [30+offset, 155, 5, 5]
         pygame.draw.rect(screen, config.WHITE, rect, 0)
         rect = [10+offset, 125, 5, 5]
         pygame.draw.rect(screen, config.WHITE, rect, 0)
         rect = [30+offset, 95, 5, 5]
         pygame.draw.rect(screen, config.WHITE, rect, 0)
         rect = [10+offset, 65, 5, 5]
         pygame.draw.rect(screen, config.WHITE, rect, 0)
         rect = [30+offset, 35, 5, 5]
         pygame.draw.rect(screen, config.WHITE, rect, 0)
         rect = [10+offset, 5, 5, 5]
         pygame.draw.rect(screen, config.WHITE, rect, 0)

      # --- City --- #
      rect = [0, 115 ,90, 275]
      draw_rect(screen, (50,50,50), rect,0)
      rect = [95, 135 ,90, 255]
      draw_rect(screen, (50,50,50), rect,0)
      rect = [190, 155 ,90, 235]
      draw_rect(screen, (50,50,50), rect,0)
      rect = [285, 85 ,90, 305]
      draw_rect(screen, (50,50,50), rect,0)
      rect = [380, 45 ,90, 345]
      draw_rect(screen, (50,50,50), rect,0)
      rect = [475, 135 ,90, 255]
      draw_rect(screen, (50,50,50), rect,0)
      rect = [570, 105 ,90, 285]
      draw_rect(screen, (50,50,50), rect,0)
      rect = [665, 235 ,90, 155]
      draw_rect(screen, (50,50,50), rect,0)
      rect = [760, 135 ,90, 255]
      draw_rect(screen, (50,50,50), rect,0)

      #--- lights ---#
      lighton = random.randint(1,2)
      if lighton == True:
         rect1 = [60, 135 ,20, 20]
         lighton = draw_rect(screen, (236,183,83), rect1,0)
      else:
         rect1 = [60, 135 ,20, 20]
         lighton = draw_rect(screen, (10,10,10), rect1,0)

      #--- water ---#
      my_rect1 = [-100, 390, 9500, 350]
      border_radius = 50
      thickness_r = 0
      pygame.draw.rect(screen, config.BLUE, my_rect1, thickness_r, border_radius)

      #--- land ---#
      rect = [0, 379 ,900, 15]
      draw_rect(screen, (20, 95, 20), rect,0)

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

      #--- Sign ---#
      rect = [197, 345 ,195, 100]
      draw_rect(screen, (170, 95, 20), rect,0)
      rect = [280, 345 ,30, 150]
      draw_rect(screen, (170, 95, 20), rect,0)

      #--- Text ---#
      draw_text(screen, "Braden Leach, Buckley", txt_font1, (180,180,180), 200, 390)
   #----------------------------------------------------------------------------------------------------------------#
      pygame.display.flip()

      # -- Limit the frame rate to the specified frames per second (FPS) -- #
      clock.tick(10) # Use the clock to control the frame rate

   pygame.quit()
   sys.exit()

if __name__ == "__main__":
   main()