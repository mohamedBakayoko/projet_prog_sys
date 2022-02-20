import os


def Execvp():
	pid = os.fork()
	if pid == 0:
		list = ["xclock"]
		os.execvp("xclock", list)
	else:
		os.wait()
