#!/usr/bin/python
#-*- coding:utf-8 -*-

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class changeVisibility(QWidget):
    main_widgets = []
    
    def __init__(self, parent=None):        
        super(changeVisibility, self).__init__(parent)
        
        self.v_layout_A = QWidget(self)
        self.v_layout_B = QWidget(self)
        
        self.textbrowserA = QTextBrowser(self.v_layout_A)
        self.textbrowserA.setStyleSheet("background-color:red")

        self.textbrowserB = QTextBrowser(self.v_layout_B)
        self.textbrowserB.setStyleSheet("background-color:blue")


        self.buttonA = QPushButton("Show A", self.v_layout_A)
        self.buttonB = QPushButton("Show B", self.v_layout_A)

        self.verticalLayout = QVBoxLayout(self.v_layout_A)
        #self.verticalLayout.addWidget(self.v_layout_A)
        self.verticalLayout.addWidget(self.textbrowserA)
        #self.verticalLayout.addWidget(self.buttonA)
        self.verticalLayout.addWidget(self.buttonB)
        
        self.verticalLayout_B = QVBoxLayout(self.v_layout_B)
        self.verticalLayout_B.addWidget(self.textbrowserB)
        self.verticalLayout_B.addWidget(self.buttonA)
        #self.verticalLayout_B.addWidget(self.buttonB)
        
        self.main_widgets.append(self.v_layout_A)
        self.main_widgets.append(self.v_layout_B)
        
        self.toggle_widget(self.v_layout_A, self.main_widgets)
        #=======================================================================
        # self.v_layout_A.show()
        # self.v_layout_B.hide()
        #=======================================================================

        self.buttonA.clicked.connect(self.showA)
        self.buttonB.clicked.connect(self.showB)

    def showA(self):
        self.toggle_widget(self.v_layout_A, self.main_widgets)
        #=======================================================================
        # self.v_layout_B.hide()
        # self.v_layout_A.show()
        #=======================================================================

    def showB(self):
        self.toggle_widget(self.v_layout_B, self.main_widgets)
        #=======================================================================
        # self.v_layout_A.hide()
        # self.v_layout_B.show()
        #=======================================================================

    def toggle_widget(self, show_widget, widgets):
        for widget in widgets:
            if widget == show_widget:
                widget.show()
            else:
                widget.hide()

def main():
    app = QApplication(sys.argv)
    cV = changeVisibility()
    cV.show()
    app.exec_()


if __name__ == '__main__':
    main()