#! /usr/bin/env python3

import json,os,sys,gzip
import argparse,string

from Crypto.Cipher import AES,PKCS1_OAEP
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA512
from Crypto.PublicKey import RSA
from Crypto import Random
from os import urandom
import base64
import engineering_notation as en

class druugianNightmare:
    def __init__(self):
        pass
   
    extU='_private.jkey'
    extE='_private.ejk'
    def newKeys(self,password=None,keySize=2048):
        random=Random.new().read(keySize)
        key=RSA.generate(keySize)
        privKey=key.exportKey(
                passphrase=password,
                format='PEM',
                pkcs=8,
                protection='scryptAndAES256-CBC'
                )
        pubKey=key.publickey().exportKey()
        return {'public-key':pubKey,'private-key':privKey}

    def importKey(self,key,password=None):
        return RSA.importKey(key,passphrase=password)
    
    def importPublicKey(self,key):
        return RSA.importKey(key)

    def writeKeys(self,keys={'private-key':None,'public-key':None},privKeyFD='private.key',pubKeyFD='public.key'):
        state=[False,'']
        #write private key
        if keys['private-key'] != None:
            with open(privKeyFD,'wb') as fileIO:
                fileIO.write(keys['private-key']+b'\n')
            state=True
        else:
            state=[False,'private-key']

        #write public key
        if keys['public-key'] != None:
            state=True
            with open(pubKeyFD,'wb') as fileIO:
                fileIO.write(keys['public-key']+b'\n')
        else:
            state=[False,'public-key']

        return state

    def sign(self,msg,privKey):
        signer=PKCS1_v1_5.new(privKey)
        digest=SHA512.new()
        digest.update(msg)
        return signer.sign(digest)

    def verify(self,msg,sig,pubKey):
        signer=PKCS1_v1_5.new(pubKey)
        digest=SHA512.new()
        digest.update(msg)
        return signer.verify(digest,sig)

    def encryptMessage(self,msg,pubKey):
        msg=gzip.compress(msg)
        cipher=PKCS1_OAEP.new(pubKey)
        #ctext=cipher.encrypt(gzip.compress(msg))
        phrase=os.urandom(32)
        cipherPhrase=cipher.encrypt(phrase)
        msgCipher=AES.new(key=phrase,mode=AES.MODE_EAX)
        ctext=msgCipher.encrypt(msg)
        #make random passphrase
        #encrypt passphrase with pubkey

        #if type(privateKey) != type(None): 
        #    privateKey=privateKey.exportKey().decode()
        return {
                'ctext':ctext,
                'chunk':{
                'size':len(ctext),
                'phrase':base64.b64encode(cipherPhrase).decode(),
                'nonce':base64.b64encode(msgCipher.nonce).decode()
                },
                }

    def decryptMessage(self,msg,privateKey,cipherPhrase,nonce):
        publicKey=privateKey.publickey()
        cipher=PKCS1_OAEP.new(privateKey)
        phrase=cipher.decrypt(cipherPhrase)
        msgCipher=AES.new(key=phrase,mode=AES.MODE_EAX,nonce=nonce)
        plaintext=gzip.decompress(msgCipher.decrypt(msg))
        sig=self.sign(plaintext,privateKey)
        verify=self.verify(plaintext,sig,publicKey)
        return plaintext,verify

    def encryptKeyList(self,masterKeyPub,ifname,fname):
        key=RSA.importKey(open(masterKeyPub,'r').read())
        kcipher=PKCS1_OAEP.new(key)
        tmp=os.urandom(32)
        etmp=kcipher.encrypt(tmp)
        cipher=AES.new(key=tmp,mode=AES.MODE_EAX)
        with open(ifname,'rb') as inf, open(fname,'wb') as keylist:
            keylist.write(etmp+cipher.nonce)
            while True:
                d=inf.read(256)
                if not d:
                    break
                data=cipher.encrypt(d)
                keylist.write(data)

    def decryptKeyList(self,masterKeyPriv,password,fname,ofname):
        key=RSA.importKey(open(masterKeyPriv,'rb').read(),password)
        kcipher=PKCS1_OAEP.new(key)
        nonce=None
        etmp=None
        with open(fname,'rb') as kl, open(ofname,'wb') as ofn:
            etmp=kl.read(256)
            nonce=kl.read(16)
            tmp=kcipher.decrypt(etmp) 
            cipher=AES.new(key=tmp,mode=AES.MODE_EAX,nonce=nonce)
            while True:
                d=kl.read(256)
                if not d:
                    break
                keys=cipher.decrypt(d)
                ofn.write(keys) 

    def encryptFile(self,ifile,ofile,masterKeyPub,key_list=None,chunksize=2048,progress_callback=None,tab=None):
        if key_list == None:
            key_list=os.path.splitext(ifile)[0]+self.extE
        tmpName=os.path.splitext(key_list)[0]+self.extU
        keys={}
        count=0
        totalChunks=0
        out=open(ofile,'wb')
        size=os.path.getsize(ifile)
        with open(ifile,'rb') as dsrc:
            while True:
                #d=dsrc.read(int((chunksize/8)-2)-(64*2))
                d=dsrc.read(chunksize)
                if not d:
                    break
                totalChunks+=len(d)
                print('[ENCRYPT] {}/{} - {}%'.format(
                    en.EngNumber(totalChunks,2),
                    en.EngNumber(size,2),
                    round((totalChunks/size)*100,2)
                    )
                    )
                if progress_callback != None and tab != None:
                    progress_callback(tab,totalChunks,size)
                publicKey=self.importKey(open(masterKeyPub,'rb').read())
                ctext=self.encryptMessage(d,publicKey)
                keys[str(count)]=ctext['chunk']
                out.write(ctext['ctext'])
                count+=1
        out.close() 
        with open(tmpName,'w') as keyList:
            json.dump(keys,keyList)    
        self.encryptKeyList(masterKeyPub,tmpName,key_list)
        os.remove(tmpName)
        #for file verification
        #p=progress_callback(tab)
        self.generate_hash_log(
                tab=tab,
                ifile=ifile,
                ofile=ofile,
                key_list=key_list,
                progress_callback=progress_callback,
                chunksize=chunksize
                )
        
    def generate_hash_log(self,tab,ifile,ofile,key_list,progress_callback=None,chunksize=2048):
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


    def decryptFile(self,ifile,ofile,masterKeyPriv,password_to_masterKey=None,key_list=None,progress_callback=None,tab=None):
        if key_list == None:
            key_list=os.path.splitext(ofile)[0]+self.extE
        tmpName=os.path.splitext(key_list)[0]+self.extU
        self.decryptKeyList(masterKeyPriv,password=password_to_masterKey,fname=key_list,ofname=tmpName)
        keys={}
        keyList=open(tmpName,'r')
        keys=json.load(keyList)
        os.remove(tmpName)
        privateKey=self.importKey(open(masterKeyPriv,'rb').read(),password=password_to_masterKey)
        count=[str(i) for i in sorted([int(i) for i in keys.keys()])]
        out=open(ofile,'wb')
        #for progress view
        counter=0
        size=os.path.getsize(ifile)
        with open(ifile,'rb') as dsrc:
            for num,i in enumerate(count):
                d=dsrc.read(keys[i]['size'])
                text,err=self.decryptMessage(d,privateKey,base64.b64decode(keys[i]['phrase']),base64.b64decode(keys[i]['nonce']))
                if err == False:
                    print('looks corrupted | tampered with: {}'.format(num*keys[i]['size']))
                out.write(text)
                counter+=keys[i]['size']
                print('[DECRYPT] {}/{} - {}%'.format(
                    en.EngNumber(counter,2),
                    en.EngNumber(size,2),
                    round((counter/size)*100,2),
                    )
                    )
                if progress_callback != None and tab != None:
                    progress_callback(tab,counter,size)
            out.close()

