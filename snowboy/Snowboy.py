#-*- coding: utf-8 -*-

import snowboydecoder
import sys
import signal
import fonction

class Snowboy(object):
    def __init__(self, model, sensitivity = 0.5):
        self.interrupted = False
        self.sensitivity = sensitivity
        self.model = model

    def signal_handler(self, signal, frame):
        self.interrupted = True

    def interrupt_callback(self):
        return self.interrupted

    def detected_callback(self):
        fonction.play("triggered.wav")
        fonction.play("Oui.wav")
        self.interrupted = True
        #sys.exit(0)
        
    def detection(self):
        # capture SIGINT signal, e.g., Ctrl+C
        signal.signal(signal.SIGINT, self.signal_handler)

        detector = snowboydecoder.HotwordDetector(self.model, sensitivity=self.sensitivity)

        #print('Listening... Press Ctrl+C to exit')

        detector.start(detected_callback=self.detected_callback,
               interrupt_check=self.interrupt_callback,
               sleep_time=0.03)

        detector.terminate()

if __name__ == "__main__":
    snow = Snowboy('resources/optimus.pmdl', 0.35)
    snow.detection()	
