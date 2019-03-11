import os,json,logging, time
from PyQt5 import QtWidgets
class emergency:
    config={
            "ssh-dir": "/home/carl/.ssh",
            "default-ofile-dir": "/home/carl/ekw-save",
            "decrypt-filter-ofile": "All Files (*)",
            "encrypt-filter-ofile": "Encrypted Binary (*.ebin);;All Files (*)",
            "decrypt-filter-ifile": "Encrypted Binary (*.ebin);;All Files (*)",
            "encrypt-filter-ifile": "All Files (*)", 
            "filter-public-key": "Key File (*.key);;Public Key (*.pub);;All Files (*)", 
            "filter-private-key": "Key File (*.key);;Private Key (*.priv);;All Files (*)", 
            "filter-key-list": "Encrypted Json Key List (*.ejk);;All Files (*)",
            "filter-hash-log": "Hash Log (*.hash);;All Files (*)",
            "default-start-tab": "encrypt", 
            "app-icon": "/home/carl/claptrap/icons/application.png", 
            "useHashLog-on-Start": True, 
            }

    tab_defaults={
            "encrypt": {
                "mode": "",
                "dataChunkSize": 10485760,
                "ifile": "", 
                "ofile": "", 
                "key_list": "", 
                "public_key": "", 
                "hash_log": ""},
            "decrypt": {
                "mode": "", 
                "ifile": "", 
                "ofile": "", 
                "key_list": "", 
                "private_key": "", 
                "password": "", 
                "hash_log": ""
                }
            }

    def __init__(me,self):
        me.modify_config(self)
        
    def modify_config(me,self):
        #modify self.config for the particulars of the current user before dumping to file
        me.config['ssh-dir']=os.path.join(os.environ['HOME'],'.ssh')
        me.config['default-ofile-dir']=os.path.join(os.environ['HOME'],'ekw_save')
        me.config['app-icon']=os.path.join(os.environ['PWD'],'icons/application.png')

    def dumpToFile(me,self,cnf,cnf_name):
        #dump cnf to file
        try:
            with open(cnf_name,'w') as cfg:
                json.dump(cnf,cfg)
        except Exception as e:
            msg='couldn\'t dump emergency config to file: {}'.format(e)
            self.logger.error(msg)
            print(msg)
            raise FileNotFoundError 
            

    def generate(me,self):
        err=[]
        try:
            me.dumpToFile(self,me.tab_defaults,self.field_defaults)
        except Exception as e:
            err.append(str(e))
            self.logger.error('there was a problem writing config file {} : {}'.format(
                os.path.join(
                    self.conf_dir,
                    self.field_defaults
                    ),
                str(e)
                )
                )
        try:
            me.dumpToFile(self,me.config,self.config_file)
        except Exception as e:
            err.append(str(e))
            self.logger.error('there was a problem writing config file {} : {}'.format(
                os.path.join(
                    self.conf_dir,
                    self.config_file
                    ),
                str(e)
                )
                )
        if len(err) > 0:
            print(err)
            dialog=QtWidgets.QMessageBox(self)
            dialog.setIcon(QtWidgets.QMessageBox.Critical)
            dialog.setText('There was an Error!')
            dialog.setInformativeText(',\n'.join(err))
            dialog.setStandardButtons(QtWidgets.QMessageBox.Ok)
            dialog.setDefaultButton(QtWidgets.QMessageBox.Ok)
            dialog.exec()
