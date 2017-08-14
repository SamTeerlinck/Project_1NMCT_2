#Import required libraries

import MySQLdb
from Tkinter import *

#Create Tkinter screen
root = Tk()
root.minsize(320,240)


#Connect to Database
db = MySQLdb.connect("localhost", "root", "root", "musicplayer")
curs=db.cursor()

#Show Top 5 most played songs
curs.execute ("SELECT song, COUNT(*) Amount FROM playedsongs GROUP BY song ORDER BY amount DESC LIMIT 5")

index = 1
top5list = ""

#Display Top 5
for reading in curs.fetchall():
	top5list += "Nr. " + str(index) + "  = #" + str(reading[1]) + "  " + str(reading[0]) + "\n"
	index += 1


#Tkinter label with Top 5	
label = Label(root,text= 'Top 5 played songs \n \n' + top5list, anchor = W, justify = LEFT)
label.place(x=5,y=5)

root.mainloop()