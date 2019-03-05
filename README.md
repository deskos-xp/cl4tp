tools for file encryption as well as for the purpose of learning Crypto in python3

example command

`python3 encryptWithKey.py -x avalon -P /home/carl/keys/public.key -p /home/carl/keys/private.key  -u ./archlinux-2018.05.01-x86_64.iso -E a -c 10485760 -e`

for the Qt Interface, use

`python3 ewk_gui.py`

```
usage: encryptWithKey.py [-h] [-p PRIVATE] [-P PUBLIC] [-x PASSWORD]
                         [-c CHUNKSIZE] [-k KEY_LIST] [-e] [-d]
                         [-u UNENCRYPTED_FILE] [-E ENCRYPTED_FILE]

 optional arguments:
  -h, --help            show this help message and exit
  -p PRIVATE, --private PRIVATE
                        privateKey
  -P PUBLIC, --public PUBLIC
                        publicKey
  -x PASSWORD, --password PASSWORD
                        password to privateKey
  -c CHUNKSIZE, --chunksize CHUNKSIZE
                        data chunksize to encrypt at one[larger chunks will
                        encrypt faster]
  -k KEY_LIST, --key-list KEY_LIST
                        name key_list will be given
  -e, --encrypt         encrypt a file
  -d, --decrypt         decrypt a file
  -u UNENCRYPTED_FILE, --unencrypted-file UNENCRYPTED_FILE
                        unencryped file
  -E ENCRYPTED_FILE, --encrypted-file ENCRYPTED_FILE
                        encrypted file
```
