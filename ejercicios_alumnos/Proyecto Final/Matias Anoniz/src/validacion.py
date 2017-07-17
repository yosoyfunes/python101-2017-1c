# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(530, 300)
        Dialog.setMinimumSize(QtCore.QSize(530, 300))
        Dialog.setMaximumSize(QtCore.QSize(530, 300))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/persona.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet('''
            QPushButton { border: 2px solid #A5A5A5; border-radius: 10px; }
            QPushButton:hover { background-color: #b8cbff; }
            QLabel { text-align: right; }
            QLineEdit { border: 1px solid #CFCFCF; background-color: #FFFFFF; border-radius: 5px; }''')
        self.email = QtWidgets.QLineEdit(Dialog)
        self.email.setEnabled(True)
        self.email.setGeometry(QtCore.QRect(110, 140, 250, 31))
        self.email.setStyleSheet("")
        self.email.setObjectName("email")
        self.btnGuardar = QtWidgets.QPushButton(Dialog)
        self.btnGuardar.setGeometry(QtCore.QRect(210, 210, 70, 70))
        self.btnGuardar.setStyleSheet("")
        self.btnGuardar.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("img/Ugrabar.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnGuardar.setIcon(icon1)
        self.btnGuardar.setIconSize(QtCore.QSize(50, 50))
        self.btnGuardar.setObjectName("btnGuardar")
        self.nombre = QtWidgets.QLineEdit(Dialog)
        self.nombre.setEnabled(True)
        self.nombre.setGeometry(QtCore.QRect(110, 20, 250, 31))
        self.nombre.setToolTip("")
        self.nombre.setStyleSheet("")
        self.nombre.setText("")
        self.nombre.setReadOnly(False)
        self.nombre.setPlaceholderText("")
        self.nombre.setObjectName("nombre")
        self.apellido = QtWidgets.QLineEdit(Dialog)
        self.apellido.setEnabled(True)
        self.apellido.setGeometry(QtCore.QRect(110, 60, 250, 31))
        self.apellido.setStyleSheet("")
        self.apellido.setObjectName("apellido")
        self.txt_nombre = QtWidgets.QLabel(Dialog)
        self.txt_nombre.setGeometry(QtCore.QRect(40, 20, 60, 30))
        self.txt_nombre.setObjectName("txt_nombre")
        self.txt_apellido = QtWidgets.QLabel(Dialog)
        self.txt_apellido.setGeometry(QtCore.QRect(40, 60, 60, 30))
        self.txt_apellido.setObjectName("txt_apellido")
        self.txt_telefono = QtWidgets.QLabel(Dialog)
        self.txt_telefono.setGeometry(QtCore.QRect(40, 100, 60, 30))
        self.txt_telefono.setObjectName("txt_telefono")
        self.txt_email = QtWidgets.QLabel(Dialog)
        self.txt_email.setGeometry(QtCore.QRect(40, 140, 60, 30))
        self.txt_email.setObjectName("txt_email")
        self.telefono = QtWidgets.QLineEdit(Dialog)
        self.telefono.setEnabled(True)
        self.telefono.setGeometry(QtCore.QRect(110, 100, 250, 31))
        self.telefono.setStyleSheet("")
        self.telefono.setObjectName("telefono")
        self.imagen = QtWidgets.QLabel(Dialog)
        self.imagen.setGeometry(QtCore.QRect(390, 30, 121, 111))
        self.imagen.setText("")
        self.imagen.setPixmap(QtGui.QPixmap("img/persona.png"))
        self.imagen.setScaledContents(True)
        self.imagen.setWordWrap(False)
        self.imagen.setObjectName("imagen")
        self.btnCancelar = QtWidgets.QPushButton(Dialog)
        self.btnCancelar.setGeometry(QtCore.QRect(300, 210, 70, 70))
        self.btnCancelar.setStyleSheet("")
        self.btnCancelar.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("img/Ucancelar.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnCancelar.setIcon(icon2)
        self.btnCancelar.setIconSize(QtCore.QSize(50, 50))
        self.btnCancelar.setObjectName("btnCancelar")
        self.btnEditar = QtWidgets.QPushButton(Dialog)
        self.btnEditar.setGeometry(QtCore.QRect(120, 210, 70, 70))
        self.btnEditar.setStyleSheet("")
        self.btnEditar.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("img/Ueditar.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnEditar.setIcon(icon3)
        self.btnEditar.setIconSize(QtCore.QSize(50, 50))
        self.btnEditar.setObjectName("btnEditar")
        self.btnNuevo = QtWidgets.QPushButton(Dialog)
        self.btnNuevo.setGeometry(QtCore.QRect(30, 210, 70, 70))
        self.btnNuevo.setStyleSheet("")
        self.btnNuevo.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("img/Unuevo.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnNuevo.setIcon(icon4)
        self.btnNuevo.setIconSize(QtCore.QSize(50, 50))
        self.btnNuevo.setObjectName("btnNuevo")
        self.btnBuscar = QtWidgets.QPushButton(Dialog)
        self.btnBuscar.setGeometry(QtCore.QRect(380, 210, 70, 70))
        self.btnBuscar.setAutoFillBackground(False)
        self.btnBuscar.setStyleSheet("")
        self.btnBuscar.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("img/Ubuscar.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnBuscar.setIcon(icon5)
        self.btnBuscar.setIconSize(QtCore.QSize(50, 50))
        self.btnBuscar.setObjectName("btnBuscar")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Datos de Clientes"))
        self.btnGuardar.setToolTip(_translate("Dialog", "aceptar"))
        self.txt_nombre.setWhatsThis(_translate("Dialog", "<html><head/><body><p align=\"right\"><br/></p></body></html>"))
        self.txt_nombre.setText(_translate("Dialog", "<html><head/><body><p align=\"right\"><span style=\" font-weight:600;\">NOMBRE :</span></p></body></html>"))
        self.txt_apellido.setText(_translate("Dialog", "<html><head/><body><p align=\"right\"><span style=\" font-weight:600;\">APELLIDO :</span></p></body></html>"))
        self.txt_telefono.setText(_translate("Dialog", "<html><head/><body><p align=\"right\"><span style=\" font-weight:600;\">TELEFONO :</span></p></body></html>"))
        self.txt_email.setText(_translate("Dialog", "<html><head/><body><p align=\"right\"><span style=\" font-weight:600;\">E-MAIL :</span></p></body></html>"))
        self.btnCancelar.setToolTip(_translate("Dialog", "cancelar"))
        self.btnEditar.setToolTip(_translate("Dialog", "editar"))
        self.btnNuevo.setToolTip(_translate("Dialog", "agregar"))
        self.btnBuscar.setToolTip(_translate("Dialog", "buscar"))

