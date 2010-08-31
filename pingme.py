""" Ping script, using ping utility from Windows"""

import sys
from PyQt4 import QtGui, QtCore
from Ui_pingme import Ui_PingMainWindow


class PingMe(object):
    def __init__(self, address_to):
        self.address_to = address_to

    def pingMe(self):
        from subprocess import Popen
        try:
            p = Popen(['ping', self.address_to, '-t'])
            return p
        except:
            return None


class PingMainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(PingMainWindow, self).__init__(parent)
        self.ui = Ui_PingMainWindow()
        self.ui.setupUi(self)
        self.ui.urlLineEdit.setText('8.8.8.8')
        self.ui.urlLineEdit.setFocus()
        # connect
        self.connect(self.ui.startPushButton, QtCore.SIGNAL("clicked()"), self.startPing)
        self.connect(self.ui.stopPushButton, QtCore.SIGNAL("clicked()"), self.stopPing)


    def startPing(self):
        url = self.ui.urlLineEdit.text()
        pingme = PingMe(str(url))
        self.pingproc = pingme.pingMe()
        if self.pingproc is None:
            QtGui.QMessageBox.waning(self,  "Proses-Gagal",  "Proses gagal dijalankan!")

    def stopPing(self):        
        self.pingproc.terminate()
        self.close()

        
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    QtGui.QApplication.setWindowIcon(QtGui.QIcon('images/computer.png'))
    PingMainWindow = PingMainWindow()
    PingMainWindow.show()
    sys.exit(app.exec_())
    
