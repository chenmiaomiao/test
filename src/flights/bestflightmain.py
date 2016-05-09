# _*_ coding: utf8 _*_

import sys
import time
import datetime
import sqlite3
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from PyQt4 import QtGui, QtCore, Qt
from PyQt4.Qt import QGridLayout
from datetime import timedelta

class Window(QtGui.QMainWindow):
    
    
    def __init__(self):
        self.conn = sqlite3.connect('stock.sqlite3')
        self.cur = self.conn.cursor()
        
        super(Window, self).__init__()
        
        self.result_thread = Worker()
        
        
        self.main_widget = QtGui.QWidget(self)
        self.setCentralWidget(self.main_widget)
        
        self.setGeometry(50, 50, 1280, 800)
        self.setWindowTitle(u'BestFlight')
        self.setWindowIcon(QtGui.QIcon('plane.png'))
        self.setWindowOpacity(0.95)
        
        # action of file
        self.act_file_exit = QtGui.QAction('&Exit', self)
        self.act_file_exit.setShortcut('Ctrl+Q')
        self.act_file_exit.setStatusTip('Leave The App')
        self.act_file_exit.triggered.connect(self.close_application)
        # action of help>style
        self.act_style_all = QtGui.QActionGroup(self)
        self.act_style_plastique= QtGui.QAction('Plastique', self.act_style_all)# , checkable = True)
        self.act_style_cleanlooks = QtGui.QAction('Cleanlooks', self.act_style_all)# , checkable = True)
        self.act_style_all.triggered.connect(self.style_set)
        self.style_actions = (self.act_style_plastique, self.act_style_cleanlooks)
        self.act_style_plastique.trigger()
        # action of help
        self.act_help_about = QtGui.QAction('&About', self)
        self.act_help_about.setStatusTip('About The App')
        self.act_help_about.triggered.connect(self.about)
          
        # self.statusBar()
          
        # sub menu of help
        self.sub_help_style = QtGui.QMenu('Style', self)
        self.sub_help_style.addActions(self.style_actions)
          
        # main menu
        self.menu_main = self.menuBar()
        # file menu
        self.menu_file = self.menu_main.addMenu('&File')
        self.menu_file.addAction(self.act_file_exit)
        # help menu
        self.menu_help = self.menu_main.addMenu('&Help')
        self.menu_help.addMenu(self.sub_help_style)
        self.menu_help.addAction(self.act_help_about)

        self.home()
        
    def home(self):
        # domestic or international
        search_combobox = QtGui.QComboBox()
        search_combobox.addItem('Domestic')
        search_combobox.addItem('International')
        
        # city
        search_dep_city = QtGui.QLabel('From: ')
        search_arr_city = QtGui.QLabel('To: ')
        
        # search input
        search_input_departure = QtGui.QLineEdit()
        search_input_arrival = QtGui.QLineEdit()
        
        # search button
        search_button = QtGui.QPushButton('Search')
        
        # search area layout
        search_layout = QtGui.QGridLayout()
        search_layout.setSpacing(0)
        search_layout.setColumnStretch(0, 1)
        search_layout.setColumnStretch(1, 1)
        search_layout.setColumnStretch(2, 1)
        search_layout.setColumnStretch(3, 1)
        search_layout.setColumnStretch(4, 1)
        search_layout.setColumnStretch(5, 1)
        search_layout.addWidget(search_combobox, 2, 1)
        search_layout.addWidget(search_dep_city, 1, 2)
        search_layout.addWidget(search_input_departure, 2, 2)
        search_layout.addWidget(search_arr_city, 1, 3)
        search_layout.addWidget(search_input_arrival, 2, 3)
        search_layout.addWidget(search_button, 2, 4)
        
        # advanced area
        days_label = QtGui.QLabel('Days: ')
        days_min = QtGui.QSpinBox()
        days_min.setRange(1, 30)
        days_min.setValue(3)
        days_min.valueChanged.connect(lambda ignore: self.update_spin_range(ignore, days_min.value(), 30))
        days_label_to = QtGui.QLabel(' ~ ')
        self.days_max = QtGui.QSpinBox()
        self.days_max.setRange(1, 30)
        self.days_max.setValue(5)
        self.days_max.valueChanged.connect(lambda ignore: self.update_spin_range(ignore, days_min.value(), 30))
        
        current = time.time()
        cal_start = QtGui.QCalendarWidget()
        cal_end = QtGui.QCalendarWidget()
        timeframe_lable = QtGui.QLabel('Time Frame: ')
        timeframe_start = QtGui.QDateEdit()
        timeframe_start.setDate(datetime.datetime.fromtimestamp(current))
        timeframe_start.setDateRange(datetime.datetime.fromtimestamp(current), 
                                     datetime.datetime.fromtimestamp(current) + datetime.timedelta(365))
        timeframe_start.setCalendarPopup(True)
        timeframe_start.setCalendarWidget(cal_start)
        timeframe_label_to = QtGui.QLabel(' ~ ')
        timeframe_end = QtGui.QDateEdit()
        timeframe_end.setDate(datetime.datetime.fromtimestamp(current) + datetime.timedelta(20))
        timeframe_end.setDateRange(datetime.datetime.fromtimestamp(current), 
                                   datetime.datetime.fromtimestamp(current) + datetime.timedelta(365))
        timeframe_end.setCalendarPopup(True)
        timeframe_end.setCalendarWidget(cal_end)
        
        dep_time_label = QtGui.QLabel('Departure Time: ')
        dep_time_begin = QtGui.QTimeEdit()
        dep_time_to = QtGui.QLabel(' ~ ')
        dep_time_over = QtGui.QTimeEdit()
        
        overnight_avoid_label = QtGui.QLabel('Overnight Avoid: ')
        overnight_avoid = QtGui.QCheckBox()
        
        weekends_prefer_label = QtGui.QLabel('Weekeends Prefer: ')
        weekends_prefer = QtGui.QCheckBox()
        
        # advanced area layout
        search_advanced_layout = QtGui.QGridLayout()
        search_advanced_layout.addWidget(days_label, 0, 0)
        search_advanced_layout.addWidget(days_min, 0, 1)
        search_advanced_layout.addWidget(days_label_to, 0, 2)
        search_advanced_layout.addWidget(self.days_max, 0, 3)
        
        search_advanced_layout.addWidget(timeframe_lable, 1, 0)
        search_advanced_layout.addWidget(timeframe_start, 1, 1)
        search_advanced_layout.addWidget(timeframe_label_to, 1, 2)
        search_advanced_layout.addWidget(timeframe_end, 1, 3)
        
        search_advanced_layout.addWidget(dep_time_label, 2, 0)
        search_advanced_layout.addWidget(dep_time_begin, 2, 1)
        search_advanced_layout.addWidget(dep_time_to, 2, 2)
        search_advanced_layout.addWidget(dep_time_over, 2, 3)
        
        search_advanced_layout.addWidget(overnight_avoid_label, 3, 0)
        search_advanced_layout.addWidget(overnight_avoid, 3, 1)
        
        search_advanced_layout.addWidget(weekends_prefer_label, 4, 0)
        search_advanced_layout.addWidget(weekends_prefer, 4, 1)
        
        # result area layout
        self.result_main = QtGui.QWidget()
                
        bottom_layout = QtGui.QHBoxLayout()
        bottom_layout.addLayout(search_advanced_layout, stretch = 1)
        bottom_layout.addWidget(self.result_main, stretch = 20)
        
        # global layout
        global_layout = QtGui.QVBoxLayout()
        global_layout.setSpacing(10)
        global_layout.addSpacing(50)
        global_layout.addLayout(search_layout, stretch = 1)
        global_layout.addLayout(bottom_layout, stretch = 20)
        
        self.main_widget.setLayout(global_layout)
        
        # prepare the canvas    
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        
        # set the layout of result_main
        result_main_layout = QtGui.QVBoxLayout()
        result_main_layout.addWidget(self.canvas)
        self.result_main.setLayout(result_main_layout)        
        # self.show()
        
        # connect
        search_input_departure.returnPressed.connect(lambda: self.search(search_combobox.currentText(), 
                                                                         search_input_departure.text(), 
                                                                         search_input_arrival.text(), 
                                                                         days_min.value(), 
                                                                         self.days_max.value(), 
                                                                         dep_time_begin.date(), 
                                                                         dep_time_over.date(), 
                                                                         overnight_avoid.isTristate(), 
                                                                         weekends_prefer.isTristate()
                                                                         )
                                                     )
        
        search_button.clicked.connect(lambda: self.search(search_combobox.currentText(), 
                                                          search_input_departure.text(), 
                                                          search_input_arrival.text(), 
                                                          days_min.value(), 
                                                          self.days_max.value(), 
                                                          dep_time_begin.date(), 
                                                          dep_time_over.date(), 
                                                          overnight_avoid.isTristate(), 
                                                          weekends_prefer.isTristate()
                                                          )
                                      )
        
    def search(self, *args):
        
        print args
        # self.result_thread.result_item_emitted[list, list].connect(self.plot_preprocessing)
        
        # query database
        # self.cur.execute("SELECT DISTINCT reportdate, holdersnumber FROM Majorholderinfo WHERE stockid = ? AND reportdate <> '-1' AND holdersnumber <> '-1'", ('%s' % search_text, ))
        # results = self.cur.fetchall()

        #update the browser
        # self.result_thread.show(results)
        
    
    def update_spin_range(self, ignore, value, range_max):
        if ignore > self.days_max.value():
            self.days_max.setValue(ignore)
        self.days_max.setRange(value, 30)
        
    def style_set(self, action_triggered):
        QtGui.QApplication.setStyle(QtGui.QStyleFactory.create(action_triggered.text()))
           
    def about(self):
        pass

    def close_application(self):
        self.cur.close()
        self.conn.close
        sys.exit()
        

class Worker(QtCore.QThread):
    # result_item_emitted = QtCore.pyqtSignal([str], [list, list])
    
    def __init__(self, parent = None):
        super(Worker, self).__init__(parent = None)
    
    #===========================================================================
    # def __del__(self):
    #     self.wait()
    #===========================================================================
        
    def show(self, results):
        self.results = results
        self.start()
    
    def run(self):
        pass
        
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    GUI.show()
    sys.exit(app.exec_())    