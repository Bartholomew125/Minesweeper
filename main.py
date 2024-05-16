import pygame as pg
from grid import Grid
from mouse import Mouse

WIDTH = 1000
HEIGHT = 1000

screen = pg.display.set_mode((WIDTH, HEIGHT))

grid = Grid(screen, 50, 50)
mouse = Mouse()

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                running = False
        
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse.left_click = True
        if event.type == pg.MOUSEBUTTONUP:
            if event.button == 1:
                mouse.left_click = False
    
    screen.fill((0,0,0))

    mouse.pos = pg.mouse.get_pos()

    grid.update(mouse)
    grid.draw()




    pg.display.flip()

pg.display.quit()
pg.quit()