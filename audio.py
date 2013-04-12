from pygame.locals import *
import pygame

# init mixer
pygame.mixer.init()

SND_PATH = 'D:\\Dropbox\\Sound Effects and Music for DI\\'

# Music
music_files = ['1mellow.mp3', '2suspence.wav', '3Questioning.mp3', '4conflict.mp3',
                '5Cheerful.mp3', '6Tragic.mp3']
current_song = -1
MUSIC_VOLUME = 0.2

# Sound effects
soundDoor = pygame.mixer.Sound(SND_PATH + "#door.wav")

def music_play_next():
    global current_song
    if current_song < len(music_files):
        current_song += 1
    else:
        return None
    next_song = SND_PATH + music_files[current_song]
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.fadeout(500)
    pygame.mixer.music.load(next_song)
    pygame.mixer.music.set_volume(MUSIC_VOLUME)
    pygame.mixer.music.play(-1)

def music_play_previous():
    global current_song
    if current_song > 0:
        current_song -= 1
    else:
        return None
    next_song = SND_PATH + music_files[current_song]
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.fadeout(500)
    pygame.mixer.music.load(next_song)
    pygame.mixer.music.set_volume(MUSIC_VOLUME)
    pygame.mixer.music.play(-1)
    
def music_pause():
    pygame.mixer.music.pause()
    
def music_unpause():
    pygame.mixer.music.unpause()

def music_active():
    return pygame.mixer.music.get_busy()
    
def door_play():
    soundDoor.play()