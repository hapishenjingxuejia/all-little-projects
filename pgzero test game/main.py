import sys
import pgzrun

WIDTH = 749
HEIGHT = 469

mouse = Actor("mouse")
mouse.x = 300
mouse.y = 300

shutdown = Actor("shutdown")
shutdown.x = 50
shutdown.y = 90


def draw():
    screen.clear()
    screen.blit("bgp", (0, 0))
    screen.draw.text("Zan OS V1.0.01", (20, 10))
    mouse.draw()
    shutdown.draw()


def update():
    if mouse.x < 0 or mouse.x > 749:
        mouse.x = 300
        mouse.y = 300
    if mouse.y < 0 or mouse.y > 469:
        mouse.y = 300
        mouse.x = 300
    if keyboard[keys.UP]:
        mouse.y -= 2
    if keyboard[keys.DOWN]:
        mouse.y += 2
    if keyboard[keys.LEFT]:
        mouse.x -= 2
    if keyboard[keys.RIGHT]:
        mouse.x += 2
    if keyboard[keys.SPACE]:
        sys.exit()


pgzrun.go()