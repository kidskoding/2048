overlay = pygame.Surface((dim, dim))
        overlay.set_alpha(128)
        overlay.fill((187, 173, 160))
        screen.blit(overlay, (0, 0))
        
        font = pygame.font.Font(None, 74)
        text = font.render('Game Over', True, (119, 110, 101))
        text_rect = text.get_rect(center=(dim / 2, dim / 2 - 70))
        screen.blit(text, text_rect)
        
        rect_width = 200
        rect_height = 50
        
        play_again_rect = pygame.Rect(dim / 2 - rect_width / 2, dim / 2 - 20, rect_width, rect_height)
        text = font.render('Play Again', True, (119, 110, 101))
        text_rect = text.get_rect(center=play_again_rect.center)
        pygame.draw.rect(screen, (187, 173, 160), play_again_rect)
        screen.blit(text, text_rect)
        
        quit_rect = pygame.Rect(dim / 2 - rect_width / 2, dim / 2 + 50, rect_width, rect_height)
        text = font.render('Quit', True, (119, 110, 101))
        text_rect = text.get_rect(center=quit_rect.center)
        pygame.draw.rect(screen, (187, 173, 160), quit_rect)
        screen.blit(text, text_rect)