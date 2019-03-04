from PyQt5 import QtWidgets,QtCore,QtGui
import json,os,sys,time
import engineering_notation as en
from copy import copy
class tabdefaults_decrypt_controls:
    def __init__(me,self):
        me.settings={}
        me.loadDefaults(self)
        me.buttons(self)
        me.valueChanged(self)

    def loadDefaults(me,self):
        me.settings=copy(self.td['controls'].settings['decrypt'])

    def browser_button_actions(me,self):
        key=self.sender().objectName()
        if len(key) > len('browse_'):
            key=key[len('browse_'):]
        print(key)

    def buttons(me,self):
        local=self.td['tabs']['decrypt']
        types=(QtWidgets.QPushButton,)
        for t in types:
            look=local['dialog'].findChildren(t,QtCore.QRegularExpression('^browse_'),QtCore.Qt.FindChildrenRecursively)
            if look != None and type(look) == type(list()):
                for i in look:
                    if type(i) == type(QtWidgets.QPushButton()):
                        i.clicked.connect(lambda: me.browser_button_actions(self))

    def saveSetting(me,self):

        value=None
        key=self.sender().objectName()
        if type(self.sender()) == type(QtWidgets.QLineEdit()):
            value=self.sender().text()
        me.settings[key]=value

    def valueChanged(me,self):
        local=self.td['tabs']['decrypt']
        types=(QtWidgets.QLineEdit,)
        for t in types:
            look=local['dialog'].findChildren(t,QtCore.QRegularExpression('.'),QtCore.Qt.FindChildrenRecursively)
            if look != None and type(look) == type(list()):
                for i in look:
                    if type(i) == type(QtWidgets.QLineEdit()):
                        i.textChanged.connect(lambda: me.saveSetting(self))
