# -*- coding: utf-8 -*-

"""
Module implementing c.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from Ui_jishiben import Ui_MainWindow


class c(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(c, self).__init__(parent)
        self.setupUi(self)
    
    @pyqtSlot()
    def on_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        #raise NotImplementedError
        a = QtWidgets.QMessageBox.information(self,u'测试报告',u'测试',)
        #self.textEdit.setText('')
        #self.textEdit.setText('dfadfdfs')

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = c()
    ui.setupUi(MainWindow)
    ui.show()
    sys.exit(app.exec_())