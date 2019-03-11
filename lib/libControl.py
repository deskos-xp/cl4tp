#! /usr/bin/python3

from PyQt5 import QtWidgets,QtCore,QtGui

class controls:
    def __init__(self):
        pass

    def init(me,self):
        me.actions(self)
        #me.buttons(self)

    def actions(me,self):
        self.action_Quit.triggered.connect(QtWidgets.QApplication.quit)
        self.action_N_RSA_Key.triggered.connect(self.nk['dialog'].show)
        self.action_Tab_Defaults.triggered.connect(self.td['dialog'].show)
        self.action_Application_wide_Settings.triggered.connect(self.es['dialog'].show)
        self.actionNew_Config.triggered.connect(lambda: self.ec['controls'].generate(self))
    '''
    def buttons(me,self):
        #self.ew['obj'].encrypt_file.clicked.connect(lambda: self.ew['controls'].encrypt_file(self))
        #self.dw['obj'].decrypt_file.clicked.connect(lambda: self.dw['controls'].decrypt_file(self))
    '''
