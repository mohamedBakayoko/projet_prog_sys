import os


def fonc():

	pid=os.fork()
	if pid == 0:
		os.execl("/bin/xlogo", "xlogo")
	else:


fonc()
