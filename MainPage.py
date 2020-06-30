# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainPage.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql
from InfoManage import UI_InfoManageDialog
from TodayTable import Ui_TodayTable
from listtest import Ui_ScoreTable

def createDB():
    con = pymysql.connect(host='localhost', user='root', password='1234', charset='utf8')
    cur = con.cursor()
    sql = 'CREATE DATABASE App'
    cur.execute(sql)
    con.commit()

def create_soldierTable():
    con = pymysql.connect(host="localhost", user="root", password="1234",
                          db='App', charset='utf8')
    cur = con.cursor()
    sql = "create table soldier(" \
          "number varchar(15)," \
          "name varchar(10) not null," \
          "work varchar(20) default '소총수'," \
          "state int not null default '1' ," \
          "score int default '0'," \
          "primary key (number))"
    cur.execute(sql)
    con.commit()


def create_timeTable():
    con = pymysql.connect(host="localhost", user="root", password="1234",
                          db='App', charset='utf8')
    cur = con.cursor()
    sql = "create table timetable(" \
          "TimeName varchar(15)," \
          "TimeScore double," \
          "primary key (timename))"
    cur.execute(sql)
    con.commit()
    insert_timeTable()

def insert_timeTable():
    con = pymysql.connect(host="localhost", user="root", password="1234",
                          db='App', charset='utf8')
    cur = con.cursor()
    query = ("insert into timetable(TimeName, TimeScore) values(%s,%s)")
    cur.execute(query, ("08:00~10:00", 1.0))
    cur.execute(query, ("10:00~12:00", 1.0))
    cur.execute(query, ("12:00~14:00", 1.0))
    cur.execute(query, ("14:00~16:00", 1.0))
    cur.execute(query, ("16:00~18:00", 1.5))
    cur.execute(query, ("18:00~20:00", 1.5))
    cur.execute(query, ("20:00~22:00", 1.5))
    cur.execute(query, ("22:00~00:00", 1.5))
    cur.execute(query, ("00:00~02:00", 2.0))
    cur.execute(query, ("02:00~04:00", 2.0))
    cur.execute(query, ("04:00~06:00", 2.0))
    cur.execute(query, ("06:00~08:00", 2.0))
    con.commit()

def create_workTable():
    con = pymysql.connect(host="localhost", user="root", password="1234",
                          db='App', charset='utf8')
    cur = con.cursor()
    sql = "create table worktable(" \
          "WorkName varchar(15)," \
          "WorkScore int," \
          "primary key (WorkName))"
    cur.execute(sql)
    con.commit()
    insert_workTable()

def insert_workTable():
    con = pymysql.connect(host="localhost", user="root", password="1234",
                          db='App', charset='utf8')
    cur = con.cursor()
    query = ("insert into worktable(WorkName, WorkScore) values(%s,%s)")
    cur.execute(query, ("위병소", 15))
    cur.execute(query, ("탄약고", 20))
    cur.execute(query, ("상황병", 10))
    cur.execute(query, ("CCTV", 10))
    con.commit()



class Ui_Dialog(object):
    def createsql(self):
        try:
            createDB()
        except:
            pass

        try:
            create_timeTable()
        except:
            pass

        try:
            create_soldierTable()
        except:
            pass

        try:
            create_workTable()
        except:
            pass



    def openInfoManager(self):
        self.window = QtWidgets.QDialog()
        self.ui = UI_InfoManageDialog()
        self.ui.setupUi (self.window)
        self.window.show()

    def openTodayTable(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_TodayTable()
        self.ui.setupUi(self.window)
        self.window.show()

    def openScoreTable(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_ScoreTable()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, Dialog):
        self.createsql()
        Dialog.setObjectName("Dialog")
        Dialog.resize(800, 500)

        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 801, 501))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("C:/Users/seo/Desktop/DBUI/mainback.jpeg"))
        self.label_2.setObjectName("label_2")


        self.InfoManager = QtWidgets.QPushButton(Dialog)
        self.InfoManager.setGeometry(QtCore.QRect(65, 290, 161, 60))
        font = QtGui.QFont()
        font.setFamily("Jalnan OTF")
        font.setPointSize(14)
        self.InfoManager.setFont(font)
        self.InfoManager.setObjectName("InfoManager")

        self.InfoManager.clicked.connect(self.openInfoManager)



        self.TodayTable = QtWidgets.QPushButton(Dialog)
        self.TodayTable.setGeometry(QtCore.QRect(230, 290, 161, 60))
        font = QtGui.QFont()
        font.setFamily("Jalnan OTF")
        font.setPointSize(15)
        self.TodayTable.setFont(font)
        self.TodayTable.setObjectName("TodayTable")

        self.TodayTable.clicked.connect(self.openTodayTable)



        self.LastTable = QtWidgets.QPushButton(Dialog)
        self.LastTable.setGeometry(QtCore.QRect(400, 290, 161, 60))
        font = QtGui.QFont()
        font.setFamily("Jalnan OTF")
        font.setPointSize(15)
        self.LastTable.setFont(font)
        self.LastTable.setObjectName("LastTable")





        self.WorkScore = QtWidgets.QPushButton(Dialog)
        self.WorkScore.setGeometry(QtCore.QRect(570, 290, 161, 60))
        font = QtGui.QFont()
        font.setFamily("Jalnan OTF")
        font.setPointSize(15)
        self.WorkScore.setFont(font)
        self.WorkScore.setObjectName("WorkScore")
        self.WorkScore.clicked.connect(self.openScoreTable)


        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.InfoManager.setText(_translate("Dialog", "정보 관리"))
        self.TodayTable.setText(_translate("Dialog", "오늘 근무표"))
        self.LastTable.setText(_translate("Dialog", "이전 근무표"))
        self.WorkScore.setText(_translate("Dialog", "점수 확인"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
