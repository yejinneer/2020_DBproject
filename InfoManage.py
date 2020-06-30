# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'InfoManage.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from InfoManage_1 import UI_InfoManage_01_Dialog
from InfoManage_2 import UI_InfoManage_02_Dialog

class UI_InfoManageDialog(object):
    def openInfoManage_1 (self):
        self.window = QtWidgets.QDialog()
        self.ui = UI_InfoManage_01_Dialog()
        self.ui.setupUi(self.window)
        self.window.show()
    def openInfoManage_2 (self):
        self.window = QtWidgets.QDialog()
        self.ui = UI_InfoManage_02_Dialog()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, InfoManageDialog):

        InfoManageDialog.setObjectName("Dialog")
        InfoManageDialog.resize(600, 400)

        self.label_2 = QtWidgets.QLabel(InfoManageDialog)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 600, 400))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("C:/Users/seo/Desktop/DBUI/info.jpeg"))
        self.label_2.setObjectName("label_2")

        self.SoldierAdd = QtWidgets.QPushButton(InfoManageDialog)
        self.SoldierAdd.setGeometry(QtCore.QRect(120, 240, 160, 50))
        font = QtGui.QFont()
        font.setFamily("Jalnan OTF")
        font.setPointSize(12)
        self.SoldierAdd.setFont(font)
        self.SoldierAdd.setObjectName("SoldierAdd")

        self.SoldierAdd.clicked.connect(self.openInfoManage_1)

        self.SoldierModify = QtWidgets.QPushButton(InfoManageDialog)
        self.SoldierModify.setGeometry(QtCore.QRect(320, 240, 160, 50))
        font = QtGui.QFont()
        font.setFamily("Jalnan OTF")
        font.setPointSize(12)
        self.SoldierModify.setFont(font)
        self.SoldierModify.setObjectName("SoldierModify")

        self.SoldierModify.clicked.connect(self.openInfoManage_2)

        self.retranslateUi(InfoManageDialog)
        QtCore.QMetaObject.connectSlotsByName(InfoManageDialog)

    def retranslateUi(self, InfoManageDialog):
        _translate = QtCore.QCoreApplication.translate
        InfoManageDialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.SoldierAdd.setText(_translate("Dialog", "병사 정보 입력"))
        self.SoldierModify.setText(_translate("Dialog", "병사 상태 수정"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    InfoManageDialog = QtWidgets.QDialog()
    ui = UI_InfoManageDialog()
    ui.setupUi(InfoManageDialog)
    InfoManageDialog.show()
    sys.exit(app.exec_())
