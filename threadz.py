import display
import threading
import sys

class myThread(threading.Thread):

	def __init__(self,threadID,name,win):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name
		self.win = win
	def run(self):
		display.refresh()
		display.msg("ABC DEF GHI JKL MNO PQR STU VWX",False,self.win)