from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from Assets import Resources

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1078, 771)
        MainWindow.setMinimumSize(QtCore.QSize(1078, 771))
        MainWindow.setMaximumSize(QtCore.QSize(1078, 771))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Assets/monitor.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-image: url(:/Res/img3.jpg);\n" "color : white;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Patient1_Heartrate = QtWidgets.QLCDNumber(self.centralwidget)
        self.Patient1_Heartrate.setGeometry(QtCore.QRect(10, 180, 161, 81))
        self.Patient1_Heartrate.setStyleSheet("color : red;")
        self.Patient1_Heartrate.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.Patient1_Heartrate.setProperty("value", 74.0)
        self.Patient1_Heartrate.setProperty("intValue", 74)
        self.Patient1_Heartrate.setObjectName("Patient1_Heartrate")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 40, 111, 121))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Assets/patient.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(480, 330, 81, 91))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("Assets/heart.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(620, 40, 111, 121))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("Assets/patient.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 420, 111, 121))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("Assets/patient.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.patient1_status_label = QtWidgets.QLabel(self.centralwidget)
        self.patient1_status_label.setGeometry(QtCore.QRect(360, 180, 81, 81))
        self.patient1_status_label.setText("")
        self.patient1_status_label.setPixmap(QtGui.QPixmap("Assets/checked.png"))
        self.patient1_status_label.setScaledContents(True)
        self.patient1_status_label.setObjectName("patient1_status_label")
        self.patient2_status_label = QtWidgets.QLabel(self.centralwidget)
        self.patient2_status_label.setGeometry(QtCore.QRect(950, 180, 81, 81))
        self.patient2_status_label.setText("")
        self.patient2_status_label.setPixmap(QtGui.QPixmap("Assets/checked.png"))
        self.patient2_status_label.setScaledContents(True)
        self.patient2_status_label.setObjectName("patient2_status_label")
        self.patient3_status_label = QtWidgets.QLabel(self.centralwidget)
        self.patient3_status_label.setGeometry(QtCore.QRect(360, 560, 81, 81))
        self.patient3_status_label.setText("")
        self.patient3_status_label.setPixmap(QtGui.QPixmap("Assets/checked.png"))
        self.patient3_status_label.setScaledContents(True)
        self.patient3_status_label.setObjectName("patient3_status_label")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(190, 210, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.Patient2_Heartrate = QtWidgets.QLCDNumber(self.centralwidget)
        self.Patient2_Heartrate.setGeometry(QtCore.QRect(610, 180, 161, 81))
        self.Patient2_Heartrate.setStyleSheet("color : red;")
        self.Patient2_Heartrate.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.Patient2_Heartrate.setProperty("value", 74.0)
        self.Patient2_Heartrate.setProperty("intValue", 74)
        self.Patient2_Heartrate.setObjectName("Patient2_Heartrate")
        self.Patient3_Heartrate = QtWidgets.QLCDNumber(self.centralwidget)
        self.Patient3_Heartrate.setGeometry(QtCore.QRect(10, 560, 161, 81))
        self.Patient3_Heartrate.setStyleSheet("color : red;")
        self.Patient3_Heartrate.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.Patient3_Heartrate.setProperty("value", 74.0)
        self.Patient3_Heartrate.setProperty("intValue", 74)
        self.Patient3_Heartrate.setObjectName("Patient3_Heartrate")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(190, 590, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(790, 210, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1078, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Central ICU Monitor"))
        self.label_8.setText(_translate("MainWindow", "BPM"))
        self.label_9.setText(_translate("MainWindow", "BPM"))
        self.label_10.setText(_translate("MainWindow", "BPM"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())