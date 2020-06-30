# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'listtest.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from TodayTable import *

def getinfo():

    con = pymysql.connect(host="localhost", user="root", password="1234",
                          db='App', charset='utf8')
    cur = con.cursor()
    sql = "SELECT name, score from soldier order by score desc"

    cur.execute(sql)
    result = cur.fetchall()
    return result


class Ui_ScoreTable(object):
    def setupUi(self, Dialog):
        score_data = getinfo()
        n = len(score_data)

        Dialog.setObjectName("Dialog")
        Dialog.resize(648, 553)

        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 648, 553))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("C:/Users/seo/Desktop/DBUI/gradeback.jpeg"))
        self.label_2.setObjectName("label_2")
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(150, 160, 361, 311))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(n)

        for i in range(n):#행 n개 생성(생성만 함)
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setVerticalHeaderItem(i, item)

        #열 생성
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)

        #행열에 위젯 추가
        for i in range(n):
            for j in range(2):
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget.setItem(i, j, item)

        self.retranslateUi(Dialog, score_data, n)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog, score_data, n):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))

        for i in range(n):
            item = self.tableWidget.verticalHeaderItem(i)
            item.setText(_translate("Dialog", str(i+1)))

        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "이름"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "점수"))


        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        for row in range(n):
            for col in range(2):
                item = self.tableWidget.item(row,col)
                item.setText(_translate('Dialog', str(score_data[row][col])))

        self.tableWidget.setSortingEnabled(__sortingEnabled)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_ScoreTable()

    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

