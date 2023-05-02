import threading
import pyttsx3
import time



# Thread for Text to Speech Engine
class TTSThread(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue
        self.daemon = True
        self.tts_engine= pyttsx3.init()
        self.token = 0
        self.stop = True

        self.start()
    


    def run(self):
        self.tts_engine.startLoop(False)
        t_running = True
        while t_running:
            data = self.queue.get()
            if data == "stop":
                print("STOPED")
                self.tts_engine.stop()
            elif len(data) > 0:
                self.tts_engine.say(data)
                self.tts_engine.iterate()
            else:
                self.tts_engine.stop()
        self.tts_engine.endLoop()
