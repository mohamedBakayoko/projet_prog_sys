import os

def Fork():

    pid_fils = os.fork()
    if pid_fils == 0:
        return "Fils : "+"PID = "+str(os.getpid())+", PPID= "+str(os.getppid())
    elif pid_fils == -1:
        return "Impossible"
    else:
        return str(os.getpid())