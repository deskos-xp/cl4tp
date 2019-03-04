from PyQt5 import QtWidgets,QtCore,QtGui
import json,os,sys,time
import engineering_notation as en

class tabdefaults_controls:
    def __init__(me,self):
        me.settings={}
        me.loadDefaults(self)
        me.buttons(self)

    def buttons(me,self):
        self.td['obj'].close.clicked.connect(lambda: me.close(self))
        self.td['obj'].save.clicked.connect(lambda: me.save(self))

    def close(me,self):
        self.td['dialog'].hide()

    def loadDefaults(me,self):
        with open(self.field_defaults,'r') as cnf:
            me.settings=json.load(cnf)

    def save(me,self):
        me.settings['encrypt']=self.td['tabs']['encrypt']['controls'].settings
        me.settings['decrypt']=self.td['tabs']['decrypt']['controls'].settings
        print(me.settings)
