import pygame
import levels
from settings import Settings
import game_functions as gf


def run_game():
    # Inicializa o pygame, as configurações e o objeto screen
    pygame.init()
    pygame.mixer.init()
    pygame.font.init()
    ai_settings = Settings()
    level = levels.Level1()

    pygame.display.set_icon(ai_settings.icon_image)
    screen = pygame.display.set_mode([ai_settings.screen_width, ai_settings.screen_height])
    pygame.display.set_caption(ai_settings.display_name)

    pygame.mixer.music.load(ai_settings.set_music)
    pygame.mixer.music.play(-1, 0.0)

    for num_level in range(1, levels.numlevels + 1):
        if num_level == 1:
            is_clearance = gf.start_level_game(level, screen, ai_settings.font_small)
            if num_level == levels.numlevels:
                gf.show_text(screen, ai_settings.font_big, is_clearance, True)
            else:
                gf.show_text(screen, ai_settings.font_big, is_clearance)


if __name__ == '__main__':
    run_game()
