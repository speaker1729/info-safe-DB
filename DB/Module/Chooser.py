import os
from PySide6 import QtWidgets
from PySide6.QtCore import QDir, Qt
from PySide6.QtWidgets import QApplication, QFileDialog


def file_choose():
    file_dialog = QFileDialog()
    file_dialog.setOption(QFileDialog.DontUseNativeDialog)
    file_dialog.setFileMode(QFileDialog.ExistingFiles)
    file_dialog.exec()
    selected_file = file_dialog.selectedFiles()
    return selected_file


def folder_choose():
    file_dialog = QFileDialog()
    file_dialog.setFileMode(QFileDialog.Directory)
    file_dialog.exec()
    selected_folder = file_dialog.selectedFiles()[0]
    return selected_folder


if __name__ == '__main__':
    app = QApplication()
    print("任意选择单个文件")
    print(file_choose())
    print("任意选择多个文件")
    print(file_choose())
    print("任意选择一个文件夹")
    print(folder_choose())
