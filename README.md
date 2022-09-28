# Pygame screen recorder util for making gifs out of pygame-based simulations
___
## How to Use
**Quick start:**
```
# other imports
import pygame_screen_recorder
...
# init pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
...
rec = pygame_screen_recorder("<OUTPUT_FILENAME>") # init recorder object
...
## Game loop
running = True
while running:

    # draw code

    rec.click(screen) # save frame as png to _temp_/ folder

    pygame.display.flip()       

rec.save() # compiles temp folder to a .gif at specified location and cleans up
pygame.quit()
```

## Requirements 
- imageio
- pygame