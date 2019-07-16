import threading
import time

from shared_resource import SharedResource
from shrek import Shrek


class MyThread(threading.Thread):
    __lock = threading.Lock()

    def __init__(self):
        threading.Thread.__init__(self)
        self._shared_resource = SharedResource()
        self._shrek = Shrek()

    def run(self):
        with MyThread.__lock:
            while self._shrek.are_we_there_yet():
                time.sleep(1)
                self._shared_resource.write(threading.current_thread().name)
