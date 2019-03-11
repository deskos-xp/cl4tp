# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui/tabdefaults.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_tabDefaults(object):
    def setupUi(self, tabDefaults):
        tabDefaults.setObjectName("tabDefaults")
        tabDefaults.resize(639, 488)
        self.gridLayout_2 = QtWidgets.QGridLayout(tabDefaults)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.clear = QtWidgets.QPushButton(tabDefaults)
        self.clear.setObjectName("clear")
        self.gridLayout_3.addWidget(self.clear, 0, 1, 1, 1)
        self.save = QtWidgets.QPushButton(tabDefaults)
        self.save.setObjectName("save")
        self.gridLayout_3.addWidget(self.save, 0, 0, 1, 1)
        self.close = QtWidgets.QPushButton(tabDefaults)
        self.close.setObjectName("close")
        self.gridLayout_3.addWidget(self.close, 0, 3, 1, 1)
        self.reset = QtWidgets.QPushButton(tabDefaults)
        self.reset.setObjectName("reset")
        self.gridLayout_3.addWidget(self.reset, 0, 2, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_3, 1, 0, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(tabDefaults)
        self.tabWidget.setObjectName("tabWidget")
        self.encrypt = QtWidgets.QWidget()
        self.encrypt.setObjectName("encrypt")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.encrypt)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.tabEncrypt = QtWidgets.QGridLayout()
        self.tabEncrypt.setObjectName("tabEncrypt")
        self.gridLayout_4.addLayout(self.tabEncrypt, 0, 0, 1, 1)
        self.tabWidget.addTab(self.encrypt, "")
        self.decrypt = QtWidgets.QWidget()
        self.decrypt.setObjectName("decrypt")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.decrypt)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.tabDecrypt = QtWidgets.QGridLayout()
        self.tabDecrypt.setObjectName("tabDecrypt")
        self.gridLayout_6.addLayout(self.tabDecrypt, 0, 0, 1, 1)
        self.tabWidget.addTab(self.decrypt, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(tabDefaults)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(tabDefaults)

    def retranslateUi(self, tabDefaults):
        _translate = QtCore.QCoreApplication.translate
        tabDefaults.setWindowTitle(_translate("tabDefaults", "Form"))
        self.clear.setToolTip(_translate("tabDefaults", "Clear fields using internal defaults not in configuration file"))
        self.clear.setText(_translate("tabDefaults", "Clear"))
        self.save.setToolTip(_translate("tabDefaults", "save data to configuration file"))
        self.save.setText(_translate("tabDefaults", "Save"))
        self.close.setToolTip(_translate("tabDefaults", "close without saving"))
        self.close.setText(_translate("tabDefaults", "Close"))
        self.reset.setToolTip(_translate("tabDefaults", "reset fields from data contained within configuration file"))
        self.reset.setText(_translate("tabDefaults", "Reset"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.encrypt), _translate("tabDefaults", "Encrypt"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.decrypt), _translate("tabDefaults", "Decrypt"))


