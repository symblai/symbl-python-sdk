from symbl.utils.Threads import Thread

def wrap_keyboard_interrupt(function):
    def wrapper(*args, **kw):
        try:
            function(*args, **kw)
        except KeyboardInterrupt:
            print("Closing all connections")
            self = args[0]
            self.connection.sock.close()
            Thread.getInstance().stop_all_threads()
    
    return wrapper