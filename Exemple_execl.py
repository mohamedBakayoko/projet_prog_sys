import os

def Execl():
	pid = os.fork()
	if pid == 0:
		os.execl("/bin/date", "date")
	else:
		os.wait()