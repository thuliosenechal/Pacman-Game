import os
import pygame


icon_path = os.path.join(os.getcwd(), 'resources/images/icon.png')
font_path = os.path.join(os.getcwd(), 'resources/font/ALGER.TTF')

class Settings():
    """Uma classe para armazenar as configurações do jogo."""

    def __init__(self):
        """Inicializa as configurações do jogo."""
        # Configurações de tela
        self.screen_width = 606
        self.screen_height = 606
        self.icon_image = pygame.image.load(icon_path)
        self.display_name = 'Pacman - Senechal Games'

        # Configurações do music
        self.set_music = os.path.join(os.getcwd(), 'resources/sounds/bg.mp3')
        self.set_time_music = (-1, 0.0)

        # Configurações da font
        self.font_small = pygame.font.Font(font_path, 18)
        self.font_big = pygame.font.Font(font_path, 24)

        # Configuração dos players
        self.pacman = os.path.join(os.getcwd(), 'resources/images/pacman.png')
        self.blinky = os.path.join(os.getcwd(), 'resources/images/Blinky.png')
        self.clyde = os.path.join(os.getcwd(), 'resources/images/Clyde.png')
        self.inky = os.path.join(os.getcwd(), 'resources/images/Inky.png')
        self.pinky = os.path.join(os.getcwd(), 'resources/images/Pinky.png')

        # Configuração das cores
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.blue = (0, 0, 255)
        self.green = (0, 255, 0)
        self.red = (255, 0, 0)
        self.yellow = (255, 255, 0)
        self.purple = (255, 0, 255)
        self.skyblue = (0, 191, 255)





