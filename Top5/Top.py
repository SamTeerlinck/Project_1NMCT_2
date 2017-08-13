import MySQLdb
from Tkinter import *

root = Tk()
root.minsize(320,240)



db = MySQLdb.connect("localhost", "root", "root", "musicplayer")
curs=db.cursor()

curs.execute ("SELECT song, COUNT(*) Amount FROM playedsongs GROUP BY song ORDER BY amount DESC LIMIT 5")

index = 1
top5list = ""

for reading in curs.fetchall():
	top5list += "Nr. " + str(index) + "  = #" + str(reading[1]) + "  " + str(reading[0]) + "\n"
	index += 1


	
label = Label(root,text= 'Top 5 played songs \n \n' + top5list, anchor = W, justify = LEFT)
label.place(x=5,y=5)

root.mainloop()