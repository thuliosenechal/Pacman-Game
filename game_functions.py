import pygame
import settings
import sys
import game


def check_keydown_events(event, hero_sprites):
    """Responde a pressionamentos de tecla."""
    if event.key == pygame.K_LEFT:
        for hero in hero_sprites:
            hero.changeSpeed([-1, 0])
            hero.is_move = True
    elif event.key == pygame.K_RIGHT:
        for hero in hero_sprites:
            hero.changeSpeed([1, 0])
            hero.is_move = True
    elif event.key == pygame.K_UP:
        for hero in hero_sprites:
            hero.changeSpeed([0, -1])
            hero.is_move = True
    elif event.key == pygame.K_DOWN:
        for hero in hero_sprites:
            hero.changeSpeed([0, 1])
            hero.is_move = True

def check_keyup_events(event, hero_sprites):
    """Responde a solturas de tecla."""
    if (event.key == pygame.K_LEFT) or \
       (event.key == pygame.K_RIGHT) or \
        (event.key == pygame.K_UP) or \
        (event.key == pygame.K_DOWN):

        for hero in hero_sprites:
            hero.is_move = False

def start_level_game(level, screen, font):
    ai_settings = settings.Settings()
    clock = pygame.time.Clock()
    SCORE = 0
    wall_sprites = level.setup_walls(ai_settings.skyblue)
    gate_sprites = level.setup_gate(ai_settings.white)
    hero_sprites, ghost_sprites = level.setup_players(ai_settings.pacman, [ai_settings.blinky,ai_settings.clyde,ai_settings.inky,ai_settings.pinky])
    food_sprites = level.setup_food(ai_settings.yellow, ai_settings.white)
    is_clearance = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(-1)
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                check_keydown_events(event, hero_sprites)

            if event.type == pygame.KEYUP:
                check_keyup_events(event, hero_sprites)

        screen.fill(ai_settings.black)
        for hero in hero_sprites:
            hero.update(wall_sprites, gate_sprites)
        hero_sprites.draw(screen)

        for hero in hero_sprites:
            food_eaten = pygame.sprite.spritecollide(hero, food_sprites, True)
        SCORE += len(food_eaten)
        wall_sprites.draw(screen)
        gate_sprites.draw(screen)
        food_sprites.draw(screen)

        for ghost in ghost_sprites:
            if ghost.tracks_loc[1] < ghost.tracks[ghost.tracks_loc[0]][2]:
                ghost.changeSpeed(ghost.tracks[ghost.tracks_loc[0]][0: 2])
                ghost.tracks_loc[1] += 1
            else:
                if ghost.tracks_loc[0] < len(ghost.tracks) - 1:
                    ghost.tracks_loc[0] += 1
                elif ghost.role_name == 'Clyde':
                    ghost.tracks_loc[0] = 2
                else:
                    ghost.tracks_loc[0] = 0
                ghost.changeSpeed(ghost.tracks[ghost.tracks_loc[0]][0: 2])
                ghost.tracks_loc[1] = 0
            if ghost.tracks_loc[1] < ghost.tracks[ghost.tracks_loc[0]][2]:
                ghost.changeSpeed(ghost.tracks[ghost.tracks_loc[0]][0: 2])
            else:
                if ghost.tracks_loc[0] < len(ghost.tracks) - 1:
                    loc0 = ghost.tracks_loc[0] + 1
                elif ghost.role_name == 'Clyde':
                    loc0 = 2
                else:
                    loc0 = 0
                ghost.changeSpeed(ghost.tracks[loc0][0: 2])
            ghost.update(wall_sprites, None)
        ghost_sprites.draw(screen)
        score_text = font.render("Score: %s" % SCORE, True, ai_settings.red)
        screen.blit(score_text, [10, 10])

        if len(food_sprites) == 0:
            is_clearance = True
            break
        if pygame.sprite.groupcollide(hero_sprites, ghost_sprites, False, False):
            is_clearance = False
            break
        pygame.display.flip()
        clock.tick(10)
    return is_clearance

def show_text(screen, font, is_clearance, flag=False):
    ai_settings = settings.Settings()
    clock = pygame.time.Clock()
    msg = 'Game Over!' if not is_clearance else 'Congratulations, you won!'
    if not is_clearance:
        positions = [[235, 233], [65, 303], [170, 333]]
    else:
        positions = [[145, 233], [65, 303], [170, 333]]
    surface = pygame.Surface((400, 200))
    surface.set_alpha(10)
    surface.fill((128, 128, 128))
    screen.blit(surface, (100, 200))
    texts = [font.render(msg, True, ai_settings.white),
             font.render('Press ENTER to continue or play again.', True, ai_settings.white),
             font.render('Press ESCAPE to quit.', True, ai_settings.white)]
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if is_clearance:
                        if not flag:
                            return
                        else:
                            game.run_game()
                    else:
                        game.run_game()
                elif event.key == pygame.K_ESCAPE:
                    sys.exit()
                    pygame.quit()
        for idx, (text, position) in enumerate(zip(texts, positions)):
            screen.blit(text, position)
        pygame.display.flip()
        clock.tick(10)