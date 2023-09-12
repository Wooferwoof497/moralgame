# -*- coding: utf-8 -*-
import pygame
import sys
import os

WIDTH, HEIGHT = 600, 450
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Learning")

# colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
MIDGREY = (128, 128, 128)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

FPS = 60
VEL = 2

# assets

PLAYERIMG = pygame.image.load(os.path.join('pythonstuff', 'assets', 'Player.png'))

ENEMYIMG = pygame.image.load(os.path.join('pythonstuff', 'assets', 'Enemy.png'))
ENEMYIMG = pygame.transform.rotate(pygame.transform.scale(ENEMYIMG, (40, 55)), 90)

player = pygame.Rect(100, 300, 16, 41)

class Room:
    def __init__(self, background_image):
        self.background_image = background_image
        self.objects = []
        self.npcs = []


# Define different room backgrounds
main_hub_bg = pygame.transform.scale(pygame.image.load(os.path.join('pythonstuff', 'assets', 'mainhubtemp.png')),
                                     (WIDTH, HEIGHT))
tutorial_bg = pygame.transform.scale(pygame.image.load(os.path.join('pythonstuff', 'assets', 'tutorial.png')),
                                     (WIDTH, HEIGHT))


class MainHubRoom(Room):
    def __init__(self, background_image):
        print("MainHub")
        super().__init__(background_image)        
        player = pygame.Rect(400, 400, 16, 41)
        self.exit_n = pygame.Rect(130, 95, 35, 45)
        # Additional setup for the main hub room

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
           
            if (pygame.Rect.colliderect(player, self.exit_n)):
                print("collide")
                #room_manager.enter_room(tutorial)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_e:
                print("key pressed!")

class Tutorial(Room):
    def __init__(self, background_image):
        print("tutorial")
        super().__init__(background_image)
        self.exit_s = pygame.Rect(140, 400, 35, 50)
        self.player = pygame.Rect(150, 350, 16, 41)

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if self.player.colliderect(self.exit_s):
                room_manager.enter_room(main_hub)
                
  


class RoomManager:
    def __init__(self):
        self.current_room = None

    def enter_room(self, room):
        self.current_room = room


# Create instances of the RoomManager and rooms
room_manager = RoomManager()
main_hub = MainHubRoom(main_hub_bg)
tutorial = Tutorial(tutorial_bg)

# Set start room
current_room = main_hub

# Set the initial current room
room_manager.enter_room(main_hub)


def draw_window(current_room, player, red):
    WIN.blit(current_room.background_image, (0, 0))
    WIN.blit(PLAYERIMG, (player.x, player.y))
    WIN.blit(ENEMYIMG, (red.x, red.y))
    pygame.display.update()
    # Render other elements specific to the current room
    


def player_movement(keys_pressed, player_rect):
    if keys_pressed[pygame.K_a]:  # left
        player_rect.x -= VEL
    if keys_pressed[pygame.K_w]:  # up
        player_rect.y -= VEL
    if keys_pressed[pygame.K_s]:  # down
        player_rect.y += VEL
    if keys_pressed[pygame.K_d]:  # right
        player_rect.x += VEL
    
    # if keys_pressed[pygame.K_SPACE]: #interact
    #  player.x -= VEL


# def drawtext(text):
#   text = pygame.font.SysFont('calibri', 50)




def main():
    red = pygame.Rect(400, 300, 40, 55)
    
  
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_g:
                print("G key pressed!")

            if pygame.Rect.colliderect(player, red):
                print("collide")
        keys_pressed = pygame.key.get_pressed()
        player_movement(keys_pressed, player)
    
        room_manager.current_room.handle_events(events)
        draw_window(current_room, player, red)
        
        
        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
