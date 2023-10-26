import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import random
def draw_pyramid(color):
    glBegin(GL_TRIANGLES)
    glColor3fv(color)
    # Base
    glVertex3f(-1.0, -1.0, -1.0)
    glVertex3f(1.0, -1.0, -1.0)
    glVertex3f(0.0, 1.0, 0.0)
    
    # Side 1
    glVertex3f(1.0, -1.0, -1.0)
    glVertex3f(1.0, -1.0, 1.0)
    glVertex3f(0.0, 1.0, 0.0)
    
    # Side 2
    glVertex3f(1.0, -1.0, 1.0)
    glVertex3f(-1.0, -1.0, 1.0)
    glVertex3f(0.0, 1.0, 0.0)
    
    # Side 3
    glVertex3f(-1.0, -1.0, 1.0)
    glVertex3f(0.0, -1.0, -1.0)
    glVertex3f(0.0, 1.0, 0.0)
    
    glEnd()

def draw_ground_plane():
    glBegin(GL_QUADS)
    glColor3f(0.5, 0.5, 0.5)  # Color for the ground plane
    glVertex3f(-2, -1, -2)
    glVertex3f(2, -1, -2)
    glVertex3f(2, -1, 2)
    glVertex3f(-2, -1, 2)
    glEnd()
def toggle_rotation():
    global angle
    global rotation_enabled
    rotation_enabled = not rotation_enabled
    if angle == 0:
        angle = 2
    else:
        angle = 0
def setup_light():
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_COLOR_MATERIAL)
    glLightfv(GL_LIGHT0, GL_POSITION, (0, 1.0, 1.0, 1.0))

def increase_rotation_speed():
    global angle
    angle += 1

def decrease_rotation_speed():
    global angle

    if angle > 1:
        angle -= 1
 

rotation_enabled = True  

rotation_axis_x = [1, 0, 0]  
rotation_axis_y = [0, 1, 0] 
current_rotation_axis = rotation_axis_x
angle = 2

figure_color = [random.random(), random.random(), random.random()]
def change_figure_color():
    global figure_color
    figure_color = [random.random(), random.random(), random.random()]
def main():
    global current_rotation_axis, angle

    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)
    setup_light()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:

                    current_rotation_axis = (
                        rotation_axis_y if current_rotation_axis == rotation_axis_x else rotation_axis_x
                    )
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    change_figure_color()
                elif event.button == 3:  # Right mouse button
                    toggle_rotation()  # Start/stop rotation
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 4:  # Scroll wheel up
                    increase_rotation_speed()  # Increase rotation speed
                elif event.button == 5:  # Scroll wheel down
                    decrease_rotation_speed()  # Decrease rotation speed
        if rotation_enabled:
            glRotatef(angle, *current_rotation_axis) 
                    
        
        glRotatef(angle, *current_rotation_axis)  
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        
        draw_pyramid(figure_color)
        
        pygame.display.flip()
        pygame.time.wait(10)
        
if __name__ == "__main__":
    main()