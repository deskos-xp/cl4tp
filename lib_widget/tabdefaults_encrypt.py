# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui/tabdefaults_encrypt.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_tabdefaults_encrypt(object):
    def setupUi(self, tabdefaults_encrypt):
        tabdefaults_encrypt.setObjectName("tabdefaults_encrypt")
        tabdefaults_encrypt.resize(578, 416)
        self.gridLayout_2 = QtWidgets.QGridLayout(tabdefaults_encrypt)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea = QtWidgets.QScrollArea(tabdefaults_encrypt)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 556, 394))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.public_key = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.public_key.setDragEnabled(True)
        self.public_key.setClearButtonEnabled(True)
        self.public_key.setObjectName("public_key")
        self.gridLayout_3.addWidget(self.public_key, 5, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 4, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 5, 0, 1, 1)
        self.dataChunkSize = QtWidgets.QSpinBox(self.scrollAreaWidgetContents)
        self.dataChunkSize.setMaximum(999999999)
        self.dataChunkSize.setProperty("value", 10485760)
        self.dataChunkSize.setObjectName("dataChunkSize")
        self.gridLayout_3.addWidget(self.dataChunkSize, 0, 1, 1, 1)
        self.ifile = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.ifile.setDragEnabled(True)
        self.ifile.setClearButtonEnabled(True)
        self.ifile.setObjectName("ifile")
        self.gridLayout_3.addWidget(self.ifile, 1, 1, 1, 1)
        self.browse_key_list = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.browse_key_list.setObjectName("browse_key_list")
        self.gridLayout_3.addWidget(self.browse_key_list, 4, 2, 1, 1)
        self.ofile = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.ofile.setDragEnabled(True)
        self.ofile.setClearButtonEnabled(True)
        self.ofile.setObjectName("ofile")
        self.gridLayout_3.addWidget(self.ofile, 3, 1, 1, 1)
        self.browse_hash_log = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.browse_hash_log.setObjectName("browse_hash_log")
        self.gridLayout_3.addWidget(self.browse_hash_log, 6, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 3, 0, 1, 1)
        self.browse_public_key = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.browse_public_key.setObjectName("browse_public_key")
        self.gridLayout_3.addWidget(self.browse_public_key, 5, 2, 1, 1)
        self.browse_ifile = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.browse_ifile.setObjectName("browse_ifile")
        self.gridLayout_3.addWidget(self.browse_ifile, 1, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)
        self.hash_log = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.hash_log.setDragEnabled(True)
        self.hash_log.setClearButtonEnabled(True)
        self.hash_log.setObjectName("hash_log")
        self.gridLayout_3.addWidget(self.hash_log, 6, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 1, 0, 1, 1)
        self.key_list = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.key_list.setDragEnabled(True)
        self.key_list.setClearButtonEnabled(True)
        self.key_list.setObjectName("key_list")
        self.gridLayout_3.addWidget(self.key_list, 4, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 6, 0, 1, 1)
        self.browse_ofile = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.browse_ofile.setObjectName("browse_ofile")
        self.gridLayout_3.addWidget(self.browse_ofile, 3, 2, 1, 1)
        self.sizeInEN = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.sizeInEN.setObjectName("sizeInEN")
        self.gridLayout_3.addWidget(self.sizeInEN, 0, 2, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(tabdefaults_encrypt)
        QtCore.QMetaObject.connectSlotsByName(tabdefaults_encrypt)

    def retranslateUi(self, tabdefaults_encrypt):
        _translate = QtCore.QCoreApplication.translate
        tabdefaults_encrypt.setWindowTitle(_translate("tabdefaults_encrypt", "Form"))
        self.label_4.setText(_translate("tabdefaults_encrypt", "Key List"))
        self.label_5.setText(_translate("tabdefaults_encrypt", "Public Key"))
        self.browse_key_list.setText(_translate("tabdefaults_encrypt", "Browse"))
        self.browse_hash_log.setText(_translate("tabdefaults_encrypt", "Browse"))
        self.label_3.setText(_translate("tabdefaults_encrypt", "Ofile"))
        self.browse_public_key.setText(_translate("tabdefaults_encrypt", "Browse"))
        self.browse_ifile.setText(_translate("tabdefaults_encrypt", "Browse"))
        self.label.setText(_translate("tabdefaults_encrypt", "Chunk Size"))
        self.label_2.setText(_translate("tabdefaults_encrypt", "Infile"))
        self.label_6.setText(_translate("tabdefaults_encrypt", "Hash Log"))
        self.browse_ofile.setText(_translate("tabdefaults_encrypt", "Browse"))
        self.sizeInEN.setText(_translate("tabdefaults_encrypt", "EN: {}"))

