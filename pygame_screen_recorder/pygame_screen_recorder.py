import imageio 
import os 
import pygame
import random

class pygame_screen_recorder:
    def __init__(self, outfile):
        self.outfile = outfile
        self.file_count = 0
        # make a temp folder with a uuid
        self.temp_folder = f'.__temp_gif{random.randint(0, 1000000)}'
        os.mkdir(self.temp_folder)

    def click(self, screen):
        fn = f"{self.temp_folder}/{self.file_count}.png"
        pygame.image.save(screen, fn)
        self.file_count += 1

    def save(self):
        files = os.listdir(self.temp_folder)
        files = sorted(files, key=lambda x: int(os.path.splitext(x)[0]))
        print(files)
        images = []
        for filename in files:
            images.append(imageio.imread(f'./{self.temp_folder}/{filename}'))
        imageio.mimsave(self.outfile, images)

    def __del__(self):
        # delete all files in temp folder
        files = os.listdir(self.temp_folder)
        for filename in files:
            os.remove(f'./{self.temp_folder}/{filename}')
        os.rmdir(self.temp_folder)

