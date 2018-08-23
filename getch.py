# class _GetchUnix:
#     def __init__(self):
#         import tty, sys
#         from select import select
#     def __call__(self):
#         import sys, tty, termios
#         from select import select
#         fd = sys.stdin.fileno()
#         old_settings = termios.tcgetattr(fd)
#         try:
#             tty.setraw(sys.stdin.fileno())
#             [i, o, e] = select([sys.stdin.fileno()], [], [], 0.05)
#             if i: 
#                 ch=sys.stdin.read(1)
#             else: 
#                 ch='' 
#         finally:
#             termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
#         return ch

class _GetchUnix:
    def __init__(self):
        import tty, sys
    def __call__(self):
        import sys
        import tty
        import termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch
     
getchS = _GetchUnix()

class AlarmException(Exception):
    pass

def alarmHandler(signum, frame):
    raise AlarmException

def getch(timeout=0.05):
    import signal
    signal.signal(signal.SIGALRM, alarmHandler)
    signal.setitimer(signal.ITIMER_REAL,timeout,timeout)
    try:
        text = getchS()
        signal.alarm(0)
        return text
    except AlarmException:
        pass
    signal.signal(signal.SIGALRM, signal.SIG_IGN)
    return ''