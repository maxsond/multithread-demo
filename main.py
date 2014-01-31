import display
from thread import myThread
		
thread1 = myThread(1, "Thread-1", display.lwin)
thread2 = myThread(2, "Thread-2", display.rwin)
		
thread1.start()
thread2.start()
display.end(display.scr)
display.curses.endwin()