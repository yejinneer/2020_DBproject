# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'temp.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql


def inputData():
    con = pymysql.connect(host="localhost", user="root", password="1234",
                          db='App', charset='utf8')
    cur = con.cursor()
    sql = 'SELECT number, name, work, score, state FROM soldier'
    cur.execute(sql)
    result = cur.fetchall()
    return result


def separateData(data, outer, outer1, outer2, inside):
    for x in data:
        if x[2] != '행정병' and x[4] != 0:
            outer.append(x)

        elif x[2] == '행정병' and x[4] != 0:
            inside.append(x)

    tmp=0
    for x in outer:
        if tmp%2==0:
            outer1.append(outer[tmp])
            tmp += 1
        else:
            outer2.append(outer[tmp])
            tmp += 1



class Ui_TodayTable(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)

        self.label_2 = QtWidgets.QLabel(MainWindow)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("C:/Users/seo/Desktop/DBUI/tableback.jpeg"))
        self.label_2.setObjectName("label_2")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(190, 100, 381, 451))
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tableWidget = QtWidgets.QTableWidget(self.tab)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 381, 421))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(12)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(4, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(5, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(5, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(6, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(6, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(7, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(7, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(8, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(8, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(9, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(9, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(10, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(10, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(11, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(11, 1, item)
        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.tab_3)
        self.tableWidget_2.setGeometry(QtCore.QRect(0, 0, 381, 421))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(2)
        self.tableWidget_2.setRowCount(12)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        for row in range(12):
            for col in range(2):
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget_2.setItem(row,col,item)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tableWidget_3 = QtWidgets.QTableWidget(self.tab_2)
        self.tableWidget_3.setGeometry(QtCore.QRect(0, 0, 381, 421))
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(2)
        self.tableWidget_3.setRowCount(12)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, item)

        for row in range(12):
            for col in range(2):
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget_3.setItem(row,col,item)
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setSizeGripEnabled(True)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        data = inputData()
        outer=[]
        outer1=[]
        outer2=[]
        inside=[]
        separateData(data, outer, outer1, outer2, inside)
        n_outer1=len(outer1)
        n_outer2=len(outer2)
        n_inside=len(inside)
        print(outer1)
        print(outer2)
        print(inside)
        print(n_outer1, n_outer2, n_inside)




        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "08:00~10:00"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "10:00~12:00"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "12:00~14:00"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "14:00~16:00"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "16:00~18:00"))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "18:00~20:00"))
        item = self.tableWidget.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "20:00~22:00"))
        item = self.tableWidget.verticalHeaderItem(7)
        item.setText(_translate("MainWindow", "22:00~00:00"))
        item = self.tableWidget.verticalHeaderItem(8)
        item.setText(_translate("MainWindow", "00:00~02:00"))
        item = self.tableWidget.verticalHeaderItem(9)
        item.setText(_translate("MainWindow", "02:00~04:00"))
        item = self.tableWidget.verticalHeaderItem(10)
        item.setText(_translate("MainWindow", "04:00~06:00"))
        item = self.tableWidget.verticalHeaderItem(11)
        item.setText(_translate("MainWindow", "06:00~08:00"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "정"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "부"))

        #위병소 정보 넣기
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)

        x = 0
        for row in range(12):
            for col in range(2):
                item = self.tableWidget.item(row, col)
                item.setText(_translate("mainWindow", str(outer1[x][1])))
                x = (x+1) % n_outer1
                con = pymysql.connect(host="localhost", user="root", password="1234",
                                      db='App', charset='utf8')
                cur = con.cursor()
                if (row < 5):
                    query = "UPDATE soldier SET score = score + %s WHERE name = %s"
                    cur.execute(query, (20, outer1[x][1]))
                    con.commit()
                elif (row >=5 and row < 9):
                    query = "UPDATE soldier SET score = score + %s WHERE name = %s"
                    cur.execute(query, (30, outer1[x][1]))
                    con.commit()
                elif (row >=9):
                    query = "UPDATE soldier SET score = score + %s WHERE name = %s"
                    cur.execute(query, (40, outer1[x][1]))
                    con.commit()


        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "위병소"))



        item = self.tableWidget_2.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "08:00~10:00"))
        item = self.tableWidget_2.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "10:00~12:00"))
        item = self.tableWidget_2.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "12:00~14:00"))
        item = self.tableWidget_2.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "14:00~16:00"))
        item = self.tableWidget_2.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "16:00~18:00"))
        item = self.tableWidget_2.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "18:00~20:00"))
        item = self.tableWidget_2.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "20:00~22:00"))
        item = self.tableWidget_2.verticalHeaderItem(7)
        item.setText(_translate("MainWindow", "22:00~00:00"))
        item = self.tableWidget_2.verticalHeaderItem(8)
        item.setText(_translate("MainWindow", "00:00~02:00"))
        item = self.tableWidget_2.verticalHeaderItem(9)
        item.setText(_translate("MainWindow", "02:00~04:00"))
        item = self.tableWidget_2.verticalHeaderItem(10)
        item.setText(_translate("MainWindow", "04:00~06:00"))
        item = self.tableWidget_2.verticalHeaderItem(11)
        item.setText(_translate("MainWindow", "06:00~08:00"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "정"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "부"))

        #탄약고 정보넣기
        __sortingEnabled = self.tableWidget_2.isSortingEnabled()
        self.tableWidget_2.setSortingEnabled(False)

        x=0
        print(outer2[0][1])
        for row in range(12):
            for col in range(2):
                item = self.tableWidget_2.item(row, col)
                print('row,col ',row,col, x)
                item.setText(_translate("mainWindow", outer2[x][1]))
                x = (x+1) % n_outer2
                con = pymysql.connect(host="localhost", user="root", password="1234",
                                      db='App', charset='utf8')
                cur = con.cursor()
                if (row < 5):
                    query = "UPDATE soldier SET score = score + %s WHERE name = %s"
                    cur.execute(query, (20, outer2[x][1]))
                    con.commit()
                elif (row >=5 and row < 9):
                    query = "UPDATE soldier SET score = score + %s WHERE name = %s"
                    cur.execute(query, (30, outer2[x][1]))
                    con.commit()
                elif (row >=9):
                    query = "UPDATE soldier SET score = score + %s WHERE name = %s"
                    cur.execute(query, (40, outer2[x][1]))
                    con.commit()
        self.tableWidget_2.setSortingEnabled(__sortingEnabled)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "탄약고"))



        item = self.tableWidget_3.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "08:00~10:00"))
        item = self.tableWidget_3.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "10:00~12:00"))
        item = self.tableWidget_3.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "12:00~14:00"))
        item = self.tableWidget_3.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "14:00~16:00"))
        item = self.tableWidget_3.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "16:00~18:00"))
        item = self.tableWidget_3.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "18:00~20:00"))
        item = self.tableWidget_3.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "20:00~22:00"))
        item = self.tableWidget_3.verticalHeaderItem(7)
        item.setText(_translate("MainWindow", "22:00~00:00"))
        item = self.tableWidget_3.verticalHeaderItem(8)
        item.setText(_translate("MainWindow", "00:00~02:00"))
        item = self.tableWidget_3.verticalHeaderItem(9)
        item.setText(_translate("MainWindow", "02:00~04:00"))
        item = self.tableWidget_3.verticalHeaderItem(10)
        item.setText(_translate("MainWindow", "04:00~06:00"))
        item = self.tableWidget_3.verticalHeaderItem(11)
        item.setText(_translate("MainWindow", "06:00~08:00"))
        item = self.tableWidget_3.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "상황병"))
        item = self.tableWidget_3.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "CCTV"))


        #상황,CCTV
        __sortingEnabled = self.tableWidget_3.isSortingEnabled()
        self.tableWidget_3.setSortingEnabled(False)

        x=0
        for row in range(12):
            for col in range(2):
                item = self.tableWidget_3.item(row, col)
                print('row,col ',row,col, x)
                item.setText(_translate("mainWindow", inside[x][1]))
                x = (x+1) % n_inside
                con = pymysql.connect(host="localhost", user="root", password="1234",
                                      db='App', charset='utf8')
                cur = con.cursor()
                if (row < 5):
                    query = "UPDATE soldier SET score = score + %s WHERE name = %s"
                    cur.execute(query, (10, inside[x][1]))
                    con.commit()
                elif (row >=5 and row < 9):
                    query = "UPDATE soldier SET score = score + %s WHERE name = %s"
                    cur.execute(query, (20, inside[x][1]))
                    con.commit()
                elif (row >=9):
                    query = "UPDATE soldier SET score = score + %s WHERE name = %s"
                    cur.execute(query, (15, inside[x][1]))
                    con.commit()

        self.tableWidget_3.setSortingEnabled(__sortingEnabled)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "상황/cctv"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_TodayTable()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

