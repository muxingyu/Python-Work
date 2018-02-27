# -*- coding: utf-8 -*-

"""
Module implementing abc.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow

from .Ui_NEWW1 import Ui_MainWindow


class abc(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(abc, self).__init__(parent)
        self.setupUi(self)


#text

#text