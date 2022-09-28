# Pygame screen recorder util for making gifs out of pygame-based simulations

<img src="test.gif"/>
## How to Use
### Install
```
pip3 install pygame-screen-recorder
```

**Quick start:**
```
# other imports
from pygame_screen_recorder import pygame_screen_recorder as pgr
...
# init pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
...
recrdr = pgr("<OUTPUT_FILENAME>") # init recorder object
...
## Game loop
running = True
while running:

    # draw code

    recrdr.click(screen) # save frame as png to _temp_/ folder

    pygame.display.flip()       

recrdr.save() # compiles temp folder to a .gif at specified location and cleans up
pygame.quit()
```

## Requirements 
- imageio
- pygame
