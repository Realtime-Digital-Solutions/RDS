import sys
import time

from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtGui import QColor

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.minDail = QtWidgets.QDial(self.centralwidget)
        self.minDail.setGeometry(QtCore.QRect(110, 290, 50, 64))
        self.minDail.setObjectName("minDail")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 270, 171, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.MaxDial = QtWidgets.QDial(self.centralwidget)
        self.MaxDial.setGeometry(QtCore.QRect(300, 290, 50, 64))
        self.MaxDial.setObjectName("MaxDial")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(250, 270, 181, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 40, 101, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.HRValue = QtWidgets.QLabel(self.centralwidget)
        self.HRValue.setGeometry(QtCore.QRect(70, 90, 131, 71))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.HRValue.setFont(font)
        self.HRValue.setScaledContents(False)
        self.HRValue.setWordWrap(False)
        self.HRValue.setObjectName("HRValue")
        self.minSet = QtWidgets.QLineEdit(self.centralwidget)
        self.minSet.setGeometry(QtCore.QRect(170, 310, 61, 22))
        self.minSet.setObjectName("minSet")
        self.maxSet = QtWidgets.QLineEdit(self.centralwidget)
        self.maxSet.setGeometry(QtCore.QRect(360, 310, 61, 22))
        self.maxSet.setObjectName("maxSet")
        self.MAC = QtWidgets.QLabel(self.centralwidget)
        self.MAC.setGeometry(QtCore.QRect(520, 110, 131, 16))
        self.MAC.setObjectName("MAC")
        self.MACaddress = QtWidgets.QLabel(self.centralwidget)
        self.MACaddress.setGeometry(QtCore.QRect(520, 140, 121, 16))
        self.MACaddress.setObjectName("MACaddress")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(240, 40, 101, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.HRValue_2 = QtWidgets.QLabel(self.centralwidget)
        self.HRValue_2.setGeometry(QtCore.QRect(260, 90, 131, 71))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.HRValue_2.setFont(font)
        self.HRValue_2.setScaledContents(False)
        self.HRValue_2.setWordWrap(False)
        self.HRValue_2.setObjectName("HRValue_2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(520, 50, 91, 16))
        self.label_5.setObjectName("label_5")
        self.PatientName = QtWidgets.QLineEdit(self.centralwidget)
        self.PatientName.setGeometry(QtCore.QRect(610, 50, 113, 22))
        self.PatientName.setObjectName("PatientName")
        self.timeOlabel = QtWidgets.QLabel(self.centralwidget)
        self.timeOlabel.setGeometry(QtCore.QRect(60, 400, 131, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.timeOlabel.setFont(font)
        self.timeOlabel.setObjectName("timeOlabel")
        self.TOAD = QtWidgets.QLabel(self.centralwidget)
        self.TOAD.setGeometry(QtCore.QRect(60, 420, 231, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.TOAD.setFont(font)
        self.TOAD.setObjectName("TOAD")
        self.Emerg = QtWidgets.QLabel(self.centralwidget)
        self.Emerg.setGeometry(QtCore.QRect(440, 400, 321, 81))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.Emerg.setFont(font)
        self.Emerg.setObjectName("Emerg")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PulseBeat"))
        self.label.setText(_translate("MainWindow", "Set Heart Rate Min limits"))
        self.label_2.setText(_translate("MainWindow", "Set Heart Rate Max limits"))
        self.label_3.setText(_translate("MainWindow", "Heart Rate BPM"))
        self.HRValue.setText(_translate("MainWindow", "75"))
        self.MAC.setText(_translate("MainWindow", "Device MAC Address"))
        self.MACaddress.setText(_translate("MainWindow", "A3:DC:45:4F:92:8E"))
        self.label_4.setText(_translate("MainWindow", "RSSI Level dBm"))
        self.HRValue_2.setText(_translate("MainWindow", "-65"))
        self.label_5.setText(_translate("MainWindow", "Patient Name"))
        self.PatientName.setText(_translate("MainWindow", "Peter Smith"))
        self.timeOlabel.setText(_translate("MainWindow", "Time of Data Arrival"))
        self.TOAD.setText(_translate("MainWindow", "12:00:00:00:00"))
        self.Emerg.setText(_translate("MainWindow", "Patient Stable"))

        # create thread
        self.thread = QtCore.QThread()
        # create object which will be moved to another thread
        self.browserHandler = BrowserHandler()
        # move object to another thread
        self.browserHandler.moveToThread(self.thread)
        # connect started signal to run method of object in another thread
        self.thread.started.connect(self.browserHandler.run)
        # start thread
        self.thread.start()

# Object, which will be moved to thread
class BrowserHandler(QtCore.QObject):
    running = False
    newTextAndColor = QtCore.pyqtSignal(str, object)

    # method which will execute algorithm in another thread
    def run(self):
        while True:
            print('Threading')
            QtCore.QThread.msleep(500)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
