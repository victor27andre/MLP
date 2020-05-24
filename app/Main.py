# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui
from Trainer import Trainer
from classes.SigmoidMultLayerNetwork import SigmoidMultLayerNetwork
import json
import sys

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

class Main(QtGui.QWidget):

    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(778, 359)
        self.widget = QtGui.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(30, 110, 631, 141))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.widget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.petal_width = QtGui.QLineEdit(self.widget)
        self.petal_width.setObjectName(_fromUtf8("petal_width"))
        self.gridLayout_2.addWidget(self.petal_width, 2, 4, 1, 1)
        self.sepal_length = QtGui.QLineEdit(self.widget)
        self.sepal_length.setObjectName(_fromUtf8("sepal_length"))
        self.gridLayout_2.addWidget(self.sepal_length, 2, 0, 1, 1)
        self.label = QtGui.QLabel(self.widget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.widget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_2.addWidget(self.label_3, 1, 2, 1, 1)
        self.label_5 = QtGui.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_2.addWidget(self.label_5, 0, 0, 1, 1)
        self.label_4 = QtGui.QLabel(self.widget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_2.addWidget(self.label_4, 1, 4, 1, 1)
        self.petal_length = QtGui.QLineEdit(self.widget)
        self.petal_length.setObjectName(_fromUtf8("petal_length"))
        self.gridLayout_2.addWidget(self.petal_length, 2, 2, 1, 1)
        self.label_2 = QtGui.QLabel(self.widget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 1, 1, 1, 1)
        self.btnClassify = QtGui.QPushButton(self.widget)
        self.btnClassify.setObjectName(_fromUtf8("btnClassify"))
        self.gridLayout_2.addWidget(self.btnClassify, 3, 0, 1, 1)
        #self.sepal_width = QtGui.QLineEdit(self.widget)
        #self.sepal_width.setObjectName(_fromUtf8("sepal_width"))
        #self.gridLayout_2.addWidget(self.sepal_width, 2, 1, 1, 1)
        self.widget_2 = QtGui.QWidget(Form)
        self.widget_2.setGeometry(QtCore.QRect(30, 30, 600, 100))
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
        self.widget_3 = QtGui.QWidget(Form)
        self.widget_3.setGeometry(QtCore.QRect(30, 260, 241, 81))
        self.widget_3.setObjectName(_fromUtf8("widget_3"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.widget_3)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label_8 = QtGui.QLabel(self.widget_3)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.verticalLayout_3.addWidget(self.label_8)
        self.result_label = QtGui.QLabel(self.widget_3)
        self.result_label.setObjectName(_fromUtf8("result_label"))
        self.verticalLayout_3.addWidget(self.result_label)
        self.btnTrain = QtGui.QPushButton(Form)
        self.btnTrain.setGeometry(QtCore.QRect(470, 30, 191, 27))
        self.btnTrain.setObjectName(_fromUtf8("btnTrain"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Rede Multicamada - Classificação", None))
        self.label.setText(_translate("Form", "Entrada 1", None))
        self.label_2.setText(_translate("Form", "Entrada 2", None))
        self.label_3.setText(_translate("Form", "Entrada 3", None))
        #self.label_4.setText(_translate("Form", "Entrada 4", None))

        self.label_5.setText(_translate("Form", "Entradas", None))
        self.label_6.setText(_translate("Form", "Dois ligados", None))
        self.label_7.setText(_translate("Form", "Insira 1 para ligado e 0 para desligado.\nCaso existam duas entradas ligadas o retorno vai ser 1, se não vai ser 0", None))
        self.label_8.setText(_translate("Form", "Resultado", None))
        self.result_label.setText(_translate("Form", "", None))

        self.btnTrain.setText(_translate("Form", "Realizar treinamento", None))
        self.btnTrain.clicked.connect(self.openTrainerScreen)
        self.btnClassify.setText(_translate("Form", "Classificar", None))
        self.btnClassify.clicked.connect(self.classify) #faz a ação de classificar

    def classify(self):
        x1 = float(self.petal_length.text())
        x2 = float(self.petal_width.text())
        x3 = float(self.sepal_length.text())
        #x4 = int(self.sepal_width.text())

        try:
            file_loaded = open("weight.json", "r")
            weights = json.load(file_loaded)
            sgnt = SigmoidMultLayerNetwork(3)
            sgnt.hidden_layer_weights = weights['hidden_layer']
            sgnt.weights = weights['input_layer']
            result = float(sgnt.test([x1, x2, x3]))
            self.result_label.setText(_translate("Form", str(result), None))
        except Exception as e:
           print("Erro: " + e.message)

        print("x1: %s, x2: %s, x3: %s" %(x1, x2, x3))
        

    def openTrainerScreen(self):
        screen = Trainer()
        screen.show()
        sys.exit(screen.exec_())

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = Main()
    ex.show()
    sys.exit(app.exec_())
