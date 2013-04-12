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
SE_VOLUME = 1.0
soundDoor = pygame.mixer.Sound(SND_PATH + "#door.wav")
soundDoor.set_volume(SE_VOLUME)
soundFaint = pygame.mixer.Sound(SND_PATH + "#sigh and fall.wav")
soundFaint.set_volume(SE_VOLUME)
soundDun = pygame.mixer.Sound(SND_PATH + "#Dun Dun Dun.wav")
soundDun.set_volume(SE_VOLUME)

def get_current_song():
    global current_song
    if current_song == -1:
        return "No Music yet"
    else:
        return music_files[current_song]

def music_play_next():
    global current_song
    if current_song < len(music_files) and current_song != len(music_files)-1:
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

def faint_play():
    soundFaint.play()
    
def dun_play():
    soundDun.play()