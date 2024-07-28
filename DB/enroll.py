# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'enroll.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6 import QtCore
from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect)
from PySide6.QtWidgets import (QLabel, QLineEdit, QPushButton)


class Ui_enroll(object):
    def setupUi(self, enroll):
        if not enroll.objectName():
            enroll.setObjectName(u"enroll")
        enroll.resize(386, 215)
        self.lineEdit = QLineEdit(enroll)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(150, 30, 161, 20))
        self.lineEdit_2 = QLineEdit(enroll)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(150, 70, 161, 20))
        self.lineEdit_4 = QLineEdit(enroll)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(150, 110, 161, 20))
        self.label = QLabel(enroll)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(70, 30, 54, 16))
        self.label_2 = QLabel(enroll)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(70, 70, 54, 16))
        self.label_3 = QLabel(enroll)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(70, 110, 54, 16))
        self.pushButton = QPushButton(enroll)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(240, 150, 75, 24))

        self.retranslateUi(enroll)
        self.pushButton.clicked.connect(enroll.slot1)

        QMetaObject.connectSlotsByName(enroll)
    # setupUi

    def retranslateUi(self, enroll):
        enroll.setWindowTitle(QCoreApplication.translate("enroll", u"Form", None))
        self.label.setText(QCoreApplication.translate("enroll", u"\u59d3\u540d\uff1a", None))
        self.label_2.setText(QCoreApplication.translate("enroll", u"\u5de5\u53f7\uff1a", None))
        self.label_3.setText(QCoreApplication.translate("enroll", u"\u5bc6\u7801\uff1a", None))
        self.pushButton.setText(QCoreApplication.translate("enroll", u"\u6ce8\u518c", None))
    # retranslateUi

import Module.User as User
import Module.Admin as Admin
import Module.Logger as Logger
from PySide6.QtWidgets import *


class enrollwindoe(QMainWindow):
    def __init__(self,base):
        super().__init__()
        self.ui=Ui_enroll()
        self.ui.setupUi(self)
        self.dbmain=base
    @QtCore.Slot()
    def slot1(self):
        username = self.ui.lineEdit.text()
        id = self.ui.lineEdit_2.text()
        password = self.ui.lineEdit_4.text()
        statue = User.registry(username, password)
        # 展示状态
        # self.ui.lab_statue.setText(statue + ' ' + username)
        Logger.log_save(statue + ' ' + username)
        # 创建用户文件访问列表
        if statue == '注册成功':
            if username == 'admin':
                # 管理员访问全部文件
                User.save(username, password, [['*', '*']])
                # 并创建密钥对
                Admin.create(password)
            else:
                # 其他用户默认无文件访问
                User.save(username, password, [['^', '^']])
                # 保存该用户的密钥
                Admin.save_key(username, password)
            # 显示登录窗口
            self.dbmain.m_login.show()
            # 注销注册窗口
            # self.destroy()
            self.close()
        else:
            QMessageBox.about(self, 'Tips', statue + ' ' + username)
