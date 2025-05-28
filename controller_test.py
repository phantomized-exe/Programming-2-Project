import pygame
pygame.init()
pygame.joystick.init()
joysticks = []
for i in range(pygame.joystick.get_count()):
    joystick = pygame.joystick.Joystick(i)
    joystick.init()
    joysticks.append(joystick)
    print(f"Detected joystick {joystick.get_name()}")
while True:
    for event in pygame.event.get():
        if event.type == pygame.JOYBUTTONDOWN:
            print(event)
        if event.type == pygame.JOYBUTTONUP:
            print(event)
        if event.type == pygame.JOYAXISMOTION:
            print(event)
        if event.type == pygame.JOYHATMOTION:
            print(event)