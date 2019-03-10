import os,json,logging, time

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
            "useHashLog-on-Start": true, 
            "ssh_dir": "/home/carl/.ssh", 
            "default_ofile_dir": "/home/carl/ekw-save", 
            "app_icon": "/home/carl/claptrap/icons/application.png" 
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
        pass

    def dumpToFile(me,self,cnf,cnf_name):
        #dump cnf to file
        try:
            with open(cnf_name,'w') as cfg:
                json.dump(cnf,cfg)
        except Exception as e:
            msg='couldn\'t dump emergency config to file: {}'.format(e)
            self.logger.error(msg)
            print(msg)
            
