# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'InfoManage_2.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql


class UI_InfoManage_02_Dialog(object):
    def messagebox(self, title, message):
        mess=QtWidgets.QMessageBox()
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mess.exec_()

    def StateChange(self):
        Snum = self.SnumCheck.text()

        if (len(self.SstateChangeEdit.text()) == 2):
            Sstate = 1
        else:
            Sstate = 0

        print(Snum,Sstate)
        con = pymysql.connect(host="localhost", user="root", password="1234",
                              db='App', charset='utf8')
        cur = con.cursor()
        query = "UPDATE soldier SET state = %s WHERE number = %s"
        data = cur.execute(query, (Sstate, Snum))
        con.commit()
        if (data):
            self.messagebox("Success", "Successfully Changed!")

        self.SnumCheck.setText("")
        self.SstateChangeEdit.setText("")

    def setupUi(self, InfoManage_02_Dialog):
        InfoManage_02_Dialog.setObjectName("Dialog")
        InfoManage_02_Dialog.resize(600, 400)

        self.label_2 = QtWidgets.QLabel(InfoManage_02_Dialog)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 600, 400))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("C:/Users/seo/Desktop/DBUI/info02.jpeg"))
        self.label_2.setObjectName("label_2")

        self.label = QtWidgets.QLabel(InfoManage_02_Dialog)
        self.label.setGeometry(QtCore.QRect(230, 50, 141, 41))
        font = QtGui.QFont()
        font.setFamily("08SeoulHangang")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayoutWidget = QtWidgets.QWidget(InfoManage_02_Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(130, 110, 160, 211))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.SnumLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("08SeoulHangang")
        self.SnumLabel.setFont(font)
        self.SnumLabel.setObjectName("SnumLabel")
        self.verticalLayout_2.addWidget(self.SnumLabel)
        self.SstateLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("08SeoulHangang")
        self.SstateLabel.setFont(font)
        self.SstateLabel.setObjectName("SstateLabel")
        self.verticalLayout_2.addWidget(self.SstateLabel)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(InfoManage_02_Dialog)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(290, 110, 160, 211))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")

        self.SnumCheck = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.SnumCheck.setObjectName("SnumCheck")
        self.verticalLayout_3.addWidget(self.SnumCheck)
        self.SstateChangeEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.SstateChangeEdit.setObjectName("SnumCheck")
        self.verticalLayout_3.addWidget(self.SstateChangeEdit)

        self.horizontalLayoutWidget = QtWidgets.QWidget(InfoManage_02_Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(250, 300, 80, 65))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.okBtn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Jalnan OTF")
        font.setPointSize(10)
        self.okBtn.setFont(font)
        self.okBtn.setObjectName("okBtn")
        self.horizontalLayout_2.addWidget(self.okBtn)
        self.okBtn.clicked.connect(self.StateChange)


        self.retranslateUi(InfoManage_02_Dialog)
        QtCore.QMetaObject.connectSlotsByName(InfoManage_02_Dialog)

    def retranslateUi(self, InfoManage_02_Dialog):
        _translate = QtCore.QCoreApplication.translate
        InfoManage_02_Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", " "))
        self.SnumLabel.setText(_translate("Dialog", " "))
        self.SstateLabel.setText(_translate("Dialog", " "))
        self.SstateChangeEdit.setPlaceholderText(_translate("Dialog", "가능/불가능"))
        self.okBtn.setText(_translate("Dialog", "OK"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    InfoManage_02_Dialog = QtWidgets.QDialog()
    ui = UI_InfoManage_02_Dialog()
    ui.setupUi(InfoManage_02_Dialog)
    InfoManage_02_Dialog.show()
    sys.exit(app.exec_())
