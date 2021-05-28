import threading

class Thread():

    __instance = None
    threads = []

    @staticmethod
    def getInstance():
        if Thread.__instance == None:
            return Thread()
        
        return Thread.__instance
    
    def __init__(self):
        if Thread.__instance != None:
            raise Exception("Can not instantiate more than once!")
        else:
            Thread.__instance = self
        

    def start_on_thread(self, target, *args):
        thread = threading.Thread(target=target, args=(*args,))
        self.threads.append(thread)
        thread.start()

    def stop_all_threads(self):
        for thread in self.threads:
            thread.join()