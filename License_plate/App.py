# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'App.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import final_main
import re


class Ui_MainWindow(object):

    def __int__(self, file):
        self.file = file


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(807, 991)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gaussian = QtWidgets.QCheckBox(self.centralwidget)
        self.gaussian.setGeometry(QtCore.QRect(140, 310, 351, 61))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.gaussian.setFont(font)
        self.gaussian.setObjectName("gaussian")
        self.median = QtWidgets.QCheckBox(self.centralwidget)
        self.median.setGeometry(QtCore.QRect(140, 370, 231, 71))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.median.setFont(font)
        self.median.setObjectName("median")
        self.erode = QtWidgets.QCheckBox(self.centralwidget)
        self.erode.setGeometry(QtCore.QRect(140, 440, 351, 81))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.erode.setFont(font)
        self.erode.setObjectName("erode")
        self.start = QtWidgets.QPushButton(self.centralwidget)
        self.start.setGeometry(QtCore.QRect(690, 530, 341, 121))
        self.start.setObjectName("start")
        self.open_file = QtWidgets.QPushButton(self.centralwidget)
        self.open_file.setGeometry(QtCore.QRect(60, 10, 751, 141))
        self.open_file.setObjectName("open_file")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 160, 471, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.erode_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.erode_2.setGeometry(QtCore.QRect(140, 520, 351, 81))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.erode_2.setFont(font)
        self.erode_2.setObjectName("erode_2")
        self.gaussian_value_1 = QtWidgets.QLineEdit(self.centralwidget)
        self.gaussian_value_1.setGeometry(QtCore.QRect(390, 330, 61, 31))
        self.gaussian_value_1.setAccessibleName("")
        self.gaussian_value_1.setObjectName("gaussian_value_1")
        self.gaussian_value_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.gaussian_value_2.setGeometry(QtCore.QRect(480, 330, 61, 31))
        self.gaussian_value_2.setAccessibleName("")
        self.gaussian_value_2.setObjectName("gaussian_value_2")
        self.median_value_1 = QtWidgets.QLineEdit(self.centralwidget)
        self.median_value_1.setGeometry(QtCore.QRect(390, 390, 61, 31))
        self.median_value_1.setAccessibleName("")
        self.median_value_1.setObjectName("median_value_1")
        self.canny = QtWidgets.QCheckBox(self.centralwidget)
        self.canny.setGeometry(QtCore.QRect(140, 600, 351, 81))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.canny.setFont(font)
        self.canny.setObjectName("canny")
        self.erode_1_value_1 = QtWidgets.QLineEdit(self.centralwidget)
        self.erode_1_value_1.setGeometry(QtCore.QRect(390, 470, 61, 31))
        self.erode_1_value_1.setAccessibleName("")
        self.erode_1_value_1.setObjectName("erode_1_value_1")
        self.erode_1_value_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.erode_1_value_2.setGeometry(QtCore.QRect(490, 470, 61, 31))
        self.erode_1_value_2.setAccessibleName("")
        self.erode_1_value_2.setObjectName("erode_1_value_2")
        self.erode_1_value_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.erode_1_value_3.setGeometry(QtCore.QRect(590, 470, 61, 31))
        self.erode_1_value_3.setAccessibleName("")
        self.erode_1_value_3.setObjectName("erode_1_value_3")
        self.erode_2_value_1 = QtWidgets.QLineEdit(self.centralwidget)
        self.erode_2_value_1.setGeometry(QtCore.QRect(390, 540, 61, 31))
        self.erode_2_value_1.setAccessibleName("")
        self.erode_2_value_1.setObjectName("erode_2_value_1")
        self.erode_2_value_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.erode_2_value_2.setGeometry(QtCore.QRect(490, 540, 61, 31))
        self.erode_2_value_2.setAccessibleName("")
        self.erode_2_value_2.setObjectName("erode_2_value_2")
        self.erode_2_value_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.erode_2_value_3.setGeometry(QtCore.QRect(590, 540, 61, 31))
        self.erode_2_value_3.setAccessibleName("")
        self.erode_2_value_3.setObjectName("erode_2_value_3")
        self.canny_1 = QtWidgets.QLineEdit(self.centralwidget)
        self.canny_1.setGeometry(QtCore.QRect(390, 620, 61, 31))
        self.canny_1.setAccessibleName("")
        self.canny_1.setObjectName("canny_1")
        self.canny_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.canny_2.setGeometry(QtCore.QRect(490, 620, 61, 31))
        self.canny_2.setAccessibleName("")
        self.canny_2.setObjectName("canny_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(390, 270, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.Probability = QtWidgets.QLabel(self.centralwidget)
        self.Probability.setGeometry(QtCore.QRect(140, 680, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.Probability.setFont(font)
        self.Probability.setObjectName("Probability")
        self.Margin = QtWidgets.QLabel(self.centralwidget)
        self.Margin.setGeometry(QtCore.QRect(700, 320, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.Margin.setFont(font)
        self.Margin.setObjectName("Margin")
        self.probability_value = QtWidgets.QLineEdit(self.centralwidget)
        self.probability_value.setGeometry(QtCore.QRect(390, 690, 61, 31))
        self.probability_value.setAccessibleName("")
        self.probability_value.setObjectName("probability_value")
        self.margin_value = QtWidgets.QLineEdit(self.centralwidget)
        self.margin_value.setGeometry(QtCore.QRect(910, 330, 61, 31))
        self.margin_value.setAccessibleName("")
        self.margin_value.setObjectName("margin_value")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 807, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Click the button
        self.open_file.clicked.connect(self.clicker)

        # Click start
        self.start.clicked.connect(self.checked)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.gaussian.setText(_translate("MainWindow", "Gaussian filter"))
        self.median.setText(_translate("MainWindow", "Median filter"))
        self.erode.setText(_translate("MainWindow", "Erode - 1"))
        self.start.setText(_translate("MainWindow", "Start"))
        self.open_file.setText(_translate("MainWindow", "Open file"))
        self.label.setText(_translate("MainWindow", "Open file:"))
        self.erode_2.setText(_translate("MainWindow", "Erode - 2"))
        self.gaussian_value_1.setText(_translate("MainWindow", "1"))
        self.gaussian_value_2.setText(_translate("MainWindow", "1"))
        self.median_value_1.setText(_translate("MainWindow", "5"))
        self.canny.setText(_translate("MainWindow", "Canny"))
        self.erode_1_value_1.setText(_translate("MainWindow", "3"))
        self.erode_1_value_2.setText(_translate("MainWindow", "5"))
        self.erode_1_value_3.setText(_translate("MainWindow", "7"))
        self.erode_2_value_1.setText(_translate("MainWindow", "3"))
        self.erode_2_value_2.setText(_translate("MainWindow", "5"))
        self.erode_2_value_3.setText(_translate("MainWindow", "7"))
        self.canny_1.setText(_translate("MainWindow", "80"))
        self.canny_2.setText(_translate("MainWindow", "120"))
        self.label_2.setText(_translate("MainWindow", "Filter parameters\n"
""))
        self.Probability.setText(_translate("MainWindow", "Probability"))
        self.Margin.setText(_translate("MainWindow", "Margin"))
        self.probability_value.setText(_translate("MainWindow", "0.75"))
        self.margin_value.setText(_translate("MainWindow", "0.025"))


    def clicker(self):
        """self.label.setText()"""
        fname = QFileDialog.getOpenFileNames(None, "Open File", "", "All Files (*);;Mp4 Files (*.mp4);;JPG File (*.jpg);;PNG File (*.png);;JPEG File (*.jpeg)")

        print(fname)
        # Output filename to screen
        if fname:
            if re.search("(.mp4|.jpg|.png|.jpeg)", str(fname[0])):
                self.label.setText("Open File:" + str(fname[0]))
                self.file = str(fname[0]).replace("[", "").replace("]", "").replace("'", "")
            else:
                self.label.setText("Error. Wrong extension")



    def checked(self):
        #Filter parammeter
        gaussian = (int(self.gaussian_value_1.text()), int(self.gaussian_value_2.text()))
        median = (int(self.median_value_1.text()))
        erode_1 = (int(self.erode_1_value_1.text()), int(self.erode_1_value_2.text()), int(self.erode_1_value_3.text()))
        erode_2 = (int(self.erode_2_value_1.text()), int(self.erode_2_value_2.text()), int(self.erode_2_value_3.text()))
        canny_1 = int(self.canny_1.text())
        canny_2 = int(self.canny_2.text())
        probability = (float(self.probability_value.text()))
        margin = (float(self.margin_value.text()))

        print(gaussian)
        print(median)
        print(erode_1)
        print(erode_2)
        print(canny_1)
        print(canny_2)
        print(probability)
        print(margin)

        if re.search("(.jpg|.png|.jpeg)", self.file):
            final_main.main(None, self.file, probability, margin, erode_1, median, gaussian, erode_2, canny_1, canny_2)

        if re.search(".mp4", self.file):
            final_main.main(self.file, None, probability, margin, erode_1, median, gaussian, erode_2, canny_1, canny_2)

        else:
            print("Error. Wrong extension")







if __name__ == "__main__":
    import sys
    import os
    os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
