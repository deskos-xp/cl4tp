from PyQt5 import QtWidgets,QtCore,QtGui
import json,os,sys,time
import engineering_notation as en


class timedMessageBox(QtWidgets.QMessageBox):
    def __init__(self,timeout,message):
        super(timedMessageBox,self).__init__()
        self.timeout=timeout
        self.message=message
        self.count=self.timeout
        timeoutMessage='Closing in {} seconds!'.format(self.timeout)
        self.setText('\n'.join((message,timeoutMessage)))
        self.msgTimer=QtCore.QTimer()
        self.msgTimer.timeout.connect(lambda: self.countDown())
        
    def countDown(self):
        self.count=self.count-1
        self.setText('{} \n Closing in {} seconds!'.format(self.message,self.count))
        print(self.count)
        if self.count < 1:
            self.msgTimer.stop()
            self.close()
        QtWidgets.QApplication.processEvents()
        
    def showEvent(self,event):    
        #QtCore.QTimer().singleShot(self.timeout*1000,self.close)
        self.msgTimer.start(1000)
        super(timedMessageBox,self).showEvent(event)

class tabdefaults_controls:
    def __init__(me,self):
        me.loadDefaults(self)
        me.buttons(self)

    def buttons(me,self):
        self.td['obj'].close.clicked.connect(lambda: me.close(self))
        self.td['obj'].save.clicked.connect(lambda: me.save(self))
        self.td['obj'].reset.clicked.connect(lambda: me.reset_dialog(self))
        self.td['obj'].clear.clicked.connect(lambda: me.clear(self))

    def clear(me,self):
        for t in self.td['settings'].keys():
            for key in self.td['settings'][t].keys():
                if type(self.td['settings'][t][key]) == type(str()):
                    self.td['settings'][t][key]=''
                elif type(self.td['settings'][t][key]) == type(int()):
                    self.td['settings'][t][key]=10*(1024**2)
            self.td['tabs'][t]['controls'].loadDefaults(self)        
            self.td['tabs'][t]['controls'].setField_data(self)

    def reset_dialog(me,self):
        me.loadDefaults(self)
        for t in self.td['settings'].keys():
            self.td['tabs'][t]['controls'].loadDefaults(self)
            self.td['tabs'][t]['controls'].setField_data(self)

    def reset_window(me,self):
        self.dw['controls'].reset_fields(self)
        self.ew['controls'].reset_fields(self)

    def close(me,self):
        self.td['dialog'].hide()
        me.reset_window(self)

    def loadDefaults(me,self):
        with open(self.field_defaults,'r') as cnf:
            self.td['settings']=json.load(cnf)

    def save(me,self):
        dec="Yes"
        warning=QtWidgets.QMessageBox(self)
        warning.setIcon(QtWidgets.QMessageBox.Warning)
        warning.setText('This operation will save your defaults to the configuration file for tab defaults? Do you wish to continue?')
        warning.setStandardButtons(QtWidgets.QMessageBox.No|QtWidgets.QMessageBox.Yes)
        warning.setDefaultButton(QtWidgets.QMessageBox.Yes)
        resolution=warning.exec()
        if resolution == QtWidgets.QMessageBox.Yes:
            self.td['settings']['encrypt']=self.td['tabs']['encrypt']['settings']
            self.td['settings']['decrypt']=self.td['tabs']['decrypt']['settings']
            with open(self.field_defaults,'w') as cnf:
                json.dump(self.td['settings'],cnf)
        else:
            dec='No'
        message='The user chose "{}".\n All operations have completed, you may now close the Tab Default\'s editor\n'.format(dec)

        info=timedMessageBox(5,message)
        info.setIcon(QtWidgets.QMessageBox.Information)
        info.exec()

