# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'container-cuser.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QListView, QPushButton,
    QSizePolicy, QWidget,QMainWindow)
from PySide6 import QtCore
class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(798, 563)
        self.listView = QListView(Form)
        self.listView.setObjectName(u"listView")
        self.listView.setGeometry(QRect(40, 70, 211, 341))
        self.listView_2 = QListView(Form)
        self.listView_2.setObjectName(u"listView_2")
        self.listView_2.setGeometry(QRect(290, 70, 211, 341))
        self.listView_3 = QListView(Form)
        self.listView_3.setObjectName(u"listView_3")
        self.listView_3.setGeometry(QRect(540, 70, 211, 341))
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(210, 450, 111, 51))
        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(470, 450, 111, 51))
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(50, 40, 81, 21))
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(300, 40, 81, 21))
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(550, 40, 81, 21))

        self.retranslateUi(Form)
        self.pushButton.clicked.connect(Form.add)
        self.pushButton_2.clicked.connect(Form.delete)
        #self.listView.clicked.connect(Form.changeview)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u589e\u52a0\u6587\u4ef6", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"\u5220\u9664\u6587\u4ef6", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u7528\u6237\u89c6\u56fe", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u6587\u4ef6\u89c6\u56fe", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u7528\u6237\u6587\u4ef6\u89c6\u56fe", None))
    # retranslateUi

from PySide6.QtGui import QStandardItem, QStandardItemModel
import Module.File as File
import Module.User as User
import Module.Admin as Admin
class containercuser(QMainWindow):
    def __init__(self,base):
        super().__init__()
        # 继承主窗口
        self.dbmain = base
        self.model = [QStandardItemModel() for _ in range(3)]
        # 选择的文件名
        self.user = None
        self.filename = None
        self.userfile = None
        # 临时变量
        self.file_tem = None
        self.user_tem = None
        self.ui=Ui_Form()
        self.ui.setupUi(self)
        # 绑定函数
        self.ui.listView.clicked.connect(self.select_0)
        self.ui.listView_2.clicked.connect(self.select_1)
        self.ui.listView_3.clicked.connect(self.select_2)
        self.changeview()
    @QtCore.Slot()
    def add(self):
        # 清理现文件再添加
        # 获取文件名
        filename = self.filename
        # 找到并添加
        for i in range(len(self.dbmain.file_cur)):
            if self.dbmain.file_cur[i][0] == filename:
                t = [filename, self.dbmain.file_cur[i][1]]
                self.file_tem.append(t)
                # GUI
                self.refresh()
                break
        self.apply()
    @QtCore.Slot()
    def delete(self):
        # 获取文件名
        filename = self.userfile
        # 找到并删除
        for i in range(len(self.file_tem)):
            if self.file_tem[i][0] == filename:
                self.file_tem.pop(i)
                # GUI
                self.refresh()
                break
        self.apply()
    def apply(self):
        # 应用
        username = self.user_tem[0]
        password = self.user_tem[1]
        User.save(username, password, self.file_tem)
    def changeview(self):
        # 列出所有用户
        files = File.get_all('Users/sha')
        # 除去管理员
        files.remove('admin')
        # 清理现文件再添加
        self.model[0].clear()
        for file in files:
            item = QStandardItem(file)
            self.model[0].appendRow(item)
        self.ui.listView.setModel(self.model[0])
        # 清理现文件再添加
        self.model[1].clear()
        # 获取已上传的全部文件
        files = File.get_all('Data')
        for file in files:
            item = QStandardItem(file)
            self.model[1].appendRow(item)
        self.ui.listView_2.setModel(self.model[1])
    def refresh(self):
        # 清理现文件再添加
        self.model[2].clear()
        files = File.filter(self.file_tem)
        for file in files:
            item = QStandardItem(file[0])
            self.model[2].appendRow(item)
        self.ui.listView_3.setModel(self.model[2])
    # 绑定
    def select_0(self, index):
        # 选取文件页面的列表
        selected_item = self.model[0].itemFromIndex(index)
        # 将选择的文件存储
        self.user = selected_item.text()
        # 列出用户的可访问文件
        # 如果没有临时用户
        if not self.user_tem:
            # 列表中选择的用户名
            username = self.user
            # 管理员导入该用户的密钥
            password = Admin.load_key(username, self.dbmain.user_cur[1])
            # 临时用户导入
            self.user_tem = [username, password]
        else:
            username = self.user_tem[0]
            password = self.user_tem[1]
        # 导入文件
        self.file_tem = User.load(username, password)
        files = File.filter(self.file_tem)
        # 清理现文件再添加
        self.model[2].clear()
        for file in files:
            item = QStandardItem(file[0])
            self.model[2].appendRow(item)
        self.ui.listView_3.setModel(self.model[2])

    def select_1(self, index):
        # 选取文件页面的列表
        selected_item = self.model[1].itemFromIndex(index)
        # 将选择的文件存储
        self.filename = selected_item.text()

    def select_2(self, index):
        # 选取文件页面的列表
        selected_item = self.model[2].itemFromIndex(index)
        # 将选择的文件存储
        self.userfile = selected_item.text()
