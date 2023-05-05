import winsound

from winsound import PlaySound


def play_music():
    PlaySound("assets/music.wav", winsound.SND_LOOP+winsound.SND_ASYNC)