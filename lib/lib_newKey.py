#! /usr/bin/env python3
from PyQt5 import QtWidgets,QtCore,QtGui
import engineering_notation as ne
from Crypto.PublicKey import RSA
import json,os,sys
import copy,time
#self refers to the class in lib_ewk_gui.py
#me.* refers to the local class
#this allows for more namespace flexibility

class controls:
    public_was_focused_once=False
    textChanged=False
    done=True
    def __init__(me,self):
        me.load_defaults(self)
        me.buttons(self)
        me.valueChanged(self)
        me.timed(self)

    def load_defaults(me,self):
        #disk io is slow, load only once, or only as necessary
        if os.path.exists(self.newKey_defaults):
            with open(self.newKey_defaults,'r') as conf:
                self.nk['settings']=json.load(conf)
            self.nk['defaults']=copy.copy(self.nk['settings'])

    def clear_fields(me,self):
        nk=self.nk['obj']
        nk.size.setValue(self.nk['defaults']['size'])
        nk.private_key.setText(self.nk['defaults']['private_key'])
        nk.public_key.setText(self.nk['defaults']['public_key'])
        nk.password.setText(self.nk['defaults']['password'])
        nk.encrypted_private.setChecked(self.nk['defaults']['encrypted_private'])

    def buttons(me,self):
        nk=self.nk['obj']
        nk.close.clicked.connect(lambda: me.close_dialog(self,self.nk['dialog'],nk))
        nk.save.clicked.connect(lambda: me.save(self))
        nk.clear.clicked.connect(lambda: me.clear_fields(self)) 
        nk.browse_public_key.clicked.connect(lambda: me.saveSetting(self,self.nk,'public_key',self.fmanager('public_key_save',tab=None),setField=True))
        nk.browse_private_key.clicked.connect(lambda: me.saveSetting(self,self.nk,'private_key',self.fmanager('private_key_save',tab=None),setField=True))

    def valueChanged(me,self):
        nk=self.nk['obj']
        nk.size.valueChanged.connect(lambda: me.saveSetting(self,self.nk,'size',nk.size.value()))
        nk.private_key.textChanged.connect(lambda: me.saveSetting(self,self.nk,'private_key',nk.private_key.text()))
        nk.public_key.textChanged.connect(lambda: me.saveSetting(self,self.nk,'public_key',nk.public_key.text()))
        nk.encrypted_private.toggled.connect(lambda: me.saveSetting(self,self.nk,'encrypted_private',nk.encrypted_private.isChecked()))
        nk.password.textChanged.connect(lambda: me.saveSetting(self,self.nk,'password',nk.password.text()))

    def allow_clear(me,self):
        counter=0
        for k,t in [['password',QtWidgets.QLineEdit],['private_key',QtWidgets.QLineEdit],['public_key',QtWidgets.QLineEdit],['size',QtWidgets.QSpinBox],['encrypted_private',QtWidgets.QCheckBox]]:
            for edit in self.nk['dialog'].findChildren(t,k,QtCore.Qt.FindChildrenRecursively):
                if type(edit) == type(QtWidgets.QLineEdit()):
                    if edit.text() != self.nk['defaults'][edit.objectName()]:
                        counter+=1
                if type(edit) == type(QtWidgets.QSpinBox()):
                    if edit.value() != self.nk['defaults'][edit.objectName()]:
                        counter+=1
                if type(edit) == type(QtWidgets.QCheckBox()):
                    if edit.isChecked() != self.nk['defaults'][edit.objectName()]:
                        counter+=1
                        print(edit.isChecked(),self.nk['defaults'][edit.objectName()])
        if counter > 0 :
            state=True
        elif counter < 1:
            state=False
        me.enable_buttons(self,state,mode='clear')

    def ready(me,self):
        if self.nk['obj'].encrypted_private.isChecked() == True:
            counter=3
        else:
            counter=2
        for k,t in [['password',QtWidgets.QLineEdit],['private_key',QtWidgets.QLineEdit],['public_key',QtWidgets.QLineEdit],['encrypted_private',QtWidgets.QCheckBox]]:
            for edit in self.nk['dialog'].findChildren(t,k,QtCore.Qt.FindChildrenRecursively):
                if type(edit) == type(QtWidgets.QCheckBox()):
                    if edit.isChecked() != self.nk['defaults'][edit.objectName()]:
                        if self.nk['obj'].password.text() != self.nk['defaults']['password']:
                            counter-=1
                            print(edit.isChecked(),self.nk['defaults'][edit.objectName()])
                else:
                    if type(edit) == type(QtWidgets.QLineEdit()):
                        if edit.text() != self.nk['defaults'][edit.objectName()]:
                            counter-=1
        if counter < 1:
            state=True
        else:
            state=False
        me.enable_buttons(self,state,mode='save')

    def enable_buttons(me,self,state,mode='clear'):
        if mode == 'clear':
            self.nk['obj'].clear.setEnabled(state)
        if mode == 'save':
            self.nk['obj'].save.setEnabled(state)

    def genKey(me,self,obj):
        tmp=RSA.generate(obj['size'])
        if obj['encrypted_private'] == True:
            obj['gen_private']=tmp.export_key('PEM',passphrase=obj['password'])
            obj['gen_public']=tmp.publickey().export_key()
        else:
            obj['gen_private']=tmp.export_key('PEM')
            obj['gen_public']=tmp.publickey().export_key()

        if os.path.exists(self.nk['settings']['private_key']):
            self.logger.error('private key file "{}" exists'.format(self.nk['settings']['private_key']))

        if os.path.exists(self.nk['settings']['public_key']):
            self.logger.error('public key file "{}" exists'.format(self.nk['settings']['public_key']))

    def saveSetting(me,self,nk,key,val,setField=False):
        me.done=False
        ext='.key'
        me.allow_clear(self)
        me.ready(self)
        self.nk['settings'][key]=val
        if key == 'encrypted_private':
            self.nk['obj'].password.setEnabled(val)
        if setField == True:
            local=self.nk['dialog'].children()
            for obj in local:
                if obj.objectName() == key:
                    if type(obj) == type(QtWidgets.QLineEdit()):
                        if obj.objectName() == 'private_key':
                            if val != '':
                                if self.nk['obj'].public_key.text() == '':
                                    if os.path.splitext(val)[1] == ext:
                                        pval=os.path.splitext(val)[0]
                                    else:
                                        pval=val
                                    self.nk['obj'].public_key.setText(pval+'.pub'+ext)
                                if os.path.splitext(val)[1] != ext:
                                    val+='.key'
                        obj.setText(val)
                    if type(obj) == type(QtWidgets.QSpinBox()):
                        obj.setValue(val)
                    if type(obj) == type(QtWidgets.QCheckBox()):
                        obj.setChecked(val)
        me.textChanged=True
        me.done=True

    def timed(me,self):
        self.nk['timer']=QtCore.QTimer()
        self.nk['timer'].timeout.connect(lambda: me.timer_actions(self))
        self.nk['timer'].start(100)

    def editActor(me,lineEdit,ext,focused):
        if focused !=  None:
            if focused.objectName() != lineEdit.objectName():
                if os.path.splitext(lineEdit.text())[1] != ext and lineEdit.text() != '':
                    if os.path.splitext(os.path.split(lineEdit.text())[1])[0].lower() not in ['','.key']:
                        if os.path.splitext(lineEdit.text())[1] == '':
                            lineEdit.setText(os.path.splitext(lineEdit.text())[0]+ext)
                    else:
                        lineEdit.setText('')

    def timer_actions(me,self):
        #dont force extension,God Dammit!
        pass
        '''
        focused=QtWidgets.QApplication.focusWidget()
        lo=self.nk['obj']
        ext='.key'
        me.editActor(lo.private_key,ext,focused)
        me.editActor(lo.public_key,ext,focused)
        if lo.public_key.text() == lo.private_key.text():
            if ( lo.public_key.text() != '' ) and ( lo.private_key.text() != '' ):
                lo.public_key.setText(
                        os.path.splitext(
                            lo.public_key.text()
                            )[0].upper()+ext
                )
        if me.public_was_focused_once == False:
            #lo.public_key.setText(os.path.splitext(lo.private_key.text())[0].upper()+ext)
            if lo.public_key.text() == '' and lo.private_key.text() != '':
                lo.public_key.setText(os.path.splitext(lo.private_key.text())[0].upper()+ext)

        if lo.public_key.text() == '':
            me.public_was_focused_once=False
        if lo.public_key.text() == '.key':
            lo.public_key.setText('')

        if focused != None:
            if focused.objectName() == 'private_key':
                if len(focused.text()) >= len(ext) and me.textChanged == True:
                    focused.setCursorPosition(len(lo.private_key.text())-len(ext)) 
            if focused.objectName() == 'public_key':
                me.public_was_focused_once=True
                if len(focused.text()) >= len(ext) and me.textChanged == True:
                    focused.setCursorPosition(len(lo.public_key.text())-len(ext))

        if time.localtime().tm_sec % 60 == 0:
            if me.done == True:
                me.textChanged=False
                    
        #if os.path.splitext(lo.public_key.text())[1] != ext and lo.public_key.text() != '':
        #    lo.public_key.setText(lo.public_key.text()+ext)
        '''

    def close_dialog(me,self,dialog,obj):
        #me.reset_fields(self,obj)
        dialog.hide()

    def save(me,self):
        me.genKey(self,self.nk['settings'])
        print(self.nk['settings'])
