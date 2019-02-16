#! /usr/bin/env bash
#build library py from ui

src=('encrypt_widget' 'decrypt_widget' 'lib_ewk_gui')
ui='./ui'
lib_widget='./lib_widget'
for i in ${src[@]} ; do
	 cmd="$ui/$i.ui -o $lib_widget/$i.py"
	 echo $cmd
	 pyuic5 $cmd
done
