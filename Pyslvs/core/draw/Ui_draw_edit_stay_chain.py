# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/ahshoe/Desktop/Pyslvs/core/draw/draw_edit_stay_chain.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(379, 325)
        Dialog.setMinimumSize(QtCore.QSize(379, 158))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/editchain.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setAutoFillBackground(False)
        Dialog.setSizeGripEnabled(False)
        Dialog.setModal(True)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(290, 20, 81, 71))
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 20, 251, 31))
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(50, 56, 141, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(130, 126, 91, 21))
        self.label_3.setObjectName("label_3")
        self.Point1 = QtWidgets.QComboBox(Dialog)
        self.Point1.setGeometry(QtCore.QRect(130, 150, 91, 25))
        self.Point1.setObjectName("Point1")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(130, 186, 91, 21))
        self.label_4.setObjectName("label_4")
        self.Point2 = QtWidgets.QComboBox(Dialog)
        self.Point2.setGeometry(QtCore.QRect(130, 210, 91, 25))
        self.Point2.setObjectName("Point2")
        self.Point3 = QtWidgets.QComboBox(Dialog)
        self.Point3.setGeometry(QtCore.QRect(130, 260, 91, 25))
        self.Point3.setObjectName("Point3")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(130, 236, 91, 21))
        self.label_5.setObjectName("label_5")
        self.p1_p2 = QtWidgets.QDoubleSpinBox(Dialog)
        self.p1_p2.setGeometry(QtCore.QRect(250, 170, 62, 26))
        self.p1_p2.setMinimum(0.01)
        self.p1_p2.setProperty("value", 10.0)
        self.p1_p2.setObjectName("p1_p2")
        self.p2_p3 = QtWidgets.QDoubleSpinBox(Dialog)
        self.p2_p3.setGeometry(QtCore.QRect(250, 230, 62, 26))
        self.p2_p3.setMinimum(0.01)
        self.p2_p3.setProperty("value", 10.0)
        self.p2_p3.setObjectName("p2_p3")
        self.p1_p3 = QtWidgets.QDoubleSpinBox(Dialog)
        self.p1_p3.setGeometry(QtCore.QRect(20, 200, 62, 26))
        self.p1_p3.setMinimum(0.01)
        self.p1_p3.setProperty("value", 10.0)
        self.p1_p3.setObjectName("p1_p3")
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(50, 260, 101, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(Dialog)
        self.line_2.setGeometry(QtCore.QRect(40, 160, 20, 111))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(Dialog)
        self.line_3.setGeometry(QtCore.QRect(50, 160, 118, 3))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(Dialog)
        self.line_4.setGeometry(QtCore.QRect(270, 160, 20, 111))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(Dialog)
        self.line_5.setGeometry(QtCore.QRect(200, 150, 81, 20))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_6 = QtWidgets.QFrame(Dialog)
        self.line_6.setGeometry(QtCore.QRect(210, 260, 71, 16))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.line_7 = QtWidgets.QFrame(Dialog)
        self.line_7.setGeometry(QtCore.QRect(210, 210, 71, 16))
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.Chain = QtWidgets.QComboBox(Dialog)
        self.Chain.setGeometry(QtCore.QRect(50, 80, 141, 25))
        self.Chain.setObjectName("Chain")
        self.buttonBox.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.line.raise_()
        self.line_2.raise_()
        self.p1_p3.raise_()
        self.line_3.raise_()
        self.line_4.raise_()
        self.p2_p3.raise_()
        self.p1_p2.raise_()
        self.line_5.raise_()
        self.Point1.raise_()
        self.line_6.raise_()
        self.Point3.raise_()
        self.line_7.raise_()
        self.Point2.raise_()
        self.Chain.raise_()

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Edit Stay Chain"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt;\">Choose points for stay chain.</span></p></body></html>"))
        self.label_2.setText(_translate("Dialog", "Name"))
        self.label_3.setText(_translate("Dialog", "Point[1]"))
        self.label_4.setText(_translate("Dialog", "Point[2]"))
        self.label_5.setText(_translate("Dialog", "Point[3]"))

import icons_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

