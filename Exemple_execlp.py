
import os

def Execlp():
	pid = os.fork()
	if pid == 0:
		list = ["pwd"]
		for i in list:
			os.execlp(i, i)
	else:
		os.wait()
