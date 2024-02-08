import pygame
import sys
import numpy as np
import pygame_gui

WIDTH, HEIGHT = 1200, 600
RADIUS = 10
MASS = 10
PIXELS_PER_METER = 1e2

pygame.init()
pygame.display.set_caption('Projectile Simulation')
screen = pygame.display.set_mode((WIDTH, HEIGHT))
manager = pygame_gui.UIManager((WIDTH, HEIGHT))

catapult = {'pos': np.array([50, HEIGHT - 50]), 'angle': 45, 'vel': 10}
settings = {'gravity': 9.81, 'wind': 0.0, 'friction': 0.0}

sliders = {
    'angle': pygame_gui.elements.UIHorizontalSlider(
        relative_rect=pygame.Rect((50, 50), (200, 20)), start_value=45, value_range=(10, 90), manager=manager),
    'velocity': pygame_gui.elements.UIHorizontalSlider(
        relative_rect=pygame.Rect((50, 100), (200, 20)), start_value=10, value_range=(0, 20), manager=manager),
    'gravity': pygame_gui.elements.UIHorizontalSlider(
        relative_rect=pygame.Rect((50, 150), (200, 20)), start_value=9.81, value_range=(0, 20), manager=manager),
    'wind': pygame_gui.elements.UIHorizontalSlider(
        relative_rect=pygame.Rect((50, 200), (200, 20)), start_value=0.0, value_range=(-10, 10), manager=manager),
    'friction': pygame_gui.elements.UIHorizontalSlider(
        relative_rect=pygame.Rect((50, 250), (200, 20)), start_value=0.0, value_range=(0, 1), manager=manager),
}

labels = {
    'angle': pygame_gui.elements.UILabel(
        relative_rect=pygame.Rect((50, 30), (200, 20)), text='Angle', manager=manager),
    'velocity': pygame_gui.elements.UILabel(
        relative_rect=pygame.Rect((50, 80), (200, 20)), text='Velocity', manager=manager),
    'gravity': pygame_gui.elements.UILabel(
        relative_rect=pygame.Rect((50, 130), (200, 20)), text='Gravity', manager=manager),
    'wind': pygame_gui.elements.UILabel(
        relative_rect=pygame.Rect((50, 180), (200, 20)), text='Wind', manager=manager),
    'friction': pygame_gui.elements.UILabel(
        relative_rect=pygame.Rect((50, 230), (200, 20)), text='Friction', manager=manager),
}

balls = []

clock = pygame.time.Clock()
while True:
    time_delta = clock.tick(60)/1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_HORIZONTAL_SLIDER_MOVED:
                if event.ui_element == sliders['angle']:
                    catapult['angle'] = event.value
                elif event.ui_element == sliders['velocity']:
                    catapult['vel'] = event.value
                elif event.ui_element == sliders['gravity']:
                    settings['gravity'] = event.value
                elif event.ui_element == sliders['wind']:
                    settings['wind'] = event.value
                elif event.ui_element == sliders['friction']:
                    settings['friction'] = event.value
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                angle_rad = np.radians(catapult['angle'])
                initial_velocity = catapult['vel'] * \
                    np.array([np.cos(angle_rad), -np.sin(angle_rad)])
                balls.append({'pos': np.array(
                    catapult['pos'], dtype=float), 'vel': initial_velocity, 'mass': MASS})

        manager.process_events(event)

    for ball in balls:
        ball['vel'][1] += settings['gravity'] / PIXELS_PER_METER
        ball['vel'][0] += settings['wind'] / PIXELS_PER_METER
        ball['vel'] *= 1 - settings['friction']
        ball['pos'] += ball['vel']

    screen.fill((0, 0, 0))
    for ball in balls:
        pygame.draw.circle(screen, (255, 255, 255), (int(
            ball['pos'][0]), int(ball['pos'][1])), RADIUS)
    manager.update(time_delta)
    manager.draw_ui(screen)
    pygame.display.flip()
