import tkinter as tk
import pygame
import os

pygame.mixer.init()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def abs_path(file):
    return os.path.join(BASE_DIR, file)

def play_sound(file):
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()

def create_app():
    root = tk.Tk()
    root.title("Minion sounds")    
    root.geometry("250x300")
    root.resizable(False, False)

    tk.Button(
        root, 
        text="Minion papoy", 
        font=("Arial", 14),
        command=lambda: play_sound(abs_path("sounds/minions-papoy.wav"))
    ).pack(pady=10)

    tk.Button(
        root, 
        text="Minion ta yes", 
        font=("Arial", 14),
        command=lambda: play_sound(abs_path("sounds/minions-ta-yes.wav"))
    ).pack(pady=10)

    tk.Button(
        root, 
        text="Minion short laugh", 
        font=("Arial", 14),
        command=lambda: play_sound(abs_path("sounds/minions-short-laugh.wav"))
    ).pack(pady=10)
    
    tk.Button(
        root,
        text="Minion wahoo",
        font=("Arial", 14),
        command=lambda: play_sound(abs_path("sounds/wahoo-minions.wav"))
    ).pack(pady=10)
    
    tk.Button(
        root,
        text="Minion banana",
        font=("Arial", 14),
        command=lambda: play_sound(abs_path("sounds/banana-minions.wav"))
    ).pack(pady=10)
    

    root.mainloop()

create_app()
