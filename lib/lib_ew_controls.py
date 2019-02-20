#! /usr/bin/python3

from PyQt5 import QtWidgets,QtCore,QtGui
import os,json,sys
import encryptWithKey as ewk

class controls:
    def __init__(me,self):
        me.valueChanged(self)
        me.buttons(self)
        self.timed_actions(self.ew)

    reset_called=False
    def encrypt_file(me,self,tab):
        tab['running']=True
        self.statusBar().showMessage('')
        self.tabDisable(self.ew,False)
        ready=self.preCheck(tab)
        if ready == True:
            #print(tab['settings'])
            ld=tab['settings']
            if ld['key_list'] == '':
                ld['key_list']=None
            ecr=ewk.druugianNightmare()
            tab['obj'].progressBar.setValue(0)
            tab['obj'].progressBar.setFormat('%p%')
            ecr.encryptFile(
                    ifile=ld['ifile'],
                    ofile=ld['ofile'],
                    masterKeyPub=ld['public_key'],
                    key_list=ld['key_list'],
                    chunksize=ld['dataChunkSize'],
                    progress_callback=self.progress_crypt,
                    tab=tab
                    )
            self.tabDisable(self.ew,True)
        else:
            self.tabDisable(self.ew,True)
            self.statusBar().showMessage('Bad Fields: Check your paths!')
        tab['running']=False

    def saveSetting(me,self,key,val,setField=False):
        self.ew['settings'][key]=val
        if setField == True:
            local=self.ew['dialog']
            field=local.findChildren(QtWidgets.QLineEdit,key,QtCore.Qt.FindChildrenRecursively)
            if field != None:
                field[0].setText(val)
        if key == 'ifile':
            if me.reset_called == False:
                self.missingKeyUpdate(ud_field=True,tab=self.ew)
                local=self.ew['dialog']
                if val != '':
                    ofile=val+'.ebin'
                    key_list=val+'.ejk'
                    #hash_log=val+'.hash'
                else:
                    ofile=''
                    key_list=''
                for k,v in [['ofile',ofile],['key_list',key_list]]:
                    field=local.findChildren(QtWidgets.QLineEdit,k,QtCore.Qt.FindChildrenRecursively)
                    field[0].setText(v)
            else:
                me.reset_called=False

    def buttons(me,self):
        self.ew['obj'].encrypt_file.clicked.connect(lambda: self.ew['controls'].encrypt_file(self,self.ew))
        self.ew['obj'].reset.clicked.connect(lambda: self.ew['controls'].reset_fields(self))
        self.ew['obj'].browse_ifile.clicked.connect(lambda: me.saveSetting(self,'ifile',self.fmanager('ifile',self.ew),setField=True))
        self.ew['obj'].browse_ofile.clicked.connect(lambda: me.saveSetting(self,'ofile',self.fmanager('ofile',self.ew),setField=True))
        self.ew['obj'].browse_keylist.clicked.connect(lambda: me.saveSetting(self,'key_list',self.fmanager('key_list',self.ew),setField=True))
        self.ew['obj'].browse_public_key.clicked.connect(lambda: me.saveSetting(self,'public_key',self.fmanager('public_key',self.ew),setField=True))

    def valueChanged(me,self):
        local=self.ew['obj']
        local.ifile.textChanged.connect(lambda: me.saveSetting(self,'ifile',local.ifile.text()))
        local.ofile.textChanged.connect(lambda: me.saveSetting(self,'ofile',local.ofile.text()))
        local.public_key.textChanged.connect(lambda: me.saveSetting(self,'public_key',local.public_key.text()))
        local.key_list.textChanged.connect(lambda: me.saveSetting(self,'key_list',local.key_list.text()))
        local.dataChunkSize.valueChanged.connect(lambda: me.saveSetting(self,'dataChunkSize',local.dataChunkSize.value()))

    def reset_fields(me,self):
        me.reset_called=True
        me.clear_settings(self)
        me.clear_fields(self)
        self.ew['obj'].progressBar.setValue(0)
        self.ew['obj'].progressBar.setFormat('%p%')

    def clear_fields(me,self):
        local=self.ew['obj']
        settings=self.ew['settings']
        local.ifile.setText(settings['ifile'])
        local.ofile.setText(settings['ofile'])
        local.public_key.setText(settings['public_key'])
        local.key_list.setText(settings['key_list'])
        local.dataChunkSize.setValue(settings['dataChunkSize'])

    def clear_settings(me,self):
        if os.path.exists(self.field_defaults):
            if not os.path.isfile(self.field_defaults):
                exit('defaults config "{}" is not a file'.format(self.field_defaults))
            else:
                keys={}
                with open(self.field_defaults,'r') as DEF:
                    keys=json.load(DEF)
                self.ew['settings']=keys['encrypt']
        else:
            exit('missing "{}" defaults config file'.format(self.field_defaults))

