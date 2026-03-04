import tkinter as tk
from tkinter import filedialog
import pygame
import os

pygame.mixer.init()

current_file = None
paused = False

def load_music():
    global current_file
    file_path = filedialog.askopenfilename(
        filetypes=[("Audio Files", "*.mp3 *.wav *.ogg")]
    )
    if file_path:
        current_file = file_path
        pygame.mixer.music.load(file_path)
        song_label.config(text=os.path.basename(file_path))

def play_music():
    global paused
    if current_file:
        if paused:
            pygame.mixer.music.unpause()
            paused = False
        else:
            pygame.mixer.music.play()

def pause_music():
    global paused
    pygame.mixer.music.pause()
    paused = True

def stop_music():
    pygame.mixer.music.stop()

def set_volume(val):
    volume = float(val) / 100
    pygame.mixer.music.set_volume(volume)

# UI
root = tk.Tk()
root.title("Simple Music Player")
root.geometry("400x350")
root.resizable(False, False)

title = tk.Label(root, text="Simple Music Player", font=("Arial", 16))
title.pack(pady=10)

song_label = tk.Label(root, text="No song loaded", wraplength=300)
song_label.pack(pady=10)

tk.Button(root, text="Load Music", width=20, command=load_music).pack(pady=5)
tk.Button(root, text="Play", width=20, command=play_music).pack(pady=5)
tk.Button(root, text="Pause", width=20, command=pause_music).pack(pady=5)
tk.Button(root, text="Stop", width=20, command=stop_music).pack(pady=5)

volume_slider = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL,
                         label="Volume", command=set_volume)
volume_slider.set(70)
volume_slider.pack(pady=10)

root.mainloop()
