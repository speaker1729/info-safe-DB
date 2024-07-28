import sys
from PySide6.QtWidgets import QApplication 
from login import ui_mainwindoe
from enroll import enrollwindoe
from admin_container import admin_containerwindow
from user_container import user_containerwindow
class dbmain(object):
    #初始化
    def __init__(self) :
        self.app=QApplication()
        #初始化登录和注册窗口
        self.m_login=ui_mainwindoe(self)
        self.m_enroll=enrollwindoe(self)
        #初始化管理员与用户窗口
        #self.m_adminwindow=admin_containerwindow(self)
        #self.m_userwindow=user_containerwindow(self)
        self.m_adminwindow=None
        self.m_userwindow=None

        #全局变量
        self.user_cur = None
        self.is_admin = None
        self.file_cur = None
    def process(self):
        self.m_login.show()
        self.app.exec()

    # 重建两个窗口
    def rebuild(self):
        self.m_login.destroy()
        self.m_enroll.destroy()
        self.m_login = None
        self.m_enroll = None
        self.m_login = ui_mainwindoe(self)
        self.m_enroll = enrollwindoe(self)
        self.user_cur = None
        self.file_cur = None

test=dbmain()
test.process()