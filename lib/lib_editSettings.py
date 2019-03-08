#! /usr/bin/python3

from PyQt5 import QtWidgets,QtCore
import os,sys,time,json

class controls:
    def __init__(me,self):
        me.buttons(self)
        #for a button to be useful/useable register in me.useable as below
        me.useableButtons={
                'close':lambda x: self.es['dialog'].close(),
            'save':me.save,
            'clear':me.clear,
            'reset':me.reset,
            'browse_ssh_dir':me.saveSetting,
            'browse_default_ofile_dir':me.saveSetting,
            'browse_app_icon':me.saveSetting,
                }

    def saveSetting(me,self):
        obj=self.sender()
        name=obj.objectName()
        prefix='browse_'
        if name.startswith(prefix) and len(name) > len(prefix):
            lineEdit=name[len(prefix):]
        print(obj,name,lineEdit)

    def clear(me,self):
        pass

    def reset(me,self):
        pass

    def save(me,self):
        pass

    def button_callback(me,self):
        button=self.sender()
        name=button.objectName()
        if name in me.useableButtons.keys():
            me.useableButtons[name](self)

    def buttons(me,self):
        local=self.es['dialog']
        for b in local.findChildren(QtWidgets.QPushButton,QtCore.QRegularExpression('.'),QtCore.Qt.FindChildrenRecursively):
            b.clicked.connect(lambda: me.button_callback(self))
