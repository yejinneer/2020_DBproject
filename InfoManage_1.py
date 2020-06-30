# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'InfoManage_1.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql


class UI_InfoManage_01_Dialog(object):

    def messagebox(self, title, message):
        mess=QtWidgets.QMessageBox()
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mess.exec_()
    def AddtoDB(self):
        Sname = self.SnameEdit.text()
        Snum = int(self.SnumEdit.text())
        Swork = self.SworkEdit.text()
        if(self.SstateEdit.text() == '0'):
            Sstate = 0
        else:
            Sstate = 1
        print(Sname,Snum,Swork,Sstate)
        con = pymysql.connect(host="localhost", user="root", password="1234",
                              db='App', charset='utf8')
        cur = con.cursor()
        query = ("insert into soldier(name, number, work, state) values(%s,%s,%s,%s)")
        data = cur.execute(query, (Sname, Snum, Swork, Sstate))
        con.commit()
        if(data):
            self.messagebox("Success","Successfully Added!")

        self.SnameEdit.setText("")
        self.SnumEdit.setText("")
        self.SworkEdit.setText("")
        self.SstateEdit.setText("")

    def setupUi(self, InfoManage_01_Dialog):

        InfoManage_01_Dialog.setObjectName("Dialog")
        InfoManage_01_Dialog.resize(600, 400)

        self.label_2 = QtWidgets.QLabel(InfoManage_01_Dialog)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 600, 400))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("C:/Users/seo/Desktop/DBUI/info01.jpeg"))
        self.label_2.setObjectName("label_2")

        self.verticalLayoutWidget = QtWidgets.QWidget(InfoManage_01_Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(130, 110, 160, 211))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.SnameLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("08SeoulHangang")
        self.SnameLabel.setFont(font)
        self.SnameLabel.setObjectName("SnameLabel")
        self.verticalLayout_2.addWidget(self.SnameLabel)
        self.SnumLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("08SeoulHangang")
        self.SnumLabel.setFont(font)
        self.SnumLabel.setObjectName("SnumLabel")
        self.verticalLayout_2.addWidget(self.SnumLabel)
        self.SworkLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("08SeoulHangang")
        self.SworkLabel.setFont(font)
        self.SworkLabel.setObjectName("SworkLabel")
        self.verticalLayout_2.addWidget(self.SworkLabel)
        self.SstateLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("08SeoulHangang")
        self.SstateLabel.setFont(font)
        self.SstateLabel.setObjectName("SstateLabel")
        self.verticalLayout_2.addWidget(self.SstateLabel)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(InfoManage_01_Dialog)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(290, 110, 160, 211))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.SnameEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.SnameEdit.setObjectName("SnameEdit")
        self.verticalLayout_3.addWidget(self.SnameEdit)
        self.SnumEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.SnumEdit.setObjectName("SnumEdit")
        self.verticalLayout_3.addWidget(self.SnumEdit)
        self.SworkEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.SworkEdit.setObjectName("SworkEdit")
        self.verticalLayout_3.addWidget(self.SworkEdit)
        self.SstateEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.SstateEdit.setObjectName("SstateEdit")
        self.verticalLayout_3.addWidget(self.SstateEdit)
        self.horizontalLayoutWidget = QtWidgets.QWidget(InfoManage_01_Dialog)
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
        self.okBtn.clicked.connect(self.AddtoDB)



        self.retranslateUi(InfoManage_01_Dialog)
        QtCore.QMetaObject.connectSlotsByName(InfoManage_01_Dialog)

    def retranslateUi(self, InfoManage_01_Dialog):
        _translate = QtCore.QCoreApplication.translate
        InfoManage_01_Dialog.setWindowTitle(_translate("Dialog", "Dialog"))

        self.SnameLabel.setText(_translate("Dialog", ""))
        self.SnumLabel.setText(_translate("Dialog", ""))
        self.SworkLabel.setText(_translate("Dialog", ""))
        self.SstateLabel.setText(_translate("Dialog", ""))
        self.SstateEdit.setPlaceholderText(_translate("Dialog", "가능(1)/불가능(0)"))
        self.okBtn.setText(_translate("Dialog", "OK"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    InfoManage_01_Dialog = QtWidgets.QDialog()
    ui = UI_InfoManage_01_Dialog()
    ui.setupUi(InfoManage_01_Dialog)
    InfoManage_01_Dialog.show()
    sys.exit(app.exec_())
