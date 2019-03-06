#! /usr/bin/python3

from PyQt5 import QtWidgets,QtCore,QtGui
import os,json
import encryptWithKey as ewk
from Crypto.Hash import SHA512
import engineering_notation as en
#import logging
#logging.basicConfig(filename='ewk-errors.log',format="%(asctime)s %(message)s",dateformat='%m/%d/%Y %H:%M:%S',level=logging.ERROR)

class controls:
    failHL=[False,0]
    def __init__(me,self):
        me.valueChanged(self)
        me.buttons(self)
        self.timed_actions(self.dw)
        me.reset_fields(self)

    def decrypt_file(me,self,tab):
        tab['running']=True
        #print(tab['settings'])
        self.statusBar().showMessage('')
        self.tabDisable(self.dw,False)
        ready=self.preCheck(tab)
        if ready == True:
            skip=False
            ld=tab['settings']
            if ld['key_list'] == '':
                ld['key_list']=None
            if ld['password'] == '':
                ld['password']=None

            if tab['obj'].checkHashes.isChecked() == True:
                hsh=me.gen_hashes(
                        ifile=ld['ifile'],
                        key_list=ld['key_list'],
                        tab=tab,
                        progress_callback=self.progress_crypt,
                        chunksize=100000
                        )
                hashlog={}
                with open(ld['hash_log'],'r') as log:
                    hashlog=json.load(log)
                keys=['key_list','efile']
                err=False
                msg=''
            
                for i in keys:
                    if hsh[i]['file'] != hashlog[i]['file']:
                        msg='the hash log file name content does not match the generated hash sum: {} | '.format(hsh[i]['file'],hashlog[i]['file'])
                        err=True
                    if hsh[i]['digest'] != hashlog[i]['digest']:
                        msg="the hash sum in the log does not match the hash sum of the current file: {}".format(hsh[i]['file'])
                        err=True
                    print('generated:',hsh[i]['file'],hsh[i]['digest'])
                    print('read-from-log:',hashlog[i]['file'],hashlog[i]['digest'])
                if err == True:
                    msgBox=QtWidgets.QMessageBox(self)
                    msgBox.setText(msg)
                    msgBox.setInformativeText('Do you want to skip decryption?')
                    msgBox.setStandardButtons(QtWidgets.QMessageBox.No | QtWidgets.QMessageBox.Yes)
                    msgBox.setDefaultButton(QtWidgets.QMessageBox.Yes)
                    skip=msgBox.exec()
                    if skip == QtWidgets.QMessageBox.Yes:
                        skip=True
                    elif skip == QtWidgets.QMessageBox.No:
                        skip=False
                    #msgBox.show()
            ecr=ewk.druugianNightmare()
            tab['obj'].progressBar.setValue(0)
            tab['obj'].progressBar.setFormat('%p%')
        
            if skip == False:
                try:
                    ecr.decryptFile(
                            ifile=ld['ifile'],
                            ofile=ld['ofile'],
                            masterKeyPriv=ld['private_key'],
                            key_list=ld['key_list'],
                            password_to_masterKey=ld['password'],
                            progress_callback=self.progress_crypt,
                            tab=tab
                            )
                except Exception as e:
                    print(e)
                    self.statusBar().showMessage('could not {} file, see log: {}'.format(tab['settings']['mode'],e))
                    self.logger.error('{} | {}'.format(e,json.dumps(tab['settings'])))
            #self.tabDisable(self.dw,True)
            tab['obj'].progressBar.setValue(0)
            tab['obj'].progressBar.setFormat('%p%')
        else:
            self.statusBar().showMessage('Bad Fields: Check your paths.')
        tab['running']=False
        self.tabDisable(self.dw,True)
    #def buttons(me,self):
    #    self.dw['obj'].decrypt_file.clicked.connect(lambda: self.dw['controls'].decrypt_file(self))

    def saveSetting(me,self,key,val,setField=False):
        me.failHL=[False,0]
        self.dw['settings'][key]=val
        if setField == True:
            local=self.dw['dialog']
            field=local.findChildren(QtWidgets.QLineEdit,key,QtCore.Qt.FindChildrenRecursively)
            if field != None:
                field[0].setText(val)
            if key == 'ifile': 
                if val != '':
                    if os.path.splitext(val)[1] == '.ebin':
                        ofile=os.path.splitext(val)[0]
                    else:
                        ofile=val+'.bin'
                    key_list=os.path.splitext(val)[0]+'.ejk'
                    hash_log=os.path.splitext(val)[0]+'.hash'
                else:
                    ofile=''
                    key_list=''
                    hash_log=''
                for k,v in [['ofile',ofile],['key_list',key_list],['hash_log',hash_log]]:
                    field=local.findChildren(QtWidgets.QLineEdit,k,QtCore.Qt.FindChildrenRecursively)
                    field[0].setText(v)
        me.checkHashLog(self,self.dw,key,val)

    def checkHashLog(me,self,tab,key,val):
        if os.path.exists(self.expand_path(val)):
            if key in ['ifile','hash_log']:
                skipNext=False
                if tab['obj'].checkHashes.isChecked() == True:
                    try:
                        #need to force hash log to be incorrect for the following situations
                        keys={}
                        print(me.failHL)
                        if os.path.exists(tab['settings']['hash_log']):
                            with open(tab['settings']['hash_log'],'r') as log:
                                keys=json.load(log) 
                            if keys == {}:
                                skipNext=True
                                me.failHL[0]=True
                                me.failHL[1]+=1
                                msg='Hash Log is empty: Not using hash log! : '.format(tab['settings']['hash_log'])
                                me.displayError(self,msg)
                                if me.failHL[1] == 1:
                                    self.logger.error(msg)
                                #show messagebox if log is empty
                            #do a check to see if log contains proper structure
                            if skipNext == False:
                                structure=me.checkLogStructure(self,keys)
                                if structure == False:
                                    skipNext=True
                                    me.failHL[0]=True
                                    me.failHL[1]+=1
                                    #show messageBox if log is not properly structured
                                    msg='Invalid Hash Log Structure: Not using hash log! : {}'.format(tab['settings']['hash_log'])
                                    me.displayError(self,msg)
                                    if me.failHL[1] == 1:
                                        self.logger.error(msg)                
                            me.fail=[False,0]
                    except json.decoder.JSONDecodeError:
                        skipNext=True
                        me.failHL[0]=True
                        me.failHL[1]+=1
                        msg='Hash Log does not appear to be in the JSON format: Not using hash log! : {}'.format(tab['settings']['hash_log'])
                        me.displayError(self,msg)
                        if me.failHL[1] == 1:
                            self.logger.error(msg)
                    if me.failHL[0] == True:
                        tab['obj'].checkHashes.setChecked(False)
                        tab['obj'].hash_log.setText('')
                    else:
                        self.statusBar().showMessage('')

    def displayError(me,self,msg):
        print(me.failHL)
        if me.failHL == [True,1]:
            self.statusBar().showMessage(msg)
            mb=QtWidgets.QMessageBox(self)
            mb.setText(msg)
            mb.setIcon(QtWidgets.QMessageBox.Critical)
            mb.show()

    def checkLogStructure(me,self,logData):
        for keyRoot in logData.keys():
            if keyRoot in ['efile','key_list']:
                for keyRootSub_0 in logData[keyRoot].keys():
                    if keyRootSub_0 not in ['file','digest']:
                        return False
            else:
                return False
        return True

    def buttons(me,self):
        self.dw['obj'].decrypt_file.clicked.connect(lambda: self.dw['controls'].decrypt_file(self,self.dw))
        self.dw['obj'].reset.clicked.connect(lambda: self.dw['controls'].reset_fields(self))
        self.dw['obj'].browse_ifile.clicked.connect(lambda: me.saveSetting(self,'ifile',self.fmanager('ifile',self.dw),setField=True))
        self.dw['obj'].browse_ofile.clicked.connect(lambda: me.saveSetting(self,'ofile',self.fmanager('ofile',self.dw),setField=True))
        self.dw['obj'].browse_key_list.clicked.connect(lambda: me.saveSetting(self,'key_list',self.fmanager('key_list',self.dw),setField=True))
        self.dw['obj'].browse_private_Key.clicked.connect(lambda: me.saveSetting(self,'private_key',self.fmanager('private_key',self.dw),setField=True))
        self.dw['obj'].browse_hashlog.clicked.connect(lambda: me.saveSetting(self,'hash_log',self.fmanager('hash_log',self.dw),setField=True))
        self.dw['obj'].checkHashes.setChecked(self.config['useHashLog_on_Start'])

    def enable_hashLog(me,self):
        dw=self.dw['obj']
        state=dw.checkHashes.isChecked()
        dw.browse_hashlog.setEnabled(state)
        dw.hash_log.setEnabled(state)
        me.checkHashLog(self,self.dw,'hash_log',dw.hash_log.text())

    def valueChanged(me,self):
        local=self.dw['obj']
        local.ifile.textChanged.connect(lambda: me.saveSetting(self,'ifile',local.ifile.text(),setField=True))
        local.ofile.textChanged.connect(lambda: me.saveSetting(self,'ofile',local.ofile.text()))
        local.private_key.textChanged.connect(lambda: me.saveSetting(self,'private_key',local.private_key.text()))
        local.key_list.textChanged.connect(lambda: me.saveSetting(self,'key_list',local.key_list.text()))
        local.password.textChanged.connect(lambda: me.saveSetting(self,'password',local.password.text()))
        local.checkHashes.toggled.connect(lambda: me.enable_hashLog(self))
        local.hash_log.textChanged.connect(lambda: me.saveSetting(self,'hash_log',local.hash_log.text()))

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
   
    '''
    def gen_hashes(self,ifile,key_list,tab,progress_callback=None,chunksize=2048):
        hashes={}
        files={'key_list':key_list,'efile':ifile}
        hsh={} 
        for key in files.keys():
            counter=0
            hsh[key]=SHA512.new()
            if progress_callback != None:
                p=progress_callback(tab)
                p[0].setValue(0)
                p[0].setFormat('%p%')
                
            size=os.path.getsize(files[key])
            with open(files[key],'rb') as of:
                while True:
                    data=of.read(chunksize)
                    if not data:
                        break
                    counter+=len(data)
                    hsh[key].update(data)
                    if progress_callback != None:
                        p[0].setFormat('Creating Hash Log - {}/{} - %p%'.format(
                            en.EngNumber(counter,2),
                            en.EngNumber(size,2)
                            )
                            )
                        p[0].setValue(int((counter/size)*100))
            hashes[key]={}
            hashes[key]['digest']=hsh[key].hexdigest()
            hashes[key]['file']=files[key]
            p[0].setValue(0)
            p[0].setFormat('%p%')
            p[1]().showMessage('')
            print(hashes)
        return hashes
    '''
    #'''
    def gen_hashes(self,ifile,key_list,tab,progress_callback=None,chunksize=2048):
        files={'key_list':key_list,'efile':ifile}
        hashes={}
        if progress_callback != None:
            p=progress_callback(tab=tab)

        for key in files.keys():
            hsh=SHA512.new()
            size=os.path.getsize(files[key])
            counter=0
            p[1]().showMessage('Generating Hash-Sum for {}.'.format(files[key]))
            print(key,files[key])
            with open(files[key],'rb') as f:
                while True:
                    data=f.read(chunksize)
                    if not data:
                        break
                    hsh.update(data)
                    prog=int((counter/size)*100)
                    print(prog,files[key])
                    if progress_callback != None:
                        p[0].setFormat('Hashing {} - {}/{} - %p%'.format(
                            key,
                            en.EngNumber(counter,2),
                            en.EngNumber(size,2)
                            ))
                        p[0].setValue(prog)
                    counter+=len(data)
                hashes[key]={}
                hashes[key]['file']=files[key]
                hashes[key]['digest']=hsh.hexdigest()
                hsh=None
            p[0].setValue(0)
            p[0].setFormat('%p%')
        p[1]().showMessage('')
        return hashes
    #'''

