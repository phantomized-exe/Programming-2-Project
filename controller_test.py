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
            #print(event)
            if event.button == 0:
                print("A pressed")
            elif event.button == 1:
                print("B pressed")
            elif event.button == 2:
                print("X pressed")
            elif event.button == 3:
                print("Y pressed")
        if event.type == pygame.JOYBUTTONUP:
            print(event)
        if event.type == pygame.JOYAXISMOTION:
            #print(event)
            if event.axis < 2:
                x = joysticks[event.joy].get_axis(0)
                y = joysticks[event.joy].get_axis(1)
                if y < -.5 and abs(x) < .5:
                    print("Up")
                elif y > .5 and abs(x) < .5:
                    print("Down")
                elif x < -.5 and abs(y) < .5:
                    print("Left")
                elif x > .5 and abs(y) < .5:
                    print("Right")
                elif x < -.5 and y < -.5:
                    print("Up-Left")
                elif x > .5 and y < -.5:
                    print("Up-Right")
                elif x < -.5 and y > .5:
                    print("Down-Left")
                elif x > .5 and y > .5:
                    print("Down-Right")
        if event.type == pygame.JOYHATMOTION:
            print(event)