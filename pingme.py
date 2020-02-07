""" Ping script, using ping utility from Windows"""

import sys
import subprocess
import tkinter as tk

class PingMe(object):
    def __init__(self, address_to):
        self.address_to = address_to

    def ping(self):
        if sys.platform.startswith('linux'):
            self.process = subprocess.Popen(["ping", self.address_to])
        elif sys.platform.startswith('win'):
            self.process = subprocess.Popen(["ping", "-t", self.address_to])
        return self.process



class MainWindow(object):
    def __init__(self):
    	self.address_to = "8.8.8.8" #default address to ping
    	self.setup_ui()

    def setup_ui(self):
      self.window = tk.Tk()
      self.ent_address = tk.Entry()
      self.ent_address.insert(0, self.address_to)
      self.btn_pingme = tk.Button(text="Ping Me", command=self.ping_start)
      self.btn_stop = tk.Button(text="Stop", command=self.ping_stop)
      self.ent_address.grid(row=0, column=0, columnspan=2, padx=4)
      self.btn_pingme.grid(row=1, column=0)
      self.btn_stop.grid(row=1, column=1)

    def ping_start(self):
    	self.address_to = self.ent_address.get()
    	self.ping = PingMe(self.address_to)
    	self.ping_proc = self.ping.ping()

    def ping_stop(self):
    	try:
    		self.ping_proc.terminate()
    	except:
    		pass


if __name__ == '__main__':
    gui = MainWindow()
    gui.window.mainloop()
