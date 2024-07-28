# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'container.ui'
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
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenuBar, QSizePolicy,
    QStackedWidget, QStatusBar, QToolBar, QWidget,QPushButton)
from container_cfile import containcfile
from container_cuser import containercuser
from PySide6 import QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(806, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(9, -1, 791, 541))
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.stackedWidget.addWidget(self.page)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.stackedWidget.addWidget(self.page_3)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stackedWidget.addWidget(self.page_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 806, 22))
        MainWindow.setMenuBar(self.menubar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

from container_logger import containlogger
class admin_containerwindow(QMainWindow):
    def __init__(self,base):
        super().__init__()
        # 继承主窗口
        self.dbmain = base
        #
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        #qstackedwidget所要显示的页面
        self.wigcfile=containcfile(base)
        self.wigcuser=containercuser(base)
        self.wiglogger = containlogger(base) # 日志
        #页面索引（方便显示页面）
        self.index_wigcfile=self.ui.stackedWidget.addWidget(self.wigcfile)
        self.index_wigcuser=self.ui.stackedWidget.addWidget(self.wigcuser)
        self.index_wiglogger = self.ui.stackedWidget.addWidget(self.wiglogger) # 日志
        self.ui.stackedWidget.setCurrentIndex(-1)
        #菜单栏
        user_manage_menu=self.ui.menubar.addMenu("用户管理")
        file_updown_menu=self.ui.menubar.addMenu("文件管理")
        log_menu = self.ui.menubar.addMenu("日志") # 日志
        user_manage_menu.addAction("文件访问权限").triggered.connect(self.cuser_view_action)
        file_updown_menu.addAction("文件上传下载").triggered.connect(self.cfile_view_action)
        log_menu.addAction("显示日志").triggered.connect(self.logger_view_action) # 日志
    def cuser_view_action(self):
        self.ui.stackedWidget.setCurrentIndex(self.index_wigcuser)
    def cfile_view_action(self):
        self.ui.stackedWidget.setCurrentIndex(self.index_wigcfile)
    def logger_view_action(self):
        self.ui.stackedWidget.setCurrentIndex(self.index_wiglogger)
        

#app=QApplication()
#temp =admin_containerwindow()
#temp.show()
#app.exec()