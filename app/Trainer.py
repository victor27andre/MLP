# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'treinamento.ui'
#
# Created by: PyQt5 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

import sys
import pandas as pd
from PyQt5.QtGui import *
from PyQt5 import QtCore, QtGui
from classes.SigmoidMultLayerNetwork import SigmoidMultLayerNetwork

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Trainer(QtGui.QWidget):

    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(791, 291)
        self.widget_2 = QtGui.QWidget(Form)
        self.widget_2.setGeometry(QtCore.QRect(20, 30, 361, 67))
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_6 = QtGui.QLabel(self.widget_2)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(11, 158, 28))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(11, 158, 28))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(123, 123, 123))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_6.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setAcceptDrops(True)
        self.label_6.setAutoFillBackground(True)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.verticalLayout_2.addWidget(self.label_6)
        self.label_7 = QtGui.QLabel(self.widget_2)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.verticalLayout_2.addWidget(self.label_7)
        self.widget = QtGui.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(20, 110, 361, 141))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.txtEpochs = QtGui.QLineEdit(self.widget)
        self.txtEpochs.setGeometry(QtCore.QRect(9, 72, 151, 27))
        self.txtEpochs.setObjectName(_fromUtf8("txtEpochs"))
        self.label = QtGui.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(10, 40, 41, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_5 = QtGui.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(9, 9, 330, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.btnTrain = QtGui.QPushButton(self.widget)
        self.btnTrain.setGeometry(QtCore.QRect(9, 105, 151, 27))
        self.btnTrain.setObjectName(_fromUtf8("btnTrain"))
        self.widget_3 = QtGui.QWidget(Form)
        self.widget_3.setGeometry(QtCore.QRect(390, 30, 381, 231))
        self.widget_3.setObjectName(_fromUtf8("widget_3"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget_3)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_2 = QtGui.QLabel(self.widget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.consoleArea = QtGui.QPlainTextEdit(self.widget_3)
        self.consoleArea.setObjectName(_fromUtf8("consoleArea"))
        self.verticalLayout.addWidget(self.consoleArea)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Rede Multicamada - Treinamento", None))
        self.label_6.setText(_translate("Form", "Treinamento", None))
        self.label_7.setText(_translate("Form", "Insira a quantidade limite de épocas.", None))
        self.label.setText(_translate("Form", "Épocas", None))
        self.label_5.setText(_translate("Form", "Entrada de informações para o treinamento", None))
        self.btnTrain.setText(_translate("Form", "Treinar", None))
        self.label_2.setText(_translate("Form", "Console com as informações do treinamento", None))

        self.btnTrain.clicked.connect(self.trainerNetwork)

    def trainerNetwork(self):

        if(self.txtEpochs.text() != ''):
            epochs = int(self.txtEpochs.text())
            train_input = pd.read_csv('../dataset/train-input.csv')
            train_output = pd.read_csv('../dataset/train-output.csv')
            sgnt = SigmoidMultLayerNetwork(3)
            sgnt.epoch_quantity = epochs
            sgnt.dataset["input"] = train_input.values
            sgnt.dataset["output"] = train_output.values
            self.consoleArea.clear()
            sgnt.trainer(self.consoleArea)
            sgnt.saveData('weights.json')
        else:
            QMessageBox.information(self, "Message", "Informe um valor valido.")


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = Trainer()
    ex.show()
    sys.exit(app.exec_())