class cmdline:
    def expand(self,path):
        return os.path.expanduser(os.path.expandvars(path))

    def init(self):
        parser=argparse.ArgumentParser()
        parser.add_argument('-p','--private',help='privateKey')
        parser.add_argument('-P','--public',help='publicKey')
        parser.add_argument('-x','--password',help='password to privateKey')
        parser.add_argument('-c','--chunksize',help='data chunksize to encrypt at one[larger chunks will encrypt faster]',default=10*(1024**2))
        parser.add_argument('-k','--key-list',help='name key_list will be given')
        parser.add_argument('-e','--encrypt',help='encrypt a file',action='store_true')
        parser.add_argument('-d','--decrypt',help='decrypt a file',action='store_true')
        parser.add_argument('-u','--unencrypted-file',help='unencryped file')
        parser.add_argument('-E','--encrypted-file',help='encrypted file')
        options=parser.parse_args()
        opts={ 
                x:getattr(options,x) for x in [
                    i for i in dir(options) if not callable(getattr(options,i)) if not i.startswith('__')
                    ]
                } 
        try:
            opts['encrypted_file']=self.expand(opts['encrypted_file'])
            opts['unencrypted_file']=self.expand(opts['unencrypted_file'])
        except TypeError as e:
            exit('paths cannot be empty:\n\t{}'.format(e))
        try:
            opts['chunksize']=int(opts['chunksize'])
        except ValueError as e:
            try:
                print('invalid chunksize value... going to try something else...!')
                num=''
                for i in opts['chunksize']:
                    if i in string.printable:
                        num+=str(ord(i))
                opts['chunksize']=int(num)
            except:
                print(
                        '''
                        unfortunately the alternative
                        method for getting chunksize
                        failed; so now I will be using
                        the internal default!
                        '''
                        )
                opts['chunksize']=int(10*(1024**2))
        return opts

if __name__ == '__main__':
    skip=True
    options=cmdline().init()
    for key in options.keys():
        if key != 'chunksize':
            print('{} - {}'.format(key,options[key]))
        else:
            print('{} ({}) - {}'.format(key,options[key],en.EngNumber(options[key],2)))

    if options['encrypt'] == True and options['decrypt'] == True:
        skip = False
    if options['encrypt'] == True or options['decrypt'] == True:
        skip = False

    if skip == False:
        app=druugianNightmare()
        if options['encrypt']:
            #chunk size is the binary equivalent to 10MB
            #chunksize=10*(1024**2)
            #key_list are will assume the format "unencrypted_fname""_private.ejk" if set/left as None
            #args are as follows
            #unencrypted file,encrypted filename,privateKey,publickey,password to private key
            #data chunksize to encrypt at one time
            #key_list, which determines the secondary key required for file decryption
            app.encryptFile(
                    ifile=options['unencrypted_file'],
                    ofile=options['encrypted_file'],
                    masterKeyPub=options['public'],
                    chunksize=options['chunksize'],
                    key_list=options['key_list']
                    )
        if options['decrypt']:
            #args are as follows
            #encrypted file
            #unencrypted filename
            #privatekey
            #password to masterkey
            #key_list name
            app.decryptFile(
                    ifile=options['encrypted_file'],
                    ofile=options['unencrypted_file'],
                    masterKeyPriv=options['private'],
                    password_to_masterKey=options['private'],
                    key_list=options['key_list'],
                    )
    else:
        print('it looks like you forgot to specify operating mode! {}/{}'.format('-e','-d'))
