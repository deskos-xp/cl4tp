# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui/editSettings.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_editSettings(object):
    def setupUi(self, editSettings):
        editSettings.setObjectName("editSettings")
        editSettings.resize(750, 546)
        self.gridLayout_2 = QtWidgets.QGridLayout(editSettings)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea = QtWidgets.QScrollArea(editSettings)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 728, 524))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.encrypt_filter_ifile = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.encrypt_filter_ifile.setObjectName("encrypt_filter_ifile")
        self.gridLayout_3.addWidget(self.encrypt_filter_ifile, 4, 3, 1, 1)
        self.tool_encrypt_filter_ifile = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.tool_encrypt_filter_ifile.setEnabled(False)
        self.tool_encrypt_filter_ifile.setObjectName("tool_encrypt_filter_ifile")
        self.gridLayout_3.addWidget(self.tool_encrypt_filter_ifile, 4, 4, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_7.setObjectName("label_7")
        self.gridLayout_3.addWidget(self.label_7, 6, 1, 1, 1)
        self.tool_filter_public_key = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.tool_filter_public_key.setEnabled(False)
        self.tool_filter_public_key.setObjectName("tool_filter_public_key")
        self.gridLayout_3.addWidget(self.tool_filter_public_key, 6, 4, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 7, 1, 1, 1)
        self.app_icon = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.app_icon.setObjectName("app_icon")
        self.gridLayout_3.addWidget(self.app_icon, 10, 3, 1, 1)
        self.encrypt_filter_ofile = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.encrypt_filter_ofile.setObjectName("encrypt_filter_ofile")
        self.gridLayout_3.addWidget(self.encrypt_filter_ofile, 2, 3, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_8.setObjectName("label_8")
        self.gridLayout_3.addWidget(self.label_8, 5, 1, 1, 1)
        self.ssh_dir = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.ssh_dir.setObjectName("ssh_dir")
        self.gridLayout_3.addWidget(self.ssh_dir, 0, 3, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 8, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 9, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_12.setObjectName("label_12")
        self.gridLayout_3.addWidget(self.label_12, 1, 1, 1, 1)
        self.tool_filter_hash_log = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.tool_filter_hash_log.setEnabled(False)
        self.tool_filter_hash_log.setObjectName("tool_filter_hash_log")
        self.gridLayout_3.addWidget(self.tool_filter_hash_log, 9, 4, 1, 1)
        self.browse_ssh_dir = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.browse_ssh_dir.setObjectName("browse_ssh_dir")
        self.gridLayout_3.addWidget(self.browse_ssh_dir, 0, 4, 1, 1)
        self.tool_decrypt_filter_ifile = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.tool_decrypt_filter_ifile.setEnabled(False)
        self.tool_decrypt_filter_ifile.setObjectName("tool_decrypt_filter_ifile")
        self.gridLayout_3.addWidget(self.tool_decrypt_filter_ifile, 5, 4, 1, 1)
        self.filter_private_key = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.filter_private_key.setObjectName("filter_private_key")
        self.gridLayout_3.addWidget(self.filter_private_key, 7, 3, 1, 1)
        self.filter_key_list = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.filter_key_list.setObjectName("filter_key_list")
        self.gridLayout_3.addWidget(self.filter_key_list, 8, 3, 1, 1)
        self.browse_default_ofile_dir = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.browse_default_ofile_dir.setObjectName("browse_default_ofile_dir")
        self.gridLayout_3.addWidget(self.browse_default_ofile_dir, 1, 4, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_9.setObjectName("label_9")
        self.gridLayout_3.addWidget(self.label_9, 4, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 11, 1, 1, 1)
        self.tool_decrypt_filter_ofile = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.tool_decrypt_filter_ofile.setEnabled(False)
        self.tool_decrypt_filter_ofile.setObjectName("tool_decrypt_filter_ofile")
        self.gridLayout_3.addWidget(self.tool_decrypt_filter_ofile, 3, 4, 1, 1)
        self.filter_public_key = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.filter_public_key.setObjectName("filter_public_key")
        self.gridLayout_3.addWidget(self.filter_public_key, 6, 3, 1, 1)
        self.browse_app_icon = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.browse_app_icon.setObjectName("browse_app_icon")
        self.gridLayout_3.addWidget(self.browse_app_icon, 10, 4, 1, 1)
        self.tool_filter_key_list = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.tool_filter_key_list.setEnabled(False)
        self.tool_filter_key_list.setObjectName("tool_filter_key_list")
        self.gridLayout_3.addWidget(self.tool_filter_key_list, 8, 4, 1, 1)
        self.tool_encrypt_ofile_filter = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.tool_encrypt_ofile_filter.setEnabled(False)
        self.tool_encrypt_ofile_filter.setObjectName("tool_encrypt_ofile_filter")
        self.gridLayout_3.addWidget(self.tool_encrypt_ofile_filter, 2, 4, 1, 1)
        self.useHashLog_on_Start = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.useHashLog_on_Start.setObjectName("useHashLog_on_Start")
        self.gridLayout_3.addWidget(self.useHashLog_on_Start, 11, 4, 1, 1)
        self.default_ofile_dir = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.default_ofile_dir.setObjectName("default_ofile_dir")
        self.gridLayout_3.addWidget(self.default_ofile_dir, 1, 3, 1, 1)
        self.decrypt_filter_ifile = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.decrypt_filter_ifile.setObjectName("decrypt_filter_ifile")
        self.gridLayout_3.addWidget(self.decrypt_filter_ifile, 5, 3, 1, 1)
        self.tool_filter_private_key = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.tool_filter_private_key.setEnabled(False)
        self.tool_filter_private_key.setObjectName("tool_filter_private_key")
        self.gridLayout_3.addWidget(self.tool_filter_private_key, 7, 4, 1, 1)
        self.default_start_tab = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.default_start_tab.setObjectName("default_start_tab")
        self.default_start_tab.addItem("")
        self.default_start_tab.addItem("")
        self.gridLayout_3.addWidget(self.default_start_tab, 11, 3, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_10.setObjectName("label_10")
        self.gridLayout_3.addWidget(self.label_10, 3, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_11.setObjectName("label_11")
        self.gridLayout_3.addWidget(self.label_11, 2, 1, 1, 1)
        self.filter_hash_log = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.filter_hash_log.setObjectName("filter_hash_log")
        self.gridLayout_3.addWidget(self.filter_hash_log, 9, 3, 1, 1)
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 10, 1, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_13.setObjectName("label_13")
        self.gridLayout_3.addWidget(self.label_13, 0, 1, 1, 1)
        self.decrypt_filter_ofile = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.decrypt_filter_ofile.setObjectName("decrypt_filter_ofile")
        self.gridLayout_3.addWidget(self.decrypt_filter_ofile, 3, 3, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.reset = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.reset.setObjectName("reset")
        self.gridLayout_6.addWidget(self.reset, 0, 1, 1, 1)
        self.close = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.close.setObjectName("close")
        self.gridLayout_6.addWidget(self.close, 0, 2, 1, 1)
        self.save = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.save.setObjectName("save")
        self.gridLayout_6.addWidget(self.save, 0, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_6, 1, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 1, 1, 1)

        self.retranslateUi(editSettings)
        QtCore.QMetaObject.connectSlotsByName(editSettings)
        editSettings.setTabOrder(self.ssh_dir, self.default_ofile_dir)
        editSettings.setTabOrder(self.default_ofile_dir, self.encrypt_filter_ofile)
        editSettings.setTabOrder(self.encrypt_filter_ofile, self.decrypt_filter_ofile)
        editSettings.setTabOrder(self.decrypt_filter_ofile, self.encrypt_filter_ifile)
        editSettings.setTabOrder(self.encrypt_filter_ifile, self.decrypt_filter_ifile)
        editSettings.setTabOrder(self.decrypt_filter_ifile, self.filter_public_key)
        editSettings.setTabOrder(self.filter_public_key, self.filter_private_key)
        editSettings.setTabOrder(self.filter_private_key, self.filter_key_list)
        editSettings.setTabOrder(self.filter_key_list, self.filter_hash_log)
        editSettings.setTabOrder(self.filter_hash_log, self.app_icon)
        editSettings.setTabOrder(self.app_icon, self.default_start_tab)
        editSettings.setTabOrder(self.default_start_tab, self.browse_ssh_dir)
        editSettings.setTabOrder(self.browse_ssh_dir, self.browse_default_ofile_dir)
        editSettings.setTabOrder(self.browse_default_ofile_dir, self.browse_app_icon)
        editSettings.setTabOrder(self.browse_app_icon, self.useHashLog_on_Start)
        editSettings.setTabOrder(self.useHashLog_on_Start, self.save)
        editSettings.setTabOrder(self.save, self.reset)
        editSettings.setTabOrder(self.reset, self.close)
        editSettings.setTabOrder(self.close, self.tool_encrypt_ofile_filter)
        editSettings.setTabOrder(self.tool_encrypt_ofile_filter, self.tool_decrypt_filter_ofile)
        editSettings.setTabOrder(self.tool_decrypt_filter_ofile, self.tool_encrypt_filter_ifile)
        editSettings.setTabOrder(self.tool_encrypt_filter_ifile, self.tool_decrypt_filter_ifile)
        editSettings.setTabOrder(self.tool_decrypt_filter_ifile, self.tool_filter_private_key)
        editSettings.setTabOrder(self.tool_filter_private_key, self.tool_filter_public_key)
        editSettings.setTabOrder(self.tool_filter_public_key, self.tool_filter_key_list)
        editSettings.setTabOrder(self.tool_filter_key_list, self.tool_filter_hash_log)
        editSettings.setTabOrder(self.tool_filter_hash_log, self.scrollArea)

    def retranslateUi(self, editSettings):
        _translate = QtCore.QCoreApplication.translate
        editSettings.setWindowTitle(_translate("editSettings", "Edit Application-Wide Settings"))
        self.tool_encrypt_filter_ifile.setText(_translate("editSettings", "?"))
        self.label_7.setText(_translate("editSettings", "Filter Public Key"))
        self.tool_filter_public_key.setText(_translate("editSettings", "?"))
        self.label_6.setText(_translate("editSettings", "Filter Private Key"))
        self.label_8.setText(_translate("editSettings", "Decrypt Filter IFile"))
        self.label_5.setText(_translate("editSettings", "Filter Key-List"))
        self.label_4.setText(_translate("editSettings", "Filter Hash-Log"))
        self.label_12.setText(_translate("editSettings", "Default OFile Dir."))
        self.tool_filter_hash_log.setText(_translate("editSettings", "?"))
        self.browse_ssh_dir.setText(_translate("editSettings", "Browse"))
        self.tool_decrypt_filter_ifile.setText(_translate("editSettings", "?"))
        self.browse_default_ofile_dir.setText(_translate("editSettings", "Browse"))
        self.label_9.setText(_translate("editSettings", "Encrypt Filter IFile"))
        self.label_3.setText(_translate("editSettings", "Default Start Tab"))
        self.tool_decrypt_filter_ofile.setText(_translate("editSettings", "?"))
        self.browse_app_icon.setText(_translate("editSettings", "Browse"))
        self.tool_filter_key_list.setText(_translate("editSettings", "?"))
        self.tool_encrypt_ofile_filter.setText(_translate("editSettings", "?"))
        self.useHashLog_on_Start.setText(_translate("editSettings", "Use Hash Log On Start"))
        self.tool_filter_private_key.setText(_translate("editSettings", "?"))
        self.default_start_tab.setItemText(0, _translate("editSettings", "Encrypt"))
        self.default_start_tab.setItemText(1, _translate("editSettings", "Decrypt"))
        self.label_10.setText(_translate("editSettings", "Decrypt Filter OFile"))
        self.label_11.setText(_translate("editSettings", "Encrypt Filter OFile"))
        self.label.setText(_translate("editSettings", "App. Icon"))
        self.label_13.setText(_translate("editSettings", "SSH Dir."))
        self.reset.setToolTip(_translate("editSettings", "reset fields to defaults from file"))
        self.reset.setText(_translate("editSettings", "&Reset"))
        self.close.setToolTip(_translate("editSettings", "close dialog without saving"))
        self.close.setText(_translate("editSettings", "Clos&e"))
        self.save.setToolTip(_translate("editSettings", "save settings to file"))
        self.save.setText(_translate("editSettings", "&Save"))

