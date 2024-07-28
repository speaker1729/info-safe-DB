# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'container_logger.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
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
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QTextBrowser, QWidget,QMainWindow)
from PySide6 import QtCore

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(798, 563)
        self.textBrowser = QTextBrowser(Form)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(40, 50, 551, 491))
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(50, 20, 53, 16))
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(620, 60, 101, 41))

        self.retranslateUi(Form)
        self.pushButton.clicked.connect(Form.display)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u65e5\u5fd7", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u52a0\u8f7d", None))
    # retranslateUi

import Module.Logger as Logger
class containlogger(QMainWindow):
    def __init__(self, base):
        super().__init__()
        # 继承主窗口
        self.dbmain = base
        # 选择的文件名
        self.filename = None
        self.ui = Ui_Form()
        self.ui.setupUi(self)

    @QtCore.Slot()
    def display(self):
        self.ui.textBrowser.clear()
        logs = Logger.log_load(self.dbmain.user_cur[1])
        for log in logs:
            self.ui.textBrowser.append(log[0]+' '+log[1]+'\n')
            self.ui.textBrowser.ensureCursorVisible()