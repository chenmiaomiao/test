import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
# from OpenGL.raw.GLX._types import Display
# from idlelib.idle_test.mock_tk import Event

vertices = (
             (-1, -1, -1),
             (1, -1, -1),
             (1, -1, 1),
             (-1 ,-1, 1),
             (-1, 1, -1),
             (1, 1, -1),
             (1 ,1 ,1),
             (-1, 1, 1)
             )

edges = (
        (0, 1),
        (0, 3),
        (0, 4),
        (2, 1),
        (2, 3),
        (2, 6),
        (5, 1),
        (5, 4),
        (5, 6),
        (7, 3),
        (7, 4),
        (7, 6)
        )

surfaces = (
            (0, 1, 2, 3),
            (2, 3, 7, 6),
            (7, 6, 4, 5),
            (4, 5, 1, 0),
            (1, 2, 6, 5),
            (0, 3, 7, 4)
            )

def Draw_Cube():
    glBegin(GL_QUADS)
    for surface in surfaces:
        for vertex in surface:
            glColor3fv((0, 1, 0))
            glVertex3fv(vertices[vertex])
    glEnd()

    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glColor3fv((1, 0, 0))
            glVertex3fv(vertices[vertex])
    glEnd()
    
def main():
    pygame.init()
    display = (800, 600)
    
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    gluPerspective(45.0, (display[0]/display[1]), 1, 50.0)
    glTranslatef(0.0, 0.0, -5.0)
    glRotatef(20, 45, 0, 0)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Draw_Cube()
        pygame.display.flip()
        pygame.time.wait(10)
    
main()