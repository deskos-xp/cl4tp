#! /usr/bin/python3

from PyQt5 import QtWidgets,QtCore,QtGui
import os,json,sys
import encryptWithKey as ewk
from Crypto.Hash import SHA512
import engineering_notation as en
#import logging
#logging.basicConfig(filename='ewk-errors.log',level=logging.ERROR)

class controls:
    def __init__(me,self):
        me.valueChanged(self)
        me.buttons(self)
        self.timed_actions(self.ew)
    
    def generate_hash_log(self,tab,ifile,ofile,key_list,progress_callback=None,chunksize=2048,hash_log=None):
        if hash_log == None:
            hash_log=os.path.join(
                    os.path.dirname(ofile),
                    os.path.basename(ifile)+'.hash'
                    )
        size=os.path.getsize(ofile)
        counter=0
        
        hashes={}
        files={'key_list':key_list,'efile':ofile}
        
        for key in files.keys():
            hsh=SHA512.new()
            if progress_callback != None:
                p=progress_callback(tab)
                p[0].setValue(0)
                p[0].setFormat('%p%')
                p[1]().showMessage('{} -> {}'.format(
                    os.path.basename(files[key]),
                    os.path.basename(hash_log)
                    )
                    )

            with open(files[key],'rb') as of:
                while True:
                    data=of.read(chunksize)
                    if not data:
                        break
                    counter+=len(data)
                    if progress_callback != None:
                        p[0].setFormat('Creating Hash Log - {}/{} - %p%'.format(
                            en.EngNumber(counter,2),
                            en.EngNumber(size,2)
                            )
                            )
                        p[0].setValue(int((counter/size)*100))
                    hsh.update(data)
            hashes[key]={}
            hashes[key]['digest']=hsh.hexdigest()
            hashes[key]['file']=files[key]
            p[0].setValue(0)
            p[0].setFormat('%p%')
        with open(hash_log,'w') as log:
            json.dump(hashes,log)
        if progress_callback != None:
            p[1]().showMessage('')

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
            try:
                ecr.encryptFile(
                        ifile=ld['ifile'],
                        ofile=ld['ofile'],
                        masterKeyPub=ld['public_key'],
                        key_list=ld['key_list'],
                        chunksize=ld['dataChunkSize'],
                        progress_callback=self.progress_crypt,
                        tab=tab
                        )
            except Exception as e:
                    print(e)
                    self.statusBar().showMessage('could not {} file, see log: {}'.format(tab['settings']['mode'],e))
                    self.logger.error('{} | {}'.format(e,json.dumps(tab['settings'])))

            if tab['obj'].useHashes.isChecked() == True:    
                me.generate_hash_log(
                    tab=tab,
                    ifile=ld['ifile'],
                    ofile=ld['ofile'],
                    key_list=ld['key_list'],
                    progress_callback=self.progress_crypt,
                    chunksize=ld['dataChunkSize'],
                    hash_log=ld['hash_log']
                    )
            self.tabDisable(self.ew,True)
            
        else:
            self.tabDisable(self.ew,True)
            self.statusBar().showMessage('Bad Fields: Check your paths!')
        tab['obj'].progressBar.setValue(0)
        tab['obj'].progressBar.setFormat('%p%')
        tab['running']=False


    def enable_hashLog(me,self):
        ew=self.ew['obj']
        state=ew.useHashes.isChecked()
        ew.browse_hash_log.setEnabled(state)
        ew.hash_log.setEnabled(state)

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
                hash_log=''
                if val != '':
                    val=os.path.join(self.config['default-ofile-dir'],os.path.basename(val))
                    ofile=val+'.ebin'
                    key_list=val+'.ejk'
                    hash_log=val+'.hash'
                else:
                    ofile=''
                    key_list=''
                for k,v in [['ofile',ofile],['key_list',key_list],['hash_log',hash_log]]:
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
        self.ew['obj'].browse_hash_log.clicked.connect(lambda: me.saveSetting(self,'hash_log',self.fmanager('hash_log',self.ew),setField=True))

    def valueChanged(me,self):
        local=self.ew['obj']
        local.ifile.textChanged.connect(lambda: me.saveSetting(self,'ifile',local.ifile.text()))
        local.ofile.textChanged.connect(lambda: me.saveSetting(self,'ofile',local.ofile.text()))
        local.public_key.textChanged.connect(lambda: me.saveSetting(self,'public_key',local.public_key.text()))
        local.key_list.textChanged.connect(lambda: me.saveSetting(self,'key_list',local.key_list.text()))
        local.hash_log.textChanged.connect(lambda: me.saveSetting(self,'hash_log',local.hash_log.text()))
        local.dataChunkSize.valueChanged.connect(lambda: me.saveSetting(self,'dataChunkSize',local.dataChunkSize.value()))
        local.useHashes.toggled.connect(lambda: me.enable_hashLog(self))

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
        local.hash_log.setText(settings['hash_log'])

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

