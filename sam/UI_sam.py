# -*- coding: utf-8 -*-

"""
Module implementing Test.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog

from .Ui_sam import Ui_Dialog


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
        