from PyQt5 import QtCore, QtGui, QtWidgets
import math
import graph


class UiMainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 366)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.functionDisplay = QtWidgets.QTextBrowser(self.centralwidget)
        self.functionDisplay.setEnabled(False)
        self.functionDisplay.setGeometry(QtCore.QRect(140, 80, 491, 41))
        self.functionDisplay.setObjectName("functionDisplay")
        self.funcList = QtWidgets.QComboBox(self.centralwidget)
        self.funcList.setGeometry(QtCore.QRect(42, 140, 171, 22))
        self.funcList.setObjectName("funcList")
        self.funcList.addItem("")
        self.funcList.addItem("")
        self.funcList.addItem("")
        self.funcList.addItem("")
        self.add = QtWidgets.QPushButton(self.centralwidget)
        self.add.setGeometry(QtCore.QRect(500, 140, 93, 28))
        self.add.setObjectName("add")
        self.parametrValue = QtWidgets.QLineEdit(self.centralwidget)
        self.parametrValue.setGeometry(QtCore.QRect(340, 140, 113, 22))
        self.parametrValue.setObjectName("parametrValue")
        self.parameter = QtWidgets.QLabel(self.centralwidget)
        self.parameter.setGeometry(QtCore.QRect(240, 140, 91, 16))
        self.parameter.setObjectName("parameter")
        self.coeff = QtWidgets.QLabel(self.centralwidget)
        self.coeff.setGeometry(QtCore.QRect(240, 170, 91, 16))
        self.coeff.setObjectName("coeff")
        self.coeffValue = QtWidgets.QLineEdit(self.centralwidget)
        self.coeffValue.setGeometry(QtCore.QRect(340, 170, 113, 22))
        self.coeffValue.setObjectName("coeffValue")
        self.ready = QtWidgets.QPushButton(self.centralwidget)
        self.ready.setGeometry(QtCore.QRect(350, 300, 93, 28))
        self.ready.setObjectName("ready")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.function = lambda x: 0;
        self.add.clicked.connect(self.addFunc)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.funcList.setItemText(0, _translate("MainWindow", "Степенная функция"))
        self.funcList.setItemText(1, _translate("MainWindow", "Косинус"))
        self.funcList.setItemText(2, _translate("MainWindow", "Синус"))
        self.funcList.setItemText(3, _translate("MainWindow", "Экспонента"))
        self.add.setText(_translate("MainWindow", "Добавить"))
        self.parameter.setText(_translate("MainWindow", "Параметр"))
        self.coeff.setText(_translate("MainWindow", "Коэффициент"))
        self.ready.setText(_translate("MainWindow", "Готово"))

    def addFunc(self):
        index = self.funcList.currentIndex()
        param = float(self.parametrValue.text())
        coefficient = float(self.coeffValue.text())
        prev = self.function
        if (index == 0):
            self.function = lambda x: prev(x) + coefficient*(x**param)
            self.functionDisplay.setText(self.functionDisplay.toPlainText() + (' ' + "%+.2d" %coefficient + ' x^' + "(%.2d)" %param))
        elif (index == 1):
            self.function = lambda x: prev(x) + coefficient*(math.cos(x))
            self.functionDisplay.setText(self.functionDisplay.toPlainText() + (' ' + "%+.2d" %coefficient + " cos(%.2d x)" %param))
        elif (index == 2):
            self.function = lambda x: prev(x) + coefficient*(math.sin(x))
            self.functionDisplay.setText(self.functionDisplay.toPlainText() + (' ' + "%+.2d" %coefficient + " sin(%.2d x)" %param))
        elif (index == 3):
            self.function = lambda x: prev(x) + coefficient*(math.exp(x))
            self.functionDisplay.setText(self.functionDisplay.toPlainText() + (' ' + "%+.2d" %coefficient + ' e^' "(%.2d x)" %param))
        else:
            return
    
    def getFunc(self):
        return self.function

    def getFuncString(self):
        return self.functionDisplay.toPlainText()