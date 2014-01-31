import threading
import time
import display

class myThread(threading.Thread):

	def __init__(self,threadID,name,win):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name
		self.win = win
	def run(self):
		display.refresh()
		display.msg("ABC DEF GHI JKL MNO PQR STU VWX",False,self.win)
		
thread1 = myThread(1, "Thread-1", display.lwin)
thread2 = myThread(2, "Thread-2", display.rwin)

thread1.start()
thread2.start()
display.end(display.scr)
display.curses.endwin()