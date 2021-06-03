from symbl.utils.Logger import Log
from symbl.utils.Threads import Thread

def wrap_keyboard_interrupt(function):
    def wrapper(*args, **kw):
        try:
            function(*args, **kw)
        except KeyboardInterrupt:
            Log.getInstance().info("Closing all connections")
            self = args[0]
            if hasattr(self, "connection"):
                self.connection.sock.close()
            Thread.getInstance().stop_all_threads()
    
    return wrapper