import sys, os, math
import pygame

import plot
from geometry import *
from render import *
        

def update(elapsed, delta, camera):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        camera.move(0, -0.5 * delta, 0)
    if keys[pygame.K_DOWN]:
        camera.move(0, 0.5 * delta, 0)
    if keys[pygame.K_RIGHT]:
        camera.move(0.5 * delta, 0, 0)
    if keys[pygame.K_LEFT]:
        camera.move(-0.5 * delta, 0, 0)
        
    mouse_rel = Vec2(*pygame.mouse.get_rel())
    
    if pygame.mouse.get_pressed()[0]:
        camera.move(-mouse_rel.x, -mouse_rel.y, 0)

def main():
    os.environ["SDL_VIDEO_CENTERED"] = "1"
    pygame.init()
    pygame.display.set_caption("Harmonics")
    pygame.display.set_icon(
        pygame.transform.scale(
            pygame.image.load(os.path.join("img", "icon.png")),
            (32, 32)
        )
    )
    window = pygame.display.set_mode(
        (WIDTH, HEIGHT),
        pygame.DOUBLEBUF |
        pygame.HWSURFACE |
        pygame.RESIZABLE
    )

    pygame.cursors.sizer_xy = [(24, 16), (8, 8)]
    pygame.cursors.sizer_xy.extend(
        pygame.cursors.compile(pygame.cursors.sizer_xy_strings)
    )
        
    plots = []
    plots.append(plot.saw(Vec2(-H_WIDTH*2, 0), 8, 200, 100, 800, 20))
    plots.append(plot.square(Vec2(-H_WIDTH*2, 0), 8, 200, 100, 800, 20))
    plots[1].color = YELLOW
    
    axes = []
    axes.append(
        Polygon(WHITE, [
                Vec3(-WIDTH, 0, 1),
                Vec3( WIDTH, 0, 1) ])
    )
    axes.append(
        Polygon(WHITE, [
                Vec3(0, -HEIGHT, 1),
                Vec3(0,  HEIGHT, 1) ])
    )

    camera = Camera(
        0, 0, -10, 0.02, 0, 200,
        clamp=Rect(-H_WIDTH, -H_HEIGHT, WIDTH, HEIGHT)
    )

    elapsed_t = pygame.time.get_ticks()
    last_t = elapsed_t
    delta_t = 1 / 60 * 1000
    accumulated_t = 0
    frames = 0
    fps_timer = 0
    fps_interval = 5
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        last_t = elapsed_t
        elapsed_t = pygame.time.get_ticks()
        accumulated_t += elapsed_t - last_t
        
        while accumulated_t >= delta_t:
            accumulated_t -= delta_t
            
            update(elapsed_t, delta_t, camera)
            fps_timer += delta_t
        
        render(window, elapsed_t, axes, camera=camera)
        render(window, elapsed_t, plots, camera=camera)
        frames += 1
        if fps_timer > 1000 * fps_interval:
            print("{:.2f}fps".format(frames / fps_interval))
            frames = 0
            fps_timer = 0
        
        pygame.display.flip()
        window.fill(CARBON)


if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        print("Quitting...")
