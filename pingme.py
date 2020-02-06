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
        self.address_to = "yahoo.com"
        self.setup_ui()

    def setup_ui(self):
        self.window = tk.Tk()
        self.window.columnconfigure(0, minsize=50)
        self.window.rowconfigure([0,1,2], minsize=50)
        self.ent_address = tk.Entry()
        self.ent_address.insert(0, self.address_to)
        self.btn_pingme = tk.Button(text="Ping Me", command=self.ping_start)
        self.btn_stop = tk.Button(text="Stop", command=self.ping_stop)
        self.ent_address.grid(row=0, column=0)
        self.btn_pingme.grid(row=1, column=0)
        self.btn_stop.grid(row=2, column=0)

    def ping_start(self):
        self.ping = PingMe(self.address_to)
        self.ping_proc = self.ping.ping()

    def ping_stop(self):
        self.ping_proc.terminate()


if __name__ == '__main__':
    gui = MainWindow()
    gui.window.mainloop()
