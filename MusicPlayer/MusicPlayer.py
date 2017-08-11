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
 
def updatelabel():
	global index
	global songname
	v.set(listofsongs[index].replace(".mp3",""))
	#return songname

def playpause(event):
	global index
	if pausebutton["text"] == 'Pause':
		pygame.mixer.music.pause()
		pausebutton["text"] = 'Play'
	elif pausebutton["text"] == 'Play':
		pygame.mixer.music.unpause()
		pausebutton["text"] = 'Pause'
	
def nextsong(event):
	global index
	if shufflevar.get() == 1:
		numberrandom = random.randint(0,len(listofsongs)-1)
		
		while index == numberrandom:
			numberrandom = random.randint(0,len(listofsongs)-1)

		index = numberrandom
		pygame.mixer.music.load(listofsongs[index])
		pygame.mixer.music.play()
		updatelabel()
	else:
		if index < len(listofsongs)-1:
			index += 1
			pygame.mixer.music.load(listofsongs[index])
			pygame.mixer.music.play()
			updatelabel()

def prevsong(event):
	global index
	if shufflevar.get() == 1:
		numberrandom = random.randint(0,len(listofsongs)-1)
		
		while index == numberrandom:
			numberrandom = random.randint(0,len(listofsongs)-1)

		index = numberrandom
		pygame.mixer.music.load(listofsongs[index])
		pygame.mixer.music.play()
		updatelabel()
	else:
		if index > 0:
			index -= 1
			pygame.mixer.music.load(listofsongs[index])
			pygame.mixer.music.play()
			updatelabel()


def stopsong(event):
	pygame.mixer.music.stop()
	v.set("")
	#return songname


label = Label(root,text='Selected songs:')
label.place(x=5,y=5)

listbox = Listbox(root)
listbox.place(x=5,y=30)

listofsongs.reverse()

indexforloop = 1
for items in listofsongs:
	listbox.insert(0,indexforloop + ". " + items.replace(".mp3",""))
	indexforloop += 1

listofsongs.reverse()

pausebutton = Button(root,text = 'Pause')
pausebutton.place(x=180,y=40)

nextbutton = Button(root,text = 'Next Song')
nextbutton.place(x=180,y=70)

previousbutton = Button(root,text = 'Previous Song')
previousbutton.place(x=180,y=100)

stopbutton = Button(root,text='Stop Music')
stopbutton.place(x=180,y=130)

shufflechkbox = Checkbutton(root,text = 'Shuffle', variable=shufflevar, onvalue = 1, offvalue = 0)
shufflechkbox.place(x=180,y=160)

pausebutton.bind("<Button-1>",playpause)
nextbutton.bind("<Button-1>",nextsong)
previousbutton.bind("<Button-1>",prevsong)
stopbutton.bind("<Button-1>",stopsong)

songlabel.place(x=40,y=185)


root.mainloop()