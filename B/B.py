# -*- coding: utf-8 -*-

"""
Module implementing Test.
"""

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog
from PyQT5.Ui_B import Ui_Dialog


class Test(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(Test, self).__init__(parent)
        self.setupUi(self)
    
    @pyqtSlot()
    def on_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        
        # TODO: not implemented yet
        # raise NotImplementedError
        
        print ('abacadfasfadfsafsaaaaaaaaaa')
    
    @pyqtSlot()
    def on_pushButton_released(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Test()
    ui.show()
    sys.exit(app.exec_())
