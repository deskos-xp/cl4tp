from PyQt5 import QtWidgets,QtCore,QtGui
import json,os,sys,time
import engineering_notation as en

class tabdefaults_controls:
    def __init__(me,self):
        me.buttons(self)

    def buttons(me,self):
        self.td['obj'].close.clicked.connect(lambda: me.close(self))

    def close(me,self):
        self.td['dialog'].hide()
