from PyQt5 import QtWidgets,QtCore,QtGui
import json,os,sys,time
import engineering_notation as en
from copy import copy

class tabdefaults_encrypt_controls:
    def __init__(me,self):
        me.loadDefaults(self)
        me.valueChanged(self)
        me.setLabelSpecial(self)
        me.buttons(self)

    def loadDefaults(me,self):
        self.td['tabs']['encrypt']['settings']=copy(self.td['settings']['encrypt'])

    def setLabelSpecial(me,self):
        self.td['tabs']['encrypt']['obj'].sizeInEN.setText("EN: {}".format(en.EngNumber(self.td['tabs']['encrypt']['obj'].dataChunkSize.value(),0)))

    def browser_button_actions(me,self):
        key=self.sender().objectName()
        if len(key) > len('browse_'):
            key=key[len('browse_'):]
        print(key)
        virt_fd=self.fmanager(key,self.td['tabs']['encrypt'])
        textbox=self.td['tabs']['encrypt']['dialog'].findChildren(QtWidgets.QLineEdit,key,QtCore.Qt.FindChildrenRecursively)
        if textbox != None and type(textbox) == type(list()):
            for i in textbox:
                if type(i) == type(QtWidgets.QLineEdit()):
                    i.setText(virt_fd)
        

    def buttons(me,self):
        local=self.td['tabs']['encrypt']
        types=(QtWidgets.QPushButton,)
        for t in types:
            look=local['dialog'].findChildren(t,QtCore.QRegularExpression('^browse_'),QtCore.Qt.FindChildrenRecursively)
            if look != None and type(look) == type(list()):
                for i in look:
                    if type(i) == type(QtWidgets.QPushButton()):
                        i.clicked.connect(lambda: me.browser_button_actions(self))
    
    def saveSetting(me,self):
         key=self.sender().objectName()
         if type(self.sender()) == type(QtWidgets.QLineEdit()):
             value=self.sender().text()
         elif type(self.sender()) == type(QtWidgets.QSpinBox()):
             value=self.sender().value()
             if key == 'dataChunkSize':
                 me.setLabelSpecial(self)
         self.td['tabs']['encrypt']['settings'][key]=value
         print(value,key)

    def valueChanged(me,self):
        local=self.td['tabs']['encrypt']
        types=(
                QtWidgets.QLineEdit,
                QtWidgets.QSpinBox,
                )
        for t in types:
            look=local['dialog'].findChildren(t,QtCore.QRegularExpression('.'),QtCore.Qt.FindChildrenRecursively)
            if look != None and type(look) == type(list()):
                for i in look:
                    if t == type(QtWidgets.QLineEdit()):
                        i.textChanged.connect(lambda: me.saveSetting(self))
                    elif t == type(QtWidgets.QSpinBox()):
                        i.valueChanged.connect(lambda: me.saveSetting(self)) 
