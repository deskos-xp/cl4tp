#! /usr/bin/python3

from PyQt5 import QtWidgets,QtCore,QtGui
import os,sys
libdirs=('./lib','./lib_widget')
try:
    for d in libdirs:
        sys.path.append(d)
except Exception as e:
    exit('modules could not be imported: {}'.format(e))
import json,time
import lib_ewk_gui
import encryptWithKey
import libControl
import encrypt_widget,decrypt_widget
import lib_ew_controls,lib_dw_controls
import engineering_notation as en
import logging
logging.basicConfig(filename='ewk-errors.log',format="%(asctime)s %(message)s",datefmt='%m/%d/%Y %H:%M:%S',level=logging.ERROR)

class ewk_gui(QtWidgets.QMainWindow,lib_ewk_gui.Ui_ewk_gui):
    field_defaults='./defaults/default.json'
    config={
            'ssh-dir':'~/.ssh',
            'default-ofile-dir':'~/ekw-save',
            'decrypt-filter-ofile':'All Files (*)',
            'encrypt-filter-ofile':'Encrypted Binary (*.ebin);;All Files (*)',
            "decrypt-filter-ifile":"Encrypted Binary (*.ebin);;All Files (*)",
            "encrypt-filter-ifile":"All Files (*)",
            'filter-public-key':'Key File (*.key);;Public Key (*.pub);;All Files(*)',
            'filter-private-key':'Key File (*.key);;Private Key (*.priv);;All Files(*)',
            'filter-key-list':'Encrypted Json Key List (*.ejk);;All Files(*)',
            'filter-hash-log':'Hash Log (*.hash);;All Files (*)',
            }
    config_file='./defaults/config.json'
    ext='.ebin'
    keyExt='.ejk'
    logger=logging
    def expand_path(self,path):
        return os.path.expanduser(os.path.expandvars(path))

    def load_config(self):
        if os.path.exists(self.config_file):
            if os.path.isfile(self.config_file):
                with open(self.config_file,'r') as cnf:
                    self.config=json.load(cnf)
            else:
                print('{} : not a file... using hardcoded defaults'.format(self.config_file))
        else:
            print('{} : does not exist... using hardcoded defaults'.format(self.config_file))
        self.config['ssh-dir']=self.expand_path(self.config['ssh-dir'])
        self.config['default-ofile-dir']=self.expand_path(self.config['default-ofile-dir'])
        if not os.path.exists(self.config['default-ofile-dir']):
            os.mkdir(self.config['default-ofile-dir'])
        if os.path.exists(self.expand_path(self.config['app-icon'])):
            icon=QtGui.QIcon(self.expand_path(self.config['app-icon']))
            self.setWindowIcon(icon)

    def actors(self,tab):
        children=tab['dialog'].findChildren(QtWidgets.QLineEdit)
        count=0
        for child in children:
            skipNext=False
            if child.objectName() not in ['password','qt_spinbox_lineedit']:
                #print(tab['settings']['mode'],count)
                if child.objectName() == 'hash_log':
                    if tab['settings']['mode'] == 'decrypt':
                        if tab['obj'].checkHashes.isChecked() == True:
                            if child.text() in ['',None]:
                                count+=1
                    elif tab['settings']['mode'] == 'encrypt':
                        if tab['obj'].useHashes.isChecked() == True:
                            if child.text() in ['',None]:
                                count+=1
                elif child.text() in ['',None]:
                    count+=1
        if count > 0:
            self.setState(False,tab)
        else:
            self.setState(True,tab)

    def setState(self,state,tab):
        if tab['running'] == False:
            if tab['settings']['mode'] == 'encrypt':
                tab['obj'].encrypt_file.setEnabled(state)
            if tab['settings']['mode'] == 'decrypt':
                tab['obj'].decrypt_file.setEnabled(state)


    def timed_actions(self,tab):
        tab['timer']={}
        tab['timer']['0']=QtCore.QTimer(self)
        tab['timer']['0'].timeout.connect(lambda: self.actors(tab))
        tab['timer']['0'].start(10)


    def fmanager(self,mode,tab):
        if mode == 'hash_log':
            key='filter-hash-log'
            fd=''
            if tab['settings']['ofile'] != '':
                fd=tab['settings']['ofile']+'.hsh'

            if tab['settings']['mode'] == 'encrypt':
                file=QtWidgets.QFileDialog.getSaveFileName(
                        caption=mode,
                        directory=os.path.join(
                            self.config['default-ofile-dir'],
                            os.path.basename(fd)
                            ),
                        filter=self.config[key]
                        )
            if tab['settings']['mode'] == 'decrypt':
                file=QtWidgets.QFileDialog.getOpenFileName(
                        caption=mode,
                        directory=os.path.join(
                            self.config['default-ofile-dir'],
                            os.path.basename(fd)
                            ),
                        filter=self.config[key]
                        )
        if mode == 'ifile':
            if tab['settings']['mode'] == 'encrypt':
                key='encrypt-filter-ifile'
            if tab['settings']['mode'] == 'decrypt':
                key='decrypt-filter-ifile'
            file=QtWidgets.QFileDialog.getOpenFileName(caption=mode,directory=os.environ['HOME'],filter=self.config[key])
        if mode == 'ofile':
            if tab['settings']['mode'] == 'encrypt':
                key='encrypt-filter-ofile'
                fd=os.path.basename(tab['settings']['ifile'])+self.ext
            if tab['settings']['mode'] == 'decrypt':
                key='decrypt-filter-ofile'
                fd=os.path.basename(os.path.splitext(tab['settings']['ifile'])[0])

            file=QtWidgets.QFileDialog.getSaveFileName(
                    caption=mode,
                    directory=os.path.join(
                        self.config['default-ofile-dir'],
                        fd
                        ),
                    filter=self.config[key]
                    )
            print(file)
            if file[1] == 'Encrypted Binary (*.ebin)':
                if os.path.splitext(file[0])[1] != self.ext:
                    return file[0]+self.ext
        if mode == 'public_key':
            file=QtWidgets.QFileDialog.getOpenFileName(caption=mode,directory=self.config['ssh-dir'],filter=self.config['filter-public-key'])
        if mode == 'private_key':
            file=QtWidgets.QFileDialog.getOpenFileName(caption=mode,directory=self.config['ssh-dir'],filter=self.config['filter-private-key'])
        if mode == 'key_list':
            if tab['settings']['mode'] == 'decrypt':
                file=QtWidgets.QFileDialog.getOpenFileName(caption=mode,directory=self.config['default-ofile-dir'],filter=self.config['filter-key-list'])
            elif tab['settings']['mode'] == 'encrypt':
                file=QtWidgets.QFileDialog.getSaveFileName(
                        caption=mode,
                        directory=os.path.join(
                            self.config['default-ofile-dir'],
                            'keylist'+self.keyExt
                            ),
                        filter=self.config['filter-key-list']
                        )

            if file[0] == '':
                return self.missingKeyUpdate(ud_field=True,tab=tab)
            if os.path.splitext(file[0])[1] == '':
                return file[0]+self.keyExt 
        if file == ('',''):
            return ''
        else:
            return file[0]
    
    def progress_crypt(self,tab,chunks=None,size=None):
        if chunks != None and size != None:
            tab['obj'].progressBar.setFormat('{}/{} - %p%'.format(en.EngNumber(chunks,2),en.EngNumber(size,2)))
            tab['obj'].progressBar.setValue(int((chunks/size)*100))
            QtWidgets.QApplication.processEvents()
        else:
            return tab['obj'].progressBar,self.statusBar

    def tabDisable(self,tab,state):
        #tab['running']=state
        if tab['settings']['mode'] == 'decrypt':
            self.encrypt.setEnabled(state)
        elif tab['settings']['mode'] == 'encrypt':
            self.decrypt.setEnabled(state)

        for i in tab['dialog'].findChildren((QtWidgets.QWidget)):
            if i.objectName() != 'progressBar': 
                if i.objectName() == 'hash_log':
                    if tab['settings']['mode'] == 'decrypt':
                        if tab['obj'].checkHashes.isChecked() == True:
                            i.setEnabled(state)
                    elif tab['settings']['mode'] == 'encrypt':
                        if tab['obj'].useHashes.isChecked() == True:
                            i.setEnabled(state)
                else:
                    i.setEnabled(state)

    def missingKeyUpdate(self,ud_field=False,tab=None):
        if tab['settings']['mode'] == 'encrypt':
            k=os.path.basename(tab['settings']['ifile'])
            if k == '':
                k='keylist'+self.keyExt
            if os.path.splitext(k)[1] != self.keyExt:
                k+=self.keyExt
            kp=os.path.join(self.config['default-ofile-dir'],k)
            if os.path.splitext(kp)[1] == '':
                kp+=self.keyExt
            if ud_field == True:
                tab['obj'].key_list.setText(kp)
                tab['settings']['key_list']=kp
            return kp
        else:
            return ''

    def pathStatus(self,path,ofile=False):
        p=os.path.expandvars(os.path.expanduser(path))
        print(p)
        if ofile == True:
            return {
                    'exists':os.path.exists(os.path.dirname(p)),
                    }
        else:
            return {
                'exists':os.path.exists(p),
                'file':os.path.isfile(p),
                }


    def preCheck(self,tab):
        local=tab['settings']
        if local['mode'] == 'encrypt':
            for key in ['ifile','ofile','public_key','key_list']:            
                if key not in ['ofile','key_list']:
                    status=self.pathStatus(local[key])
                    print(status)
                    if status['exists'] == False:
                        return False
                    if status['file'] == False:
                        return False
                else:
                    status=self.pathStatus(local[key],ofile=True)
                    print(status)
                    if status['exists'] == False:
                        return False
        elif local['mode'] == 'decrypt':
            for key in ['ifile','ofile','private_key','key_list','hash_log']:
                if key != 'hash_log':
                    if key != 'ofile':
                        status=self.pathStatus(local[key])
                        if status['exists'] == False:
                            return False
                        if status['file'] == False:
                            return False
                    else:
                        status=self.pathStatus(local[key],ofile=True)
                        if status['exists'] == False:
                            return False
                elif key == 'hash_log':
                    if tab['settings']['mode'] == 'decrypt':
                        if tab['obj'].checkHashes.isChecked() == True:
                            status=self.pathStatus(local[key])
                            if status['exists'] == False:
                                return False
                            if status['file'] == False:
                                return False
                    if tab['settings']['mode'] == 'encrypt':
                        if tab['obj'].useHashes.isChecked() == True:
                            status=self.pathStatus(local[key],ofile=True)
                            if status['exists'] == False:
                                return False
        else:
            return None
        return True

    def __init__(self):
        super(self.__class__,self).__init__()
        self.load_config()

        self.setupUi(self)
        
        #setup the encrypt widget
        self.ew={}
        self.ew['dialog']=QtWidgets.QDialog(self)
        self.ew['obj']=encrypt_widget.Ui_encrypt()
        self.ew['obj'].setupUi(self.ew['dialog'])
        self.ew['settings']={
                'mode':'encrypt',
                'ifile':"",
                'ofile':"",
                'public_key':"",
                'key_list':"",
                'dataChunkSize':10485760
                }
        self.ew['running']=False
        self.ew['controls']=lib_ew_controls.controls(self)
        self.encrypt_layout.addWidget(self.ew['dialog'])


        #setup the decrypt widget
        self.dw={}
        self.dw['dialog']=QtWidgets.QDialog(self)
        self.dw['obj']=decrypt_widget.Ui_decrypt()
        self.dw['obj'].setupUi(self.dw['dialog'])
        self.dw['settings']={
                'mode':'decrypt',
                'ifile':"",
                'ofile':"",
                'private_key':"",
                'password':"",
                'key_list':"",
                'hash_log':"",
                }
        self.dw['running']=False
        self.dw['controls']=lib_dw_controls.controls(self)
        self.decrypt_layout.addWidget(self.dw['dialog'])


        #setup controls
        self.ctrl=libControl.controls()
        self.ctrl.init(self)
       
        #set default tab from config
        #if tab not in config, use hardcoded
        failTab=0
        for index in range(self.tabWidget.count()):
            if self.config['default-start-tab'] == self.tabWidget.tabText(index).lower():
                self.tabWidget.setCurrentIndex(index)
            else:
                failTab+=1
        if failTab == self.tabWidget.count():
            print('invalid default-start-tab value in config')
        
        
if __name__ == "__main__":
    a=QtWidgets.QApplication(sys.argv)
    app=ewk_gui()
    app.show()
    a.exec_()
