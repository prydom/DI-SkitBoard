from pygame.locals import *
import pygame

SND_PATH = 'D:\\Dropbox\\Sound Effects and Music for DI\\'

# Music list
music_files = ['1mellow.mp3', '2suspence.wav', '3Questioning.mp3', '4conflict.mp3',
                '5Cheerful.mp3', '6Tragic.mp3']
current_song = -1

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
    pygame.mixer.music.play(-1)

def music_play_back():
    global current_song
    if current_song > 0:
        current_song -= 1
    else:
        return None
    next_song = SND_PATH + music_files[current_song]
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.fadeout(500)
    pygame.mixer.music.load(next_song)
    pygame.mixer.music.play(-1)
    