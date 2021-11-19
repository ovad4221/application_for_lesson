from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QColorDialog, QInputDialog, \
    QTableWidgetItem
import sys
import csv
from random import randint
from PyQt5.QtCore import Qt
import json
from PyQt5 import uic
from main_window import Ui_MainWindow
from help_functions import *


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.InitUi()

    def InitUi(self):
        self.setWindowTitle('Домашка')
        self.mean_marks_for_lesson.clicked.connect(self.mean_marks_funk)
        self.from_teacher.clicked.connect(self.from_teacher_funk)
        self.corr_data_teacher.clicked.connect(self.corr_data_teacher_funk)
        self.corr_data_lesson.clicked.connect(self.corr_data_lesson_funk)
        self.corr_mark.clicked.connect(self.corr_mark_funk)

    def mean_marks_funk(self):
        self.lcdNumber.display(0)
        mark = mean_mark_of_les(self.name_lesson.text())
        if type(mark) == float:
            self.lcdNumber.display(mark)
        else:
            self.statusbar.showMessage(mark, 3000)

    def from_teacher_funk(self):
        self.lineEdit_2.setText('')
        lesson, flag = lesson_from_tes(self.name_teacher.text())
        if flag:
            self.lineEdit_2.setText(lesson)
        else:
            self.statusbar.showMessage(lesson, 3000)

    def corr_data_teacher_funk(self):
        pass

    def corr_data_lesson_funk(self):
        pass

    def corr_mark_funk(self):
        pass


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    sys.excepthook = except_hook
    ex.show()
    sys.exit(app.exec_())
