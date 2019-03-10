#! /usr/bin/python3

from PyQt5 import QtWidgets,QtCore
import os,sys,time,json

class controls:
    def __init__(me,self):
        #for a button to be useful/useable register in me.useable as below
        me.useableButtons={
                'close':me.close,
            'save':me.save, 
            'reset':me.reset,
            'browse_ssh_dir':me.saveSetting,
            'browse_default_ofile_dir':me.saveSetting,
            'browse_app_icon':me.saveSetting,
            'useHashLog_on_Start':me.saveSetting,
            'ssh_dir':me.saveSetting,
            'default_ofile_dir':me.saveSetting,
            'encrypt_filter_ofile':me.saveSetting,
            'decrypt_filter_ofile':me.saveSetting,
            'encrypt_filter_ifile':me.saveSetting,
            'decrypt_filter_ifile':me.saveSetting,
            'filter_public_key':me.saveSetting,
            'filter_private_key':me.saveSetting,
            'filter_key_list':me.saveSetting,
            'filter_hash_log':me.saveSetting,
            'app_icon':me.saveSetting,
            'default_start_tab':me.saveSetting,
                }
        me.buttons(self)
        me.valueChanged(self)
        me.loadSettings(self)

    def close(me,self):
        self.statusBar().showMessage('')
        self.es['dialog'].close()

    def loadSettings(me,self):
        local=self.es['dialog']
        save=self.es['settings']
        types=(QtWidgets.QLineEdit,QtWidgets.QComboBox,QtWidgets.QCheckBox)
        for t in types:
            widgets=local.findChildren(t,QtCore.QRegularExpression('.'),QtCore.Qt.FindChildrenRecursively)
            if widgets != None:
                for widget in widgets:
                    nameSave=widget.objectName().replace('_','-')
                    if type(widget) == type(QtWidgets.QLineEdit()):
                        widget.setText(save[nameSave])
                    if type(widget) == type(QtWidgets.QCheckBox()):
                        widget.setChecked(save[nameSave])
                    if type(widget) == type(QtWidgets.QComboBox()):
                        text=save[nameSave][0].upper()+save[nameSave][1:]
                        widget.setCurrentIndex(widget.findText(text,QtCore.Qt.MatchExactly))

    def getState(me,self,obj,_class):
        if _class == QtWidgets.QLineEdit:
            return obj.text()
        elif _class == QtWidgets.QCheckBox:
            return obj.isChecked() 
        elif _class == QtWidgets.QComboBox:
            return obj.currentText().lower()

    def saveSetting(me,self):
        save=self.es['settings']
        obj=self.sender()
        name=obj.objectName()
        prefix='browse-'
        name=name.replace('_','-')
        lineEdit_data=None
        data=None
        if type(obj) == type(QtWidgets.QPushButton()):
            if name.startswith(prefix) and len(name) > len(prefix):
                lineEdit=name[len(prefix):].replace('-','_')
                lineEdit_data=self.es['dialog'].findChildren(QtWidgets.QLineEdit,lineEdit,QtCore.Qt.FindChildrenRecursively)
                if lineEdit_data != None:
                    for i in lineEdit_data:
                        #print(i.objectName())
                        if 'dir' in i.objectName():
                            data=self.fmanager('dir-select',self.es)
                        if 'icon' in i.objectName():
                            data=self.fmanager('icon-select',self.es)
                        i.setText(data)
                        #data=me.getState(self,i,QtWidgets.QLineEdit)
            save[lineEdit]=data
            #print(obj,name,lineEdit,data)
        
        if type(obj) == type(QtWidgets.QCheckBox()):
            data=me.getState(self,obj,QtWidgets.QCheckBox)
            save[name]=data
            #print(obj,name,data)
        
        if type(obj) == type(QtWidgets.QLineEdit()):
            data=me.getState(self,obj,QtWidgets.QLineEdit)
            save[name]=data
            #print(obj,name,data)
        
        if type(obj) == type(QtWidgets.QComboBox()):
            data=me.getState(self,obj,QtWidgets.QComboBox)
            save[name]=data
            #print(obj,name,data)

    def reset(me,self):
        with open(os.path.join(self.conf_dir,'config_hardwire.json'),'r') as cnf:
            self.es['settings']=json.load(cnf)
        me.loadSettings(self)
        self.statusBar().showMessage('loaded hardwired defaults to reset fields!')

    def save(me,self):
        local=self.es['dialog']
        save=self.es['settings']
        types=(QtWidgets.QLineEdit,QtWidgets.QCheckBox,QtWidgets.QComboBox)
        for t in types:
            widgets=local.findChildren(t,QtCore.QRegularExpression('.'),QtCore.Qt.FindChildrenRecursively)
            if widgets != None:
                for widget in widgets:
                    if type(widget) == type(QtWidgets.QLineEdit()):
                        name=widget.objectName().replace('_','-')
                        save[name]=widget.text()
                    elif type(widget) == type(QtWidgets.QCheckBox()):
                        name=widget.objectName().replace('_','-')
                        save[name]=widget.isChecked()
                    elif type(widget) == type(QtWidgets.QComboBox()):
                        name=widget.objectName().replace('_','-')
                        save[name]=widget.currentText().lower()
        with open(self.config_file,'w') as cnf:
            json.dump(save,cnf)
        self.statusBar().showMessage('Save settings to file!')

    def change_callback(me,self):
        button=self.sender()
        name=button.objectName()
        if name in me.useableButtons.keys():
            me.useableButtons[name](self)

    def valueChanged(me,self):
        local=self.es['dialog']
        for c in local.findChildren(QtWidgets.QCheckBox,QtCore.QRegularExpression('.'),QtCore.Qt.FindChildrenRecursively):
            c.toggled.connect(lambda: me.change_callback(self))
        
        for l in local.findChildren(QtWidgets.QLineEdit,QtCore.QRegularExpression('.'),QtCore.Qt.FindChildrenRecursively):
            l.textChanged.connect(lambda: me.change_callback(self))
        
        for c in local.findChildren(QtWidgets.QComboBox,QtCore.QRegularExpression('.'),QtCore.Qt.FindChildrenRecursively):
            c.currentIndexChanged.connect(lambda: me.change_callback(self))

    def buttons(me,self):
        local=self.es['dialog']
        for b in local.findChildren(QtWidgets.QPushButton,QtCore.QRegularExpression('.'),QtCore.Qt.FindChildrenRecursively):
            b.clicked.connect(lambda: me.change_callback(self))
