#! /usr/bin/python3

from PyQt5 import QtWidgets,QtCore,QtGui
import os,json
import encryptWithKey as ewk
class controls:
    def __init__(me,self):
        me.valueChanged(self)
        me.buttons(self)
        self.timed_actions(self.dw)

    def decrypt_file(me,self,tab):
        print(tab['settings'])
        ld=tab['settings']
        if ld['key_list'] == '':
            ld['key_list']=None
        if ld['password'] == '':
            ld['password']=None

        ecr=ewk.druugianNightmare()
        tab['obj'].progressBar.setValue(0)
        tab['obj'].progressBar.setFormat('%p%')
        self.tabDisable(self.dw,False)
        ecr.decryptFile(
                ifile=ld['ifile'],
                ofile=ld['ofile'],
                masterKeyPriv=ld['private_key'],
                key_list=ld['key_list'],
                password_to_masterKey=ld['password'],
                progress_callback=self.progress_crypt,
                tab=tab
                )
        self.tabDisable(self.dw,True)

    def buttons(me,self):
        self.dw['obj'].decrypt_file.clicked.connect(lambda: self.dw['controls'].decrypt_file(self))

    def saveSetting(me,self,key,val,setField=False):
        self.dw['settings'][key]=val
        if setField == True:
            local=self.dw['dialog']
            field=local.findChildren(QtWidgets.QLineEdit,key,QtCore.Qt.FindChildrenRecursively)
            if field != None:
                field[0].setText(val)

    def buttons(me,self):
        self.dw['obj'].decrypt_file.clicked.connect(lambda: self.dw['controls'].decrypt_file(self,self.dw))
        self.dw['obj'].reset.clicked.connect(lambda: self.dw['controls'].reset_fields(self))
        self.dw['obj'].browse_ifile.clicked.connect(lambda: me.saveSetting(self,'ifile',self.fmanager('ifile',self.dw),setField=True))
        self.dw['obj'].browse_ofile.clicked.connect(lambda: me.saveSetting(self,'ofile',self.fmanager('ofile',self.dw),setField=True))
        self.dw['obj'].browse_key_list.clicked.connect(lambda: me.saveSetting(self,'key_list',self.fmanager('key_list',self.dw),setField=True))
        self.dw['obj'].browse_private_Key.clicked.connect(lambda: me.saveSetting(self,'private_key',self.fmanager('private_key',self.dw),setField=True))


    def valueChanged(me,self):
        local=self.dw['obj']
        local.ifile.textChanged.connect(lambda: me.saveSetting(self,'ifile',local.ifile.text()))
        local.ofile.textChanged.connect(lambda: me.saveSetting(self,'ofile',local.ofile.text()))
        local.private_key.textChanged.connect(lambda: me.saveSetting(self,'private_key',local.private_key.text()))
        local.key_list.textChanged.connect(lambda: me.saveSetting(self,'key_list',local.key_list.text()))
        local.password.textChanged.connect(lambda: me.saveSetting(self,'password',local.password.text()))

    def reset_fields(me,self):
        me.clear_settings(self)
        me.clear_fields(self)
        self.dw['obj'].progressBar.setValue(0)
        self.dw['obj'].progressBar.setFormat('%p%')

    def clear_fields(me,self):
        local=self.dw['obj']
        settings=self.dw['settings']
        local.ifile.setText(settings['ifile'])
        local.ofile.setText(settings['ofile'])
        local.private_key.setText(settings['private_key'])
        local.key_list.setText(settings['key_list'])
        local.password.setText(settings['password'])

    def clear_settings(me,self):
        if os.path.exists(self.field_defaults):
            if not os.path.isfile(self.field_defaults):
                exit('defaults config "{}" is not a file'.format(self.field_defaults))
            else:
                keys={}
                with open(self.field_defaults,'r') as DEF:
                    keys=json.load(DEF)
                self.dw['settings']=keys['decrypt']
        else:
            exit('missing "{}" defaults config file'.format(self.field_defaults))

