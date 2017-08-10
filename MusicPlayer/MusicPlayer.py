import os

import pygame

from tkinter.filedialog import askdirectory
from tkinter import *

import random

root = Tk()
root.minsize(320,240)

listofsongs = []
realnames = []
 
v = StringVar()
songlabel = Label(root,textvariable=v,width=35)

shufflevar = IntVar()
shufflevar.set(0)
 
index = 0
numberrandom = 0
 
def directorychooser():
	directory = askdirectory()
	os.chdir(directory)
	
	for files in os.listdir(directory):
		if files.endswith(".mp3"):
			listofsongs.append(files)
			
	pygame.mixer.init()
	pygame.mixer.music.load(listofsongs[0])
	pygame.mixer.music.play()
	v.set(listofsongs[index].replace(".mp3",""))
	
	
	
directorychooser()