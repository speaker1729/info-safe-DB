# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import sys

from PySide6 import QtCore,QtWidgets
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget,QMainWindow)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(402, 228)
        Form.setCursor(QCursor(Qt.ArrowCursor))
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(90, 20, 71, 41))
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(80, 130, 54, 16))
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(100, 60, 91, 41))
        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(150, 30, 151, 21))
        self.lineEdit_2 = QLineEdit(Form)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(150, 70, 151, 21))
        self.checkBox = QCheckBox(Form)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(150, 110, 131, 20))
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(260, 160, 75, 24))
        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(100, 160, 75, 24))

        self.retranslateUi(Form)
        self.pushButton.clicked.connect(Form.login)
        self.pushButton_2.clicked.connect(Form.enroll)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"login", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u7528\u6237\u540d", None))
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("Form", u"\u5bc6\u7801", None))
        self.checkBox.setText(QCoreApplication.translate("Form", u"\u6211\u540c\u610f\u7528\u6237\u534f\u8bae", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u767b\u5f55", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"\u6ce8\u518c", None))
    # retranslateUi

import Module.User as User
import Module.Admin as Admin
import Module.Logger as Logger
from PySide6.QtWidgets import *
from admin_container import admin_containerwindow
from user_container import user_containerwindow
class ui_mainwindoe(QMainWindow):
    def __init__(self,base):
        super().__init__()
        #将dbmain的指针保存
        self.dbmain=base
        self.ui=Ui_Form()
        self.ui.setupUi(self)
    @QtCore.Slot()
    def login(self):
        username = self.ui.lineEdit.text()
        password = self.ui.lineEdit_2.text()
        statue = User.login(username, password)
        # 展示状态
        # self.ui.lab_statue.setText(statue + ' ' + username)
        Logger.log_save(statue + ' ' + username)
        # 导入用户
        if statue == '登录成功':
            # 展示用户
            # self.ui.lab_user.setText(username)
            # 导入用户名
            self.dbmain.user_cur = (username, password)
            # 导入文件
            self.dbmain.file_cur = User.load(username, password)
            if username == 'admin':
                # 管理员可访问用户列表
                self.dbmain.is_admin = True
                # 管理员可访问所有文件
                self.dbmain.file_cur = Admin.load_list(password)
                # 显示管理员窗口
                self.dbmain.m_adminwindow = admin_containerwindow(self.dbmain)
                self.dbmain.m_adminwindow.show()
                # 注销登录窗口
                self.close()
            else:
                # 显示用户窗口
                self.dbmain.m_userwindow = user_containerwindow(self.dbmain)
                self.dbmain.m_userwindow.show()
                # 注销登录窗口
                self.close()
        else:
            QMessageBox.about(self, 'Tips', statue + ' ' + username)


    @QtCore.Slot()
    def enroll(self):
        #显示注册窗口
        self.dbmain.m_enroll.show()
        #销毁登录窗口
        self.close()
#app=QtWidgets.QApplication(sys.argv)
#window=ui_mainwindoe()
#window.show()
#app.exec()