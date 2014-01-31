import time
import curses
from winsize import x, y
x = x()
y = y()
scr = curses.initscr()
scr.border(0)
lwin = scr.derwin(0,x/2,1,1)
rwin = scr.derwin(0,0,1,x/2+1)
def refresh():
	scr.border(0)
	scr.refresh()
	lwin.border(0)
	rwin.border(0)
	lwin.refresh()
	rwin.refresh()
refresh()
r = lwin.getmaxyx()[1]
time.sleep(1)
class msg:
	
	def __init__(self,txt="Test String",wait=True,win=lwin,speed=0.1):
		self.txt = txt
		self.x = x + 1
		self.y = y + 1
		self.speed = speed
		self.win = win
		self.tw(wait,win)
		
	def al(self, align):	#Represents how the text should be horizontally aligned relative to (x,y)
		if align == 'right':
			return self.x
		elif align == 'center':
			return self.x - len(self.txt)/2
		elif align == 'left':
			return self.x - len(self.txt)

	def tw(self,wait=True,win=lwin,xy=(1,1)):
		"""Taps out a message like a typewriter.

		msg -> Message to be tapped out
		w -> Window to work in
		x,y -> Where the cursor should start
		"""
		#try:
		win.move(xy[0],xy[1])
		a = self.txt.split(" ")
		for i in a:
			a[a.index(i)] = len(i)
		index = 0
		for c in self.txt:
			if c == " ":
				index += 1
				if a[index] + i + 3 > r:
					win.move(j+1,1)
			i = win.getyx()[1]
			j = win.getyx()[0]
			win.addch(c)
			#win.addstr(str(i))
			win.refresh()
			time.sleep(self.speed)
			
#		except:
#			self.win.clear
#			curses.endwin()
#			print ""
#			print "Fatal error! Cursor went out of bounds!", self.x, self.y
		if wait:
			win.getch()
		refresh()
def end(win):
	win.erase()
	win.refresh()
	curses.endwin()
def clear(win):
	win.erase()
	win.border(0)
	win.move(1,1)
	win.refresh()
def inp(win=rwin):
	try:
		win.move(1,1)
		#msg.tw(False)
		#print msg.y+1, msg.al('right')
		return win.getstr(1,1)
		#print win.is_wintouched()
		#print xyz.is_wintouched()
		win.refresh()
	except:
		exit()
def test():
	time.sleep(0.5)
#clear(scr)
#curses.endwin()