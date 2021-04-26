from PyQt5 import QtCore, QtGui, QtWidgets
from pyqtgraph import PlotWidget
import tablemodel
import numath

class Ui_MainWindow(object):
    def setupUi(self, MainWindow, function):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.data = []
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.graph = PlotWidget(self.centralwidget)
        self.graph.setGeometry(QtCore.QRect(20, 20, 371, 251))
        self.graph.setObjectName("graph")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(420, 20, 331, 281))
        self.stackedWidget.setObjectName("stackedWidget")
        self.newtons = QtWidgets.QWidget()
        self.newtons.setObjectName("newtons")
        self.formLayoutWidget = QtWidgets.QWidget(self.newtons)
        self.formLayoutWidget.setGeometry(QtCore.QRect(30, 30, 271, 276))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.label_5)
        self.leftNewtone = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.leftNewtone.setObjectName("leftNewtone")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.leftNewtone)
        self.rightNewtone = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.rightNewtone.setObjectName("rightNewtone")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.rightNewtone)
        self.approxNewton = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.approxNewton.setObjectName("approxNewton")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.approxNewton)
        self.accuracyNewton = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.accuracyNewton.setObjectName("accuracyNewton")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.accuracyNewton)
        self.label_21 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_21.setObjectName("label_21")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_21)
        self.label_22 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_22.setObjectName("label_22")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_22)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.startNewton = QtWidgets.QPushButton(self.formLayoutWidget)
        self.startNewton.setObjectName("startNewton")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.startNewton)
        self.stackedWidget.addWidget(self.newtons)
        self.iterations = QtWidgets.QWidget()
        self.iterations.setObjectName("iterations")
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.iterations)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(30, 30, 271, 237))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_3 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.formLayout_3.setObjectName("formLayout_3")
        self.startIter = QtWidgets.QPushButton(self.formLayoutWidget_2)
        self.startIter.setObjectName("startIter")
        self.formLayout_3.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.startIter)
        self.label_10 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_10.setObjectName("label_10")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.label_10)
        self.rightIter = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.rightIter.setObjectName("rightIter")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.rightIter)
        self.leftIter = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.leftIter.setObjectName("leftIter")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.leftIter)
        self.label_23 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_23.setObjectName("label_23")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_23)
        self.label_24 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_24.setObjectName("label_24")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_24)
        self.accuracy_Iter = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.accuracy_Iter.setObjectName("accuracy_Iter")
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.accuracy_Iter)
        self.approx_Iter = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.approx_Iter.setObjectName("approx_Iter")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.approx_Iter)
        self.label_9 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_9.setObjectName("label_9")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.label_8 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_8.setObjectName("label_8")
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.stackedWidget.addWidget(self.iterations)
        self.hords = QtWidgets.QWidget()
        self.hords.setObjectName("hords")
        self.formLayoutWidget_3 = QtWidgets.QWidget(self.hords)
        self.formLayoutWidget_3.setGeometry(QtCore.QRect(30, 30, 271, 231))
        self.formLayoutWidget_3.setObjectName("formLayoutWidget_3")
        self.formLayout_5 = QtWidgets.QFormLayout(self.formLayoutWidget_3)
        self.formLayout_5.setContentsMargins(0, 0, 0, 0)
        self.formLayout_5.setObjectName("formLayout_5")
        self.startHords = QtWidgets.QPushButton(self.formLayoutWidget_3)
        self.startHords.setObjectName("startHords")
        self.formLayout_5.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.startHords)
        self.label_20 = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.label_20.setObjectName("label_20")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.label_20)
        self.left = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        self.left.setObjectName("left")
        self.formLayout_5.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.left)
        self.right = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        self.right.setObjectName("right")
        self.formLayout_5.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.right)
        self.accuracyhords = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        self.accuracyhords.setObjectName("accuracyhords")
        self.formLayout_5.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.accuracyhords)
        self.label_16 = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.label_16.setObjectName("label_16")
        self.formLayout_5.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_16)
        self.label_17 = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.label_17.setObjectName("label_17")
        self.formLayout_5.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_17)
        self.label_19 = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.label_19.setObjectName("label_19")
        self.formLayout_5.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_19)
        self.stackedWidget.addWidget(self.hords)
        self.table = QtWidgets.QTableView(self.centralwidget)
        self.table.setGeometry(QtCore.QRect(55, 341, 691, 211))
        self.table.setObjectName("table")
        self.graph.showGrid(x=True, y=True)
        self.error = QtWidgets.QLabel(self.centralwidget)
        self.error.setGeometry(QtCore.QRect(300, 300, 270, 16))
        self.error.setText("")
        self.error.setObjectName("error")
        self.save = QtWidgets.QPushButton(self.centralwidget)
        self.save.setGeometry(QtCore.QRect(150, 300, 121, 24))
        self.save.setObjectName("save")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(630, 300, 121, 28))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.function = function
        self.pushButton.clicked.connect(self.changeMethod)
        self.startHords.clicked.connect(self.HordesInit)
        self.startNewton.clicked.connect(self.NewtonInit)
        self.startIter.clicked.connect(self.IterationInit)
        self.save.clicked.connect(self.saveToFile)
        self.updateGraph(-10,10)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_5.setText(_translate("MainWindow", "Метод Ньютона"))
        self.label_21.setText(_translate("MainWindow", "Левая граница"))
        self.label_22.setText(_translate("MainWindow", "Правая граница"))
        self.label_4.setText(_translate("MainWindow", "Приближение"))
        self.label_3.setText(_translate("MainWindow", "Точность"))
        self.startNewton.setText(_translate("MainWindow", "Рассчитать"))
        self.startIter.setText(_translate("MainWindow", "Рассчитать"))
        self.label_10.setText(_translate("MainWindow", "Метод простой итерации"))
        self.label_23.setText(_translate("MainWindow", "Левая граница"))
        self.label_24.setText(_translate("MainWindow", "Правая граница"))
        self.label_9.setText(_translate("MainWindow", "Приближение"))
        self.label_8.setText(_translate("MainWindow", "Точность"))
        self.startHords.setText(_translate("MainWindow", "Рассчитать"))
        self.label_20.setText(_translate("MainWindow", "Метод Хорд"))
        self.label_16.setText(_translate("MainWindow", "Левая граница"))
        self.label_17.setText(_translate("MainWindow", "Правая граница"))
        self.label_19.setText(_translate("MainWindow", "Точность"))
        self.save.setText(_translate("MainWindow", "Сохранить в файл"))
        self.pushButton.setText(_translate("MainWindow", "Сменить метод"))

    def updateGraph(self, a, b):
        delta = abs(b-a) / 100
        values = []
        plots = []
        for i in range(100):
            plots.append(a + i * delta)
            values.append(self.function(a + i * delta))
        self.graph.clear()
        self.graph.plot(plots, values)

    def changeMethod(self):
        index = self.stackedWidget.currentIndex()
        if (index > 1):
            index = 0
        else:
            index = index + 1
        self.stackedWidget.setCurrentIndex(index)

    def HordesInit(self):
        try:
            a = float(self.left.text())
            b = float(self.right.text())
            acc = float(self.accuracyhords.text())
            if not self.validateParams(a, b, a):
                raise ValueError
            self.error.setText('')
            delta = abs( b - a )
            self.updateGraph( a - delta * 0.1, b + delta * 0.1 )
            data = numath.Hordes(self.function, a, b, acc)
            self.data = data
            model = tablemodel.TableModel(data, ["a", "b", "x", "F(a)", "F(b)", "F(x)", "|x_(i+1) - x_i"])
            self.table.setModel(model)
            self.table.update()
        except ValueError:
            self.error.setText('Invalid params')
        except numath.RequirementException:
            self.error.setText("Convergence requirements faild")

    def NewtonInit(self):
        try:
            a = float(self.leftNewtone.text())
            b = float(self.rightNewtone.text())
            approx = float(self.approxNewton.text())
            acc = float(self.accuracyNewton.text())
            if not self.validateParams(a, b, approx):
                raise ValueError
            self.error.setText('')
            delta = abs( b - a )
            self.updateGraph( a - delta * 0.1, b + delta * 0.1 )
            data = numath.Newton(self.function, a, b, approx, acc)
            self.data = data
            model = tablemodel.TableModel(data, ["x", "f(x)", "f'(x)", "x_(n+1)", "|x_(n+1) - x_n|"])
            self.table.setModel(model)
            self.table.update()
        except ValueError:
            self.error.setText('Invalid params')
        except numath.RequirementException:
            self.error.setText("Convergence requirements faild")

    def IterationInit(self):
        try:
            a = float(self.leftIter.text())
            b = float(self.rightIter.text())
            approx = float(self.approx_Iter.text())
            acc = float(self.approx_Iter.text())
            if not self.validateParams(a, b, approx):
                raise ValueError
            self.error.setText('')
            delta = abs( b - a )
            self.updateGraph( a - delta * 0.1, b + delta * 0.1 )
            data = numath.Iteration(self.function, a, b, approx, acc)
            self.data = data
            model = tablemodel.TableModel(data, ["x_i", "x_(i+1)", "phi(x)", "f(x)", "|x_(i+1) - x_i|"])
            self.table.setModel(model)
            self.table.update()
        except ValueError:
            self.error.setText("Invalid Params")
        except numath.RequirementException:
            self.error.setText("Convergence requirements faild")
        except numath.RootOutOfRange:
            self.error.setText("Root out of range")

    def validateParams(self, a, b, approx):
        if (b > a and approx <= b and approx >= a):
            return True
        else:
            return False

    def saveToFile(self):
        openfile = QtGui.QFileDialog.getOpenFileName(self, 'Open file')[0]
        f = open(openfile, 'w')
        data = self.data
        for d in data:
            f.write(','.join(list(map(str, d))))
        f.close()